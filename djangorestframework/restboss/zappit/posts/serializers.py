from rest_framework import serializers
from .models import *
class Postserializer(serializers.ModelSerializer):
    postername=serializers.ReadOnlyField(source='poster.username')
    poster_id=serializers.ReadOnlyField(source='poster.id')
    
    class Meta:
        model=Post
        fields=['id','title','url','postername','poster_id','created']
 
class Voteserializer(serializers.ModelSerializer):
    class Meta:
        model=Vote
        fields=['id',]
 