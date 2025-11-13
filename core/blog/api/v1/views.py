from rest_framework.decorators import api_view,permission_classes
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
# from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework import viewsets, mixins
from rest_framework.decorators import action

from django_filters.rest_framework import DjangoFilterBackend
import json

# @api_view()
# def PostList(request):
#     # post=Post.objects.all( )
#     post=Post.objects.filter(id=1)
#     serializer=PostSerializer(post,many=True) 
#     return Response(serializer.data)
# @api_view(["GET","POST"])
# # in hatman bayad baad az api_view bashe
# @permission_classes([IsAuthenticated])
# def PostList(request):
#     if request.method =="GET":
#         post=Post.objects.filter(status=True)
#         serializer=PostSerializer(post,many=True) 
#         return Response(serializer.data)
#     elif request.method =="POST":
#         serializer=PostSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors)
        
# @api_view()
# def PostDetail(request,id):
    # try:
    #     post=Post.objects.get(id=id)
    #     # print(post)
    #     # # nokte in ke dar content bayad string besoorate json bashe vagarna error mide.
    #     # a=json.loads(post.content)
    #     # aa=Post.objects.filter(id=id) 
    #     # print(aa)
    #     # z=list(aa ) # <QuerySet [<Post: g>]> => [<Post: g>]
    #     # jj=aa.values() #<QuerySet [{'id': 1, 'title': 'g', 'content': '{"a":"b"}'....utc)}]>
    #     # kk=list(jj) #[{'id': 1, 'title': '...ezone.utc)}]
    #     # print(kk)
    #     # print(post.__dict__){'_state': <django.db.models.base.ModelState object at 0x74387e37bca0>, 'id': 1, 'title': 'g', 'content': '{"a":"b"}', 'status': False, 'category_id': 1, 'image': 'j.png', 'author_id': 1, 'created_date': datetime.datetime(2025, 11, 6, 19, 33, 38, 562760, tzinfo=datetime.timezone.utc), 'updated_date': datetime.datetime(2025, 11, 7, 20, 16, 28, 890568, tzinfo=datetime.timezone.utc), 'published_date': datetime.datetime(2025, 11, 6, 19, 33, 26, tzinfo=datetime.timezone.utc)}
    #     post=PostSerializer(post,many=False).data 
    #     return Response(post)
    # except Post.DoesNotExist:
    #     # return Response({"detail":"doesnot exist"},status=404)
    #     return Response({"detail":"doesnot exist"},status=status.HTTP_404_NOT_FOUND)
    # post=get_object_or_404(Post,pk=id)
    # serializer=PostSerializer(post,many=False) 
    # return Response(serializer.data)

# @api_view(["GET","PUT","DELETE"])
# def PostDetail(request,id):
#     post=get_object_or_404(Post,pk=id, )
#     if request.method =="GET":
#         serializer=PostSerializer(post) 
#         return Response(serializer.data)
#     elif request.method =="PUT":
#         serializer=PostSerializer(post,data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data)
#     elif request.method=="DELETE":
#         post.delete()
#         return Response({"detail":"item removed"},status=status.HTTP_204_NO_CONTENT)
        
# class PostList(APIView):
#     # in baes mishe oon jadvale biad:
    
#     serializer_class=PostSerializer
#     def get(self,request):
#         # print('fffffffffffffffffffffff', request.build_absolute_uri())

#         posts=Post.objects.all()

#         serializer = PostSerializer(posts, context={'request': request,},many=True)
#         return Response(serializer.data)

#     def post(self,request):
#         serializer = PostSerializer(data=request.data )
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data)

#     permission_classes = (IsAuthenticated, )

# class PostDetail(APIView):
#     # filter_backends = [DjangoFilterBackend]
#     # filterset_fields = ['category', 'author','status',]
#     serializer_class=PostSerializer

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
#     permission_classes = (IsAuthenticated, )
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


# class PostList(GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin):
#     filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
#     # filterset_fields = ['category', 'author','status',]
#     # vase vaghti ke masalan mikhaim begim ab=x&ab=y.. masalan: category__in=1,2...
 
#     filterset_fields = {
#         "category": ["exact", "in"],
#         "author": ["exact"],
#         "status": ["exact"],
#     }
#     search_fields = ["title", "content"]
#     ordering_fields = ["published_date"]
#     pagination_class = LargeResultsSetPagination

#     serializer_class = PostSerializer
#     queryset = Post.objects.all()

#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)

#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)


# class PostDetail(
#     GenericAPIView,
#     mixins.RetrieveModelMixin,
#     mixins.UpdateModelMixin,
#     mixins.DestroyModelMixin,
# ):
#     serializer_class = PostSerializer
#     # permission_classes = (IsAuthenticated,)
#     queryset = Post.objects.all()
#     # ya bayad be pk taghir bedim ya lookup field dashte bashim:
#     lookup_field = "id"

#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)

#     def put(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)

#     def delete(self, request, *args, **kwargs):
#         return self.destroy(request, *args, **kwargs)


# class PostList(ListCreateAPIView):
#     serializer_class=PostSerializer
#     queryset=Post.objects.all()
#     permission_classes = (IsAuthenticated, )


# class PostDetail (RetrieveUpdateDestroyAPIView):
#     serializer_class=PostSerializer
#     lookup_field='id'
#     permission_classes = (IsAuthenticated, )
#     queryset=Post.objects.all()
# important just viewset and modelviewset:
from rest_framework import viewsets
class PostViewSet(viewsets.ViewSet):
    serializer_class=PostSerializer
    queryset=Post.objects.all()
    permission_classes = (IsAuthenticated, )
    
    
    # filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    # filterset_fields = ['category', 'author','status',]
    # vase vaghti ke masalan mikhaim begim ab=x&ab=y.. masalan: category__in=1,2...
 
    # filterset_fields = {
    #     "category": ["exact", "in"],
    #     "author": ["exact"],
    #     "status": ["exact"],
    # }
    # search_fields = ["title", "content"]
    # ordering_fields = ["published_date"]
    # pagination_class = LargeResultsSetPagination


    def list(self,request):
        serializer=self.serializer_class(self.queryset , context={'request': request,} ,many=True)
        return Response(serializer.data)

    def retrieve(self,request,pk=None):
        post_object=get_object_or_404(self.queryset,pk=pk)
        serializer=self.serializer_class( post_object, context={'request': request,} )
        return Response(serializer.data)
    def create(self,request):
        pass

    def put(self,request):
        pass

    def partial_update(self,request):
        pass

    def destroy(self,request):
        pass

class PostViewSet(viewsets.ModelViewSet):


    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['category', 'author','status',]
    # vase vaghti ke masalan mikhaim begim ab=x&ab=y.. masalan: category__in=1,2...
 
    # filterset_fields = {
    #     "category": ["exact", "in"],
    #     "author": ["exact"],
    #     "status": ["exact"],
    # }
    # search_fields = ["title", "content"]
    # ordering_fields = ["published_date"]
    # pagination_class = LargeResultsSetPagination
    
    
    serializer_class=PostSerializer
    queryset=Post.objects.all()
    permission_classes = (IsAuthenticated, )
    # filter_backends=[DjangoFilterBackend]
    # filterset_fields = ['category', 'author','status',]


    # @action(methods=["get"],detail=False)
    # def get_ok(self,request):
    #     return Response({'detail':'ok'})

class CategoryViewSet(viewsets.ModelViewSet):
    serializer_class=CategorySerializer
    queryset=Category.objects.all()
    permission_classes = (IsAuthenticated, )
