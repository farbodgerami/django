from operator import mod
from statistics import mode
from django.db import models
# vaseye taghire modele user darim:
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager


class Userprofilemanager(BaseUserManager):
      def create_user(self,email,name,password=None):
          if not email:
              raise ValueError('user must have an email address')
          email=self.normalize_email(email)
          user=self.model(email=email,name=name)
          user.set_password(password)
          user.save(using=self._db)
          return user
      def create_superuser(self,email,name,password):
          user=self.create_user(email,name,password)
          user.is_superuser=True
          user.is_staff=True
          user.save(using=self._db)
          return user


# user modele jadide ma:
class Userprofile(AbstractBaseUser,PermissionsMixin):

    email= models.EmailField(max_length=255,unique=True)
    name=models.CharField(max_length=255)
    is_active=models.BooleanField(default=True)
    is_staff=models.BooleanField(default=False)

    objects=Userprofilemanager()
    USERNAME_FIELD='email'
    REQUIRED_FIELDS=['name']
    def getfullname(self):
        return self.name

    def getshortname(self):
        return self.name
    
    def __str__(self):
        return self.email
