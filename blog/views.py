from rest_framework import viewsets, mixins, status
from rest_framework.response import Response

from blog.models import BlogPost
from blog.serializers import BlogPostListSerializer, BlogPostDetailSerializer, BlogPostCreateUpdateSerializer


class BlogPostListViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostListSerializer


class BlogPostDetailViewSet(mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostDetailSerializer


class BlogPostCreateViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostCreateUpdateSerializer


class BlogPostUpdateViewSet(mixins.UpdateModelMixin, viewsets.GenericViewSet):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostCreateUpdateSerializer



class BlogPostDeleteViewSet(mixins.DestroyModelMixin, viewsets.GenericViewSet):
    queryset = BlogPost.objects.filter(deleted=False)



class BlogPostViewSet(viewsets.ModelViewSet):
    queryset = BlogPost.objects.filter(deleted=False)

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return BlogPostDetailSerializer
        elif self.action == 'create':
            return BlogPostCreateUpdateSerializer
        elif self.action == 'update':
            return BlogPostCreateUpdateSerializer

        else:
            return BlogPostListSerializer


    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.deleted = True
        instance.save()
        return Response(status=status.HTTP_204_NO_CONTENT)
