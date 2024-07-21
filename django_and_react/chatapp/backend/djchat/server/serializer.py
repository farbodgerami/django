from rest_framework import serializers

from .models import *

class ChannelSerializer(serializers.ModelSerializer):
    owner=serializers.SerializerMethodField(read_only=True)
    server=serializers.SerializerMethodField(read_only=True)
    class Meta:
     model=Channel
     fields='__all__'
    def get_owner(self,obj):
       return obj.owner.username
    def get_server(self,obj):
       return obj.server.name
    
class ServerSerializer(serializers.ModelSerializer):
    channel_server=ChannelSerializer(many=True)
    num_members=serializers.SerializerMethodField()
    # category=serializers.SerializerMethodField(read_only=True)
    category=serializers.StringRelatedField()

    class Meta:
        model=Server
        # fields='__all__'
        # dar in ja nemikhaim har bar ke server ha seda zade shodand hesazan member ro ham begire va namayesh bede pass:
        exclude=("member",)
        
    def get_num_members(self,obj):
        if hasattr(obj,"num_members"):
           return obj.num_members
            # print('kkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk',obj.num_membersl())
            # return  obj.num_membersl()
        return None
    # def get_category(self,obj):
    #     return obj.category.name
    
    # in hich arzeshi nadara vali shayad ye rooz ye jai be dard bokhore:
    def to_representation(self, instance,): 
       data= super().to_representation(instance)
       num_members=self.context.get("num_members")
       if not num_members:
          data.pop("num_members",None)
       return data

class CategorySerializer(serializers.ModelSerializer):
   class Meta:
      model=Category
      fields="__all__"