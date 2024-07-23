from django.urls import path
from . import views

"""
the app_name variable allows us to organise URLs by application and use the
name when reffering to them.
"""
app_name = 'blog'

urlpatterns = [
    # post views
    # path('', views.post_list, name='post_list'),
    path('', views.PostListView.as_view(), name='post_list'),
    path(
        '<int:year>/<int:month>/<int:day>/<slug:post>/',
        views.post_detail,
        name='post_detail'),
    path(
        '<int:post_id>/comment/', views.post_comment, name='post_comment'
    ),
]

"""
Note: We use angle brackets to capture values from the URL. Any value specified
in the URL pattern as a <parameter> is captured as a string. You use path
converters such as <int:year>, to specifically match and return an integer.
E.g: <slug:post> would specifically match a slug.

Also note that if class based views are going to be used for post list then the
blog/list.html template needs to change as the generic view passes the page
number reuqested in a variable called page_obj. So line 22:
{% include "pagination.html" with page=posts %}  now becomes:
{% include "pagination.html" with page=page_obj %}
"""
