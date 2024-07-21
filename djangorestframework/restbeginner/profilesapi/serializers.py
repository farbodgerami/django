from rest_framework import serializers

class helloserializer(serializers.Serializer):
    name=serializers.CharField(max_length=255)