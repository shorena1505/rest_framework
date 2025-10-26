from rest_framework import serializers

from blog.models import BlogPost


class BlogPostListSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogPost
        fields = ['id', 'title']


class BlogPostDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogPost
        fields = ['id', 'title', 'author', 'published']


class BlogPostCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogPost
        fields = ['title', 'author']


