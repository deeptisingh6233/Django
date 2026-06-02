from django.shortcuts import render 
from django.http import HttpResponse
from django.template.loader import render_to_string
# Create your views here.

from django.core.mail import send_mass_mail, EmailMultiAlternatives

"""def send_bulk_email(request):
       message1=['subject to user 1', 'content to be sent','deeptisinghclassx@gmail.com' ,['deeptisingh6233@gmail.com']]
       message2=['subject to user 2', 'content to be sent','deeptisinghclassx@gmail.com' ,['deeptisingh6233@gmail.com']]
       message3=['subject to user 3', 'content to be sent','deeptisinghclassx@gmail.com' ,['deeptisingh6233@gmail.com']]

       send_mass_mail((message1,message2,message3),fail_silently=False)
       return HttpResponse('Bulk Mail Sent sucessfully')"""

def send_bulk_email(request):
       subject='Welcome to our platform'
       from_email='deeptisinghclassx@gmail.com'
       recipient_list=['deeptisingh6233@gmail.com', 'deeptisingh2336789@gmail.com']

       html_content=render_to_string('welcome_email.html',{'username':'MOhit'})

       msg=EmailMultiAlternatives(subject,"welcome to my platform hope u are doing well in your life" , from_email,recipient_list)
       msg.attach_alternative(html_content,'text/html')
       msg.send()

       return HttpResponse('Bulk Email Send Sucessfully')