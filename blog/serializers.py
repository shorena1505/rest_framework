from rest_framework import serializers


class BlogPostSerializer(serializers.Serializer):
    id=serializers.IntegerField(required=False)
    title = serializers.CharField(max_length=100)
    author = serializers.CharField()
    published = serializers.DateTimeField()