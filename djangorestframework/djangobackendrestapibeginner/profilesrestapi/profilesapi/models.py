from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager
# vase feed api:
from django.conf import Settings
from profilesproject import settings
class UserProfileManager(BaseUserManager):
    """manager for user profiles"""
    def create_user(self,email,name,password=None):
        """create a new user profile"""
        if not email:
            raise ValueError('User must have email')
        email = self.normalize_email(email)
        user = self.model(email=email, name=name)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self,email,name,password):
        """creates and saves a new superuser with given details"""
        user = self.create_user(email,name,password)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db) 
        return user

class UserProfile(AbstractBaseUser,PermissionsMixin):
    """database model for users in the system"""
    email=models.EmailField(max_length=255,unique=True)
    name=models.CharField(max_length=255)
    is_active=models.BooleanField(default=True)
    is_staff=models.BooleanField(default=False)
    # isf=models.BooleanField(default=False)
    objects=UserProfileManager()
    USERNAME_FIELD="email"
    # name pain hamoon username balast ke dar vaghe email hast
    REQUIRED_FIELDS=["name"]
    
    def getfullname(self):
        """retrieve full name"""
        return self.name
    def getshortname(self):
        '''retrieve shortname of user'''
        return self.name
    def __str__(self):
        """returns string representation of the user"""
        return self.email
      
class profilefeeditem(models.Model):
    """profile status update"""
    userprofile=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    statustext=models.CharField(max_length=255)
    createdon=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        """returns the model as a strign"""
        return self.statustext


     