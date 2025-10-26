from django.urls import path
from blog.views import create_blog_post, blog_post_list_create, BlogPostList

urlpatterns = [
    path('create_blog_post/', create_blog_post, name='create_blog_post'),
    path('blog_post_list_create/', blog_post_list_create, name='blog_post_list_create'),
    path('blog_post-list_class/', BlogPostList.as_view(), name='BlogPostList'),
]
