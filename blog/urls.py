from django.urls import path, include
from rest_framework.routers import DefaultRouter
from blog.views import BlogPostListViewSet, BlogPostDetailViewSet, BlogPostCreateViewSet, BlogPostUpdateViewSet, \
    BlogPostDeleteViewSet, BlogPostViewSet

router = DefaultRouter()
router.register(r'blog_posts', BlogPostListViewSet, basename='blog_posts')
router.register(r'blog-post', BlogPostDetailViewSet, basename='blog_post')
router.register(r'blog-post_create', BlogPostCreateViewSet, basename='blog_post_create')
router.register(r'blog-post_update', BlogPostUpdateViewSet, basename='blog_post_update')
router.register(r'blog-post_delete', BlogPostDeleteViewSet, basename='blog_post_delete')

router.register(r'blogposts', BlogPostViewSet, basename='blogpost')

urlpatterns = [
    path('', include(router.urls)),
]
