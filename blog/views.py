from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render, redirect
from django.views.decorators.http import require_POST
from django.views.generic import ListView
from .forms import CommentForm
from .models import Post, Comment


def post_list(request):
    """
    The request parameter is required by all views!
    Here we get all posts using our custom manager (i.e the PublishedManager)
    It retrieves all posts with a status of PUBLISHED
    """
    post_list = Post.published.all()
    # Pagination with 3 posts per page
    paginator = Paginator(post_list, 3)
    page_number = request.GET.get('page', 1)
    try:
        posts = paginator.page(page_number)
    except PageNotAnInteger:
        # If page_number is not an integer get the first page
        posts = paginator.page(1)
    except EmptyPage:
        # If page_number is out of range get last page of results
        posts = paginator.page(paginator.num_pages)

    return render(
        request,
        'blog/post/list.html',
        {'posts': posts}
    )


def post_detail(request, year, month, day, post):
    """
    This post detail view takes the id arguement of a post. It uses the
    get_object_or_404 shortcut.
    If the post is not found a HTTP 404 exception is raised.
    """
    post = get_object_or_404(
        Post,
        status=Post.Status.PUBLISHED,
        slug=post,
        created_on__year=year,
        created_on__month=month,
        created_on__day=day
    )

    # List of active comments for this post
    comments = post.comments.filter(is_active=True)
    form = CommentForm()

    return render(
        request,
        'blog/post/detail.html',
        {
            'post': post,
            'comments': comments,
            'form': form
        }
    )


class PostListView(ListView):
    """
    Alternative post list view
    """
    queryset = Post.published.all()
    context_object_name = 'posts'
    paginate_by = 3
    template_name = 'blog/post/list.html'


@login_required
@require_POST
def post_comment(request, post_id):
    post = get_object_or_404(Post, id=post_id, status=Post.Status.PUBLISHED)
    form = CommentForm(data=request.POST)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.post = post
        comment.user = request.user
        comment.save()
        return redirect(
            'blog:post_detail',
            year=post.created_on.year,
            month=post.created_on.month,
            day=post.created_on.day,
            post=post.slug
        )
    return render(
        request,
        'blog/post/detail.html',
        {'post': post, 'form': form}
    )


@login_required
def edit_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id, user=request.user)

    if request.method == 'POST':
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            form.save()
            return redirect(
                'blog:post_detail',
                year=comment.post.created_on.year,
                month=comment.post.created_on.month,
                day=comment.post.created_on.day,
                post=comment.post.slug
            )
    else:
        form = CommentForm(instance=comment)
    return render(
        request,
        'blog/post/comment/edit_comment.html',
        {'form': form}
    )


@login_required
def delete_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id, user=request.user)
    post = comment.post
    if request.method == 'POST':
        comment.delete()
        return redirect(
            'blog:post_detail',
            year=post.created_on.year,
            month=post.created_on.month,
            day=post.created_on.day,
            post=post.slug
        )
    return render(
        request,
        'blog/post/comment/delete_comment.html',
        {'comment': comment}
    )
