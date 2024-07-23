""" imports """
from django.conf import settings
from django.db import models
from django.urls import reverse


class PublishedManager(models.Manager):
    """
    This creates a custom manager. It allows us to retrieve posts using
    code like Post.published.all()
    Note: All models come with a default manager - the objects manager
    for example Post.objects.all()
    """

    def get_queryset(self) -> models.QuerySet:
        return super().get_queryset().filter(status=Post.Status.PUBLISHED)


class Post(models.Model):
    """ data model for a post """
    class Status(models.TextChoices):
        DRAFT = 'DF', 'Draft'
        PUBLISHED = 'PB', 'Published'

    title = models.CharField(max_length=200)
    slug = models.SlugField(
        max_length=210,
        unique_for_date='created_on'
    )
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='blog_posts'
    )
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    status = models.CharField(
        max_length=2,
        choices=Status,
        default=Status.DRAFT
    )
    # the default manager
    objects = models.Manager()
    # our custom manager
    published = PublishedManager()

    class Meta:
        """
        This class defines the meta data for the model
        ordering is tell django that it should sort results by the updated_on
        field (latest first indicated by '-')
        indexes allows us to define the database indexing for this model
        """
        ordering = ['-updated_on']
        indexes = [
            models.Index(fields=['-updated_on']),
        ]

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse(
            "blog:post_detail",
            args=[
                self.created_on.year,
                self.created_on.month,
                self.created_on.day,
                self.slug
            ]
        )


class Comment(models.Model):
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name="comments"
    )
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField(max_length=800)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['created_on']
        indexes = [
            models.Index(fields=['created_on']),
        ]

    def __str__(self):
        return f'Comment by {self.name} on {self.post}'
