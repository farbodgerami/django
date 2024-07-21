
from rest_framework import serializers
from .models import UserProfile
from profilesapi import models


class helloserializer(serializers.Serializer):
    name = serializers.CharField(max_length=15)


class UserProfileserializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        # fields='__all__'
        # oonai ke mikhaim namayesh dade beshe
        fields = ('id', 'email', 'name', 'password')
        extra_kwargs = {
            'password': {
                'write_only': True,
                'style': {'input_type': 'password'}
            }
        }

    def create(self, validated_data):
        """create and return a new user"""
        """it overrides the create functino"""
        user = UserProfile.objects.create_user(
            email=validated_data['email'],
            name=validated_data['name'],
            password=validated_data['password']

        )
        return user


class profilefeeditemserializer(serializers.ModelSerializer):
    """serializers profile feed items"""
    class Meta:
        model = models.profilefeeditem
        fields = ('id', 'userprofile', 'statustext', 'createdon')
        extra_kwargs = {
            'userprofile': {
                'read_only': True,
            }
        }
