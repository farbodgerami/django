from django.db import models
'''post for blog app'''
class Post(models.Model):
    title=models.CharField(max_length=250)
    content=models.TextField()
    status=models.BooleanField()
    category=models.ForeignKey('Category',on_delete=models.SET_NULL,null=True)
    image=models.ImageField(null=True,blank=True)
    author=models.ForeignKey('User',on_delete=models.CASCADE)
    created_date=models.DateTimeField(auto_now_add=True)
    updated_date=models.DateTimeField(auto_now=True)
    published_date=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
class Category(models.Model):
    name=models.CharField(max_length=250)

    def __str__(self):
        return self.name
