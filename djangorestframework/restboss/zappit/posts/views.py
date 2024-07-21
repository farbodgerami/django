from rest_framework.exceptions import ValidationError
from django.shortcuts import render
from rest_framework import generics,permissions

from .serializers import *
from .models import *
class Postlist(generics.ListCreateAPIView):
    queryset=Post.objects.all()
    serializer_class=Postserializer
    # vase inke ke auth shodeha bebinan va taghir bedan va gharibeha faghat bebinan
    permission_classes=[permissions.IsAuthenticatedOrReadOnly]
    def perform_create(self, serializer):
        serializer.save(poster=self.request.user)


class Votecreate(generics.CreateAPIView):
 
    serializer_class=Voteserializer
    # vase inke ke auth shodeha bebinan va taghir bedan va gharibeha faghat bebinan
    permission_classes=[permissions.IsAuthenticated]
    def get_queryset(self):
        user=self.request.user
        post=Post.objects.get(pk=self.kwargs['pk'])
        # vase search badan be karet miad
        return Vote.objects.filter(voter=user,post=post)
    def perform_create(self, serializer):
        if self.get_queryset().exists():raise ValidationError('already voted')
        serializer.save(voter=self.request.user,post=Post.objects.get(pk=self.kwargs['pk']))
