from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse

# getting usermodel object:
# this may can be used for using user model in microservices
User = get_user_model()


class Post(models.Model):
    title = models.CharField(max_length=250)
    content = models.TextField()
    status = models.BooleanField()
    
    # vase inke age category delete shod post pak nashe
    category = models.ForeignKey("Category", on_delete=models.SET_NULL, null=True)
    image = models.ImageField(null=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    published_date = models.DateTimeField()

    def get_snippet(self):
        return self.content[0:5]

    def delete(self, *args, **kwargs):
        if self.image:
            self.image.delete()
        super().delete(*args, **kwargs)

    def get_absolute_api_url(self):
        return reverse("blog:api-v1:post-detail", kwargs={"id": self.id})

    def __str__(self):
        return self.title


class Category(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name
