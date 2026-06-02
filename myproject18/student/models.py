from django.db import models

# Create your models here.

class Student(models.Model):
       Name=models.CharField()
       age=models.IntegerField()
       email=models.EmailField()

       def __str__(self):
           return self.name