from dataclasses import field
from rest_framework import serializers
from .models import *

class Studentserializer(serializers.ModelSerializer):

    class Meta:
        model=Student
        fields=['id','name','testscore']

from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
class Userserializer(serializers.ModelSerializer):
   
    class Meta:
        model=User
        fields=('id','username','email','password',)
        extra_kwargs={'password':{'write_only':True,'required':False}}
    def create(self,validated_data):       
        user=User.objects.create_user(**validated_data)        
        Token.objects.create(user=user)
        return user