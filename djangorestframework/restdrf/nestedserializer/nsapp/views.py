from .models import *
from .serializer import *
from rest_framework import generics
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated,DjangoModelPermissions


class Autorlistview(generics.ListCreateAPIView):
    queryset=Author.objects.all()
    serializer_class=Authorserializer
    # login using BasicAuthentication
    authentication_classes=[BasicAuthentication]
    # api is acceable only if user is authed
    permission_classes=[IsAuthenticated,DjangoModelPermissions]

class Authordetailview(generics.RetrieveUpdateDestroyAPIView):
    queryset=Author.objects.all()
    serializer_class=Authorserializer

class Booklistview(generics.ListCreateAPIView):
    queryset=Book.objects.all()
    serializer_class=Bookserializer

class Bookdetailview(generics.RetrieveUpdateDestroyAPIView):
    queryset=Book.objects.all()
    serializer_class=Bookserializer
