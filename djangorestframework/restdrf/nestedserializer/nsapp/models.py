from django.db import models

class Author(models.Model):
    firstname=models.CharField(max_length=20)
    lastname=models.CharField(max_length=20)
    def __str__(self):
        return self.firstname + self.lastname

class Book(models.Model):
    title=models.CharField(max_length=20)
    ratings=models.CharField(max_length=10)
    author=models.ForeignKey(Author,related_name='books',on_delete=models.CASCADE)

    