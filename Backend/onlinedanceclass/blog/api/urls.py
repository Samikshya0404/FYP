"""Home Api Urls
"""

from django.urls import path
from blog.api.views import BlogListApi, BlogDetailView

urlpatterns = [
    path('get_blog_list', BlogListApi.as_view(), name="blog_list"),
    path('get_blog_details/<int:pk>', BlogDetailView.as_view(), name="blog_details"),

]


