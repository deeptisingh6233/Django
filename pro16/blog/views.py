from django.shortcuts import render

# Create your views here.
from .models import UserProfile
from django.core.cache import cache

def users_list(request):
       users=cache.get('user_list')

       if not users:
              print('cache is missed')
              users=UserProfile.objects.all()
              cache.set('users_list',users,timeout=60)
       else:
              print('cache hit retrival userr from cache')
       return render(request,'user_list.html' ,{'users':users})