from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Product, Review
from rest_framework_simplejwt.tokens import RefreshToken ,AccessToken


class Reviewserializer(serializers.ModelSerializer):
    class Meta:
        model=Review
        fields='__all__'

class Productserializer(serializers.ModelSerializer):
    reviews=serializers.SerializerMethodField(read_only=True)
    class Meta:
        model=Product
        fields='__all__'
    def get_reviews(self,obj):
        # reviews=obj.review_set.all()
        reviews=Review.objects.filter(product=obj)
        serializer=Reviewserializer(reviews,many=True)
        return serializer.data
    
class Userserializer(serializers.ModelSerializer):
    name=serializers.SerializerMethodField(read_only=True)
    _id=serializers.SerializerMethodField(read_only=True)
    isadmin=serializers.SerializerMethodField(read_only=True)
    class Meta:
        model=User
        fields=['_id','username','email','name','isadmin']
        # fields='__all__'
    def get_name(self,obj):
        name=obj.first_name
        if name=='':
            name=obj.email
        return name
    
    def get__id(self,obj):
        _id=obj.id
        return _id

    def get_isadmin(self,obj):
        isadmin=obj.is_staff
        return isadmin

class Userserializerwithtoken(Userserializer):
    
    token=serializers.SerializerMethodField(read_only=True)
    class Meta:
        model=User
        fields=['id','_id','username','email','name','isadmin','token']
        # fields='__all__'
    def get_token(self,obj):
        
        # token=RefreshToken.for_user(obj)
        token=AccessToken.for_user(obj)
        return str(token)

