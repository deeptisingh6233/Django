from django.shortcuts import render
from .models import YouTubeUser
from django.core.cache import cache
# Create your views here.

def user_list(request):
       users=cache.get('users_data')#try to get data from cache

       if not users:
              print('cache Miss:Fetching data from database')
              users=YouTubeUser.objects.all()
              cache.set('users_data', users, timeout=300)
       else:
              print('fetching data from cache')
       return render(request,'user_list.html', {'users':users})