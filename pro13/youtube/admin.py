from django.contrib import admin
from .models import YouTubeUser
# Register your models here.
@admin.register(YouTubeUser)
class YouTubeUserAdmin(admin.ModelAdmin):
       disply_list=('name' ,'email','subscriber')