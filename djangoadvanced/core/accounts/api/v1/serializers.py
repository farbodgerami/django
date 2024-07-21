from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password
from ...models import *
from django.core import exceptions


class RegisterationSerializer(serializers.ModelSerializer):
    password1 = serializers.CharField(max_length=255, write_only=True)

    # password2=serializers.CharField(max_length=255,write_only=True)
    class Meta:
        model = User
        fields = ["email", "password", "password1"]

    def validate(self, attrs):
        if attrs["password"] != attrs["password1"]:
            raise serializers.ValidationError({"detail": "password doesn't match"})
        try:
            validate_password(attrs["password"])
        except exceptions.ValidationError as e:
            raise serializers.ValidationError({"password": list(e.messages)})
        return super().validate(attrs)

    def create(self, validated_data):
        validated_data.pop("password", None)
        return User.objects.create_user(**validated_data)
