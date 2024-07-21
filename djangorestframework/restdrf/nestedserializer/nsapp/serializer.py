from dataclasses import field
from .models import *
from rest_framework import serializers

class Bookserializer(serializers.ModelSerializer):
    # author=serializers.ReadOnlyField(source='author.firstname')
    
    class Meta:
        model=Book
        fields=['id','author','title','ratings']

class Authorserializer(serializers.ModelSerializer):
    books=Bookserializer(read_only=True,many=True)
    class Meta:
        model=Author
        fields='__all__'