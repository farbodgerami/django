from typing import Iterable
from django.db import models
from django.db.models import Count
from django.dispatch import receiver
from django.shortcuts import get_object_or_404
# Create your models here.
from account.models import *
from .validator import*

# def categoryIconUploadPath(instance,filename):
#     return f"category/"
class Category(models.Model):
    name=models.CharField(max_length=100) 
    description=models.TextField(blank=True,null=True)
    icon=models.FileField(null=True,blank=True,upload_to="images/category/")
    def delete(self, *args, **kwargs):
     if self.icon:
        self.icon.delete()
     super().delete(*args, **kwargs)
    #  vase replace kardan:
    def save(self,*args,**kwargs):
        if self.id:
            existing=get_object_or_404(Category,id=self.id)
            if existing.icon != self.icon:
                existing.icon.delete(save=False)
        super().save(*args,**kwargs)
  
    def __str__(self) -> str:
        return self.name

class Server(models.Model):
    name=models.CharField(max_length=100) 
    owner=models.ForeignKey(Account,on_delete=models.CASCADE ,related_name='server_owner')
    category=models.ForeignKey(Category,on_delete=models.CASCADE ,related_name='server_category')
    description=models.CharField(max_length=250,blank=True,null=True)
    # dastan ine ke dar teori mishe berim be account va oonja ye foreignkey be server bedim. va ralatedname ro bedim owner-server vali designe sheti hast
    # ye rahe dige ine ke ye class be name member tarif konim va be server va user foreinkey bedim ke albate query zadanesh yejoor dge mishe
    # nokte: agar listi az bala dasti bekhaim az manytomany estefade mikonim. hal agar bekhaim dar baladasti listi az pain dasti dashte bashim
    # az related name estefade mikonim. yani dar inja baraye gereftane memeberh a az manytomany va baraye in ke oon ozv bebine dar kodoom serverha osz hast
    # ralatedname ro ezafe mikonim     member=models.ManyToManyField(Account, related_name='listOfserversmemberJoined')
    member=models.ManyToManyField(Account ,blank=True )
    # vase gereftane member ha in ham mishe:
    # def num_membersl(self):
    #     return self.member.count()
    banner=models.ImageField(upload_to='images/banners/',blank=True,null=True)
    icon=models.ImageField( upload_to='images/icons',blank=True,null=True , validators=[validateIconImageSize,validateImageFileExtension])

    def delete(self, *args, **kwargs):
        if self.icon:
            self.icon.delete()
        if self.banner:
            self.banner.delete()
        super().delete(*args, **kwargs)
    #  vase replace kardan:
    def save(self,*args,**kwargs):
        self.name=self.name.lower()
        if self.id:
            existing=get_object_or_404(Server,id=self.id)
            if existing.icon != self.icon:
                existing.icon.delete(save=False)
            if existing.banner != self.icon:
                existing.banner.delete(save=False)
        super().save(*args,**kwargs)
    

    
    def __str__(self) -> str:
        return self.name

class Channel(models.Model):
    name=models.CharField(max_length=100) 
    owner=models.ForeignKey(Account,on_delete=models.CASCADE ,related_name='channel_owner')
    topic=models.CharField(max_length=250,blank=True,null=True)
    server=models.ForeignKey(Server,on_delete=models.CASCADE,related_name='channel_server')

 
  
    def __str__(self) -> str:
        return self.name