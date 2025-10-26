from rest_framework import response, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

import blog
from blog.models import BlogPost
from blog.serializers import BlogPostSerializer


@api_view(['POST'])
def create_blog_post(request):
    serializer=BlogPostSerializer(data=request.data)
    if serializer.is_valid():
       return Response(serializer.validated_data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
def blog_post_list_create(request):
    if request.method == 'GET':
        blogs = BlogPost.objects.all()
        serializer = BlogPostSerializer(blogs, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = BlogPostSerializer(data=request.data)
        if serializer.is_valid():
            BlogPost.objects.create(**serializer.validated_data)
            return Response(serializer.validated_data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BlogPostList(APIView):
    def get(self, request):
        blogs = BlogPost.objects.all()
        serializer = BlogPostSerializer(blogs, many=True)
        return Response(serializer.data)
    def post(self, request):
        serializer = BlogPostSerializer(data=request.data)
        if serializer.is_valid():
            BlogPost.objects.create(**serializer.validated_data)
            return Response(serializer.validated_data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
