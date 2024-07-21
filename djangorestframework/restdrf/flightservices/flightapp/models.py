from turtle import ondrag
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.conf import settings

class Flight(models.Model):
    flightnumber=models.CharField(max_length=10)
    operatingairlines=models.CharField(max_length=20)
    departurecity=models.CharField(max_length=20,blank=True,null=True)
    arrivalcity=models.CharField(max_length=20)
    dateofdeparture=models.DateField()
    estimatedtimeofdeparture=models.TimeField()
    def __str__(self):
        return self.flightnumber


class Passengar(models.Model):
    firstname=models.CharField(max_length=20)
    lastname=models.CharField(max_length=20)
    middlename=models.CharField(max_length=20)
    email=models.CharField(max_length=20)
    phone=models.CharField(max_length=10)
    def __str__(self):
        return self.firstname + ' ' + self.lastname

class Reservation(models.Model):
    # one flight can be a part of multiple reservations:(onetomany)
    flight=models.ForeignKey(Flight,on_delete=models.CASCADE)
    passengar=models.OneToOneField(Passengar,on_delete=models.CASCADE)
# ba sakhte shodane user token ham khodesh sakhte beshe:
@receiver(post_save,sender=settings.AUTH_USER_MODEL)
def createauthtoken(sender,instance,created,**kwargs):
    if created:
        Token.objects.create(user=instance)
