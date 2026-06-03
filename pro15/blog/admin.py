from django.contrib import admin

# Register your models here.
from .models import UserList

@admin.register(UserList)
class UserListAdmin(admin.ModelAdmin):
       list_display=('name','subscriber')
