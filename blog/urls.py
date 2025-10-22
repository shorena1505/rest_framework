from django.urls import path
from blog.views import create_blog_post

urlpatterns = [
    path('create_blog_post', create_blog_post, name='create_blog_post'),
]
