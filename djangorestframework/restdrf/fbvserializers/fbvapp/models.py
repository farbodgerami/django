 

from django.db import models

class Student(models.Model):
    id=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=255)
    testscore=models.DecimalField(max_digits=10,decimal_places=3)
    def __str__(self):
        return self.id + self.name + self.testscore