from rest_framework import serializers


class BlogPostSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=100)
    author = serializers.CharField()
    published = serializers.DateTimeField()