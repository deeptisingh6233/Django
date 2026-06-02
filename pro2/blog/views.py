from django.shortcuts import render
from django.contrib import messages

# Create your views here.
def show(request):
       messages.debug(request,"This is a debug message")
       messages.info(request,"this is infor mation tab")
       messages.success(request,"congrats u are sucessful")
       messages.warning(request,'alert')

       return render(request,'show_message.html')
