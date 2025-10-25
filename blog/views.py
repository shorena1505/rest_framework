from rest_framework import response, status
from rest_framework.decorators import api_view
from rest_framework.response import Response


import blog
from blog.models import BlogPost
from blog.serializers import BlogPostSerializer


@api_view(['POST'])
def create_blog_post(request):
    serializer=BlogPostSerializer(data=request.data)
    if serializer.is_valid():
       return response.Response(serializer.validated_data)
    return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
def blog_post_list_create(request):
    if request.method == 'GET':
        blogs = BlogPost.objects.filter(author=request.user)
        serializer = BlogPostSerializer(blogs, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = BlogPostSerializer(data=request.data)
        if serializer.is_valid():
            BlogPost.objects.create(**serializer.validated_data)
            return Response(serializer.validated_data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
