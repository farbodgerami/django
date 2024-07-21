from datetime import datetime
from django.conf import settings
from django.db import models
from django.db.models.signals import post_save
from django.db import models
import datetime
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    paidnuntil = models.DateField(null=True, blank=True)
    email = models.EmailField(unique=True, blank=True)
    
    def setpaiduntil(self,dateortimestamp):
        if isinstance(dateortimestamp,int):
            paiduntil=datetime.date.fromtimestamp(dateortimestamp)
        elif isinstance(dateortimestamp,str):
            paiduntil=datetime.date.fromtimestamp(int(dateortimestamp))
        else:
            paiduntil=dateortimestamp
        self.paidnuntil=paiduntil
        self.save()

    def haspaid(self, currentdate=datetime.date.today()):
        if self.paidnuntil is None:
            return False
        return currentdate < self.paidnuntil


class Video(models.Model):
    title = models.CharField(max_length=30)
    thumbnail = models.FileField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Video'
        verbose_name_plural = 'Videos'

    def __str__(self):
        return f"{self.title}"


# import stripe
# membershipchoices=(('enterprise','ent'),('professional','pro'),('Free','free'))
# class Membership(models.Model):
#     slug=models.SlugField()
#     membershiptype=models.CharField(choices=membershipchoices,default='Free',max_length=30)
#     price=models.IntegerField(default=15)
#     stripplanid=models.CharField(max_length=255)
#     def __str__(self):
#         return self.membershiptype

# class Usermembership(models.Model):
#     user=models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
#     stripecustomerid=models.CharField(max_length=40)
#     mempership=models.ForeignKey(Membership,on_delete=models.SET_NULL,null=True)
#     def __str__(self):
#         return self.user.username
# def postsaveusermempershipcreate(sender,instance,created,*arg,**kwargs):
#     if created:
#         Usermembership.objects.get_or_create(user=instance)
#     usermempership,created= Usermembership.objects.get_or_create(user=instance)
#     if usermempership.stripecustomerid is None or usermempership.stripecustomerid == '':
#         newcustumerid=stripe.Customer.create(email=instance.email)
#         usermempership.stripecustomerid=new

# class Subscription(models.Model):
#     usermembership=models.ForeignKey(Usermembership,on_delete=models.CASCADE)
#     stripesubscriptionid=models.CharField(max_length=40)
#     active=models.BooleanField(default=True)
#     def __str__(self):
#         return self.usermembership.user.username