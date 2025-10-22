from rest_framework import response, status
from rest_framework.decorators import api_view
from blog.serializers import BlogPostSerializer


@api_view(['POST'])
def create_blog_post(request):
    serializer=BlogPostSerializer(data=request.data)
    if serializer.is_valid():
       return response.Response(serializer.validated_data)
    return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
