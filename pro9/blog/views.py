from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse

def set_cookie(request):
       response=HttpResponse("setup of cookie")
       response.set_cookie('username' , 'mohit' , max_age=60*60*24*7)
       response.set_cookie('cource ',"python " , max_age=60*60*24*7)
       
       return response

def get_cookie(request):
       username=request.COOKIES.get("username", 'guest')
       cource=request.COOKIES.get('cource' , 'java')
       return HttpResponse(f'username is {username} and cource opted is {cource}')

def delete_cookie(request):
       response=HttpResponse("cookie deleted sucessfully")
       response.delete_cookie('username')
       response.delete_cookie("cource")
       return response