from django.shortcuts import render
from django.core.mail import EmailMessage
from django.http import HttpResponse
from django.template.loader import render_to_string


def send_test_email(request):
    subject = "Welcome to my blog"

    message = render_to_string(
        'email/welcome_email.html',
        {
            'username': 'mohit',
            'cource': 'django',
        }
    )

    email = EmailMessage(
        subject,
        message,
        'deeptisinghclassx@gmail.com',
        ['deeptisingh6233@gmail.com']
    )

    email.content_subtype = "html"  # Send HTML email
    email.send()

    return HttpResponse("Email sent successfully!")