from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import *
from ...models import Post
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.generics import (
    CreateAPIView,
    ListAPIView,
    ListCreateAPIView,
    RetrieveAPIView,
    RetrieveUpdateAPIView,
    RetrieveUpdateDestroyAPIView,
    DestroyAPIView,
    UpdateAPIView,
    GenericAPIView,
)
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from .permissions import *
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework import viewsets, mixins
from rest_framework.decorators import action


# class PostList(APIView):
#     serializer_class=PostSerializer
#     def get(self,request):

#         posts=Post.objects.all()

#         serializer = PostSerializer(posts, context={'request': request,},many=True)
#         return Response(serializer.data)

#     def post(self,request):
#         serializer = PostSerializer(data=request.data )
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data)

#     # permission_classes = (IsAuthenticated,IsOwnerOrReadOnly )

# class PostDetail(APIView):
#     # filter_backends = [DjangoFilterBackend]
#     # filterset_fields = ['category', 'author','status',]
#     serializer_class=PostSerializer
#     # permission_classes = (IsAuthenticated, )

#     def get(self,request,id):
#         post=get_object_or_404(Post,pk=id)
#         serializer=self.serializer_class(post,context={'request': request,})
#         # serializer = PostSerializer(post, context={'request': request,} )
#         return Response(serializer.data)

#     def put(self,request,id):
#         post=get_object_or_404(Post,pk=id)
#         serializer=self.serializer_class(post)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data)

#     def delete(self,request,id):
#         post=get_object_or_404(Post,pk=id)
#         post.delete()
#         return Response('item removed')
# ino estefade kon va modelviewset
# class PostList(GenericAPIView):
#     serializer_class=PostSerializer
#     queryset=Post.objects.all()
#     def get(self,request):

#         serializer = self.serializer_class(self.get_queryset(), context={'request': request,},many=True)
#         return Response(serializer.data)

#     def post(self,request):
#         serializer = self.serializer_class(data=request.data )
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
# return Response(serializer.data)

from .pagination import *


class PostList(GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin):
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    # filterset_fields = ['category', 'author','status',]
    # vase vaghti ke masalan mikhaim begimr ab=x&ab=y.. masalan: category__in=1,2...
    # https://django-filter.readthedocs.io/en/stable/
    filterset_fields = {
        "category": ["exact", "in"],
        "author": ["exact"],
        "status": ["exact"],
    }
    search_fields = ["title", "content"]
    ordering_fields = ["published_date"]
    pagination_class = LargeResultsSetPagination

    serializer_class = PostSerializer
    queryset = Post.objects.all()

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class PostDetail(
    GenericAPIView,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
):
    serializer_class = PostSerializer
    permission_classes = (IsAuthenticated,)
    queryset = Post.objects.all()
    # ya bayad be pk taghir bedim ya lookup field dashte bashim:
    lookup_field = "id"

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


# class PostList(ListCreateAPIView):
#     serializer_class=PostSerializer
#     queryset=Post.objects.all()
#     permission_classes = (IsAuthenticated, )


# class PostDetail (RetrieveUpdateDestroyAPIView):
#     serializer_class=PostSerializer
#     lookup_field='id'
#     permission_classes = (IsAuthenticated, )
#     queryset=Post.objects.all()

# class PostViewSet(viewsets.ViewSet):
#     serializer_class=PostSerializer
#     queryset=Post.objects.all()
#     permission_classes = (IsAuthenticated, )

#     def list(self,request):

#         serializer=self.serializer_class(self.queryset , context={'request': request,} ,many=True)
#         return Response(serializer.data)

#     def retrieve(self,request,pk=None):
#         post_object=get_object_or_404(self.queryset,pk=pk)
#         serializer=self.serializer_class( post_object, context={'request': request,} )
#         return Response(serializer.data)
#     def create(self,request):
#         pass

#     def put(self,request):
#         pass

#     def partial_update(self,request):
#         pass

#     def destroy(self,request):
#         pass


# class PostViewSet(viewsets.ModelViewSet):
#     serializer_class=PostSerializer
#     queryset=Post.objects.all()
#     permission_classes = (IsAuthenticated, )
#     filter_backends=[DjangoFilterBackend]
#     filterset_fields = ['category', 'author','status',]


#     # @action(methods=["get"],detail=False)
#     # def get_ok(self,request):
#     #     return Response({'detail':'ok'})

# class CategoryViewSet(viewsets.ModelViewSet):
#     serializer_class=CategorySerializer
#     queryset=Category.objects.all()
#     permission_classes = (IsAuthenticated, )
