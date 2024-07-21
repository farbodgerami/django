import imp
from rest_framework import serializers
from .models import *
import re
class Flightserializer(serializers.ModelSerializer):
    class Meta:
        model=Flight
        fields='__all__'
    def validate_flightnumber(self,flightnumber):
        if(re.match('^[a-zA-Z0-9]*$',flightnumber)==None):
            raise serializers.ValidationError('invalidflightnumber enter alphanumeric')
        return flightnumber
    def validate(self,data):
        print(data)
        return data

class Reservationserializer(serializers.ModelSerializer):
    flight=serializers.SerializerMethodField(read_only=True)
    passengar=serializers.SerializerMethodField(read_only=True)
    class Meta:
        model=Reservation
        fields='__all__'

    def get_flight(self,obj):
        name=obj.flight.flightnumber
        return name
    def get_passengar(self,obj):
        name=obj.passengar.firstname
        return name  

class Passengarserializer(serializers.ModelSerializer):
    class Meta:
        model=Passengar
        fields='__all__'