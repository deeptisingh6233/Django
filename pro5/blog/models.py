from django.db import models
from django.urls import reverse

class Post(models.Model):
       title=models.CharField(max_length=50)
       content=models.TextField()

       def __str__(self):
             return self.title

       def get_absolute_url(self):
              return reverse('post_details' ,args=[str(self.id)])

# Create your models here.
