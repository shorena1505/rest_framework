from rest_framework import serializers


class BlogPostSerializer(serializers.ModelSerializer):
    title = serializers.CharField(source='title', read_only=True)
    author = serializers.CharField(source='author', read_only=True)
    published = serializers.DateTimeField(source='published', read_only=True)