from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    user=models.ForeignKey(User,on_delete=models.SET_NULL,null=True)#agar user pak shod mahsool pak nashe
    name=models.CharField(max_length=200,null=True,blank=False)
    image=models.ImageField(null=True,blank=True,default='p.png')
    brand=models.CharField(max_length=200,null=True,blank=True)
    category=models.CharField(max_length=200,null=True,blank=True)
    description=models.TextField(null=True,blank=True)
    rating=models.DecimalField(max_digits=7,decimal_places=2,null=True,blank=True)
    numreviews=models.IntegerField(blank=True,null=True,default=0)
    price=models.DecimalField(max_digits=7,decimal_places=2)
    countinstocks=models.IntegerField(blank=True,null=True,default=0)
    createdat=models.DateTimeField(auto_now_add=True)
    # vase override kardane id
    _id=models.AutoField(primary_key=True,editable=False)
    def __str__(self):
        return self.name
    def delete(self, using=None, keep_parents=False):
        self.image.delete()
        super().delete()

class Review(models.Model):
    product=models.ForeignKey(Product,on_delete=models.SET_NULL,null=True)
    user=models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    name=models.CharField(max_length=200,null=True,blank=True)
    rating=models.IntegerField(blank=True,null=True,default=0)
    comment=models.TextField(null=True,blank=True)
    createdat=models.DateTimeField(auto_now_add=True,null=True, blank=True)
    _id=models.AutoField(primary_key=True,editable=False)
    def __str__(self):
        return str(self.rating)

class Order(models.Model):
    user=models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    paymentmethod=models.CharField(max_length=200,null=True,blank=True)
    taxPrice=models.DecimalField(max_digits=7,decimal_places=2)
    shipingprice=models.DecimalField(max_digits=7,decimal_places=2)
    totalprice=models.DecimalField(max_digits=7,decimal_places=2)
    ispaid=models.BooleanField(default=False)
    paidat=models.DateTimeField(auto_now_add=False,null=True, blank=True)
    isdelivered=models.BooleanField(default=False)
    deleverdat=models.DateTimeField(auto_now_add=False,null=True, blank=True)
    createdat=models.DateTimeField(auto_now_add=False,null=True, blank=True)
    _id=models.AutoField(primary_key=True,editable=False)

    def __str__(self):
        return str(self.createdat)

class Orderitem(models.Model):
    product=models.ForeignKey(Product,on_delete=models.SET_NULL,null=True)
    order=models.ForeignKey(Order,on_delete=models.SET_NULL,null=True)
    name=models.CharField(max_length=200,null=True,blank=True)
    qty=models.IntegerField(blank=True,null=True,default=0)
    price=models.DecimalField(max_digits=7,decimal_places=2)
    image=models.CharField(max_length=200,null=True,blank=True)
    _id=models.AutoField(primary_key=True,editable=False)
    def __str__(self):
        return self.name

class Shippingadress(models.Model):
    order=models.OneToOneField(Order,on_delete=models.CASCADE,null=True,blank=True)
    address=models.CharField(max_length=200,null=True,blank=True)
    city=models.CharField(max_length=200,null=True,blank=True)
    postalcode=models.CharField(max_length=200,null=True,blank=True)
    country=models.CharField(max_length=200,null=True,blank=True)
    shippingprice=models.DecimalField(max_digits=7,decimal_places=2)
    _id=models.AutoField(primary_key=True,editable=False)
    def __str__(self):
        return str(self.address)
