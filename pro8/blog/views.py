from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def set_session(request):
       request.session['username']='mohit'
       request.session['cource']='Python'
       return HttpResponse('"data added sucessfullly')

def get_session(request):
       username=request.session.get('username','guest')
       cource=request.session.get('cource', 'java')

       return HttpResponse(f"person'{username} is having the cource{cource}")

def delete_session(request):
       request.session.flush()
       return HttpResponse("evertything is deleted")