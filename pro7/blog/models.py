
from django.db import models




class Blog(models.Model):
       title=models.CharField( max_length=50)
       content=models.TextField
       created_at=models.TimeField(auto_now_add=False)

       def __str__(self):
              return self.title


# Create your models here.
