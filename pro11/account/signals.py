from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.core.mail import send_mail

@receiver(post_save,sender=User)
def send_welcome_mail(sender,instance,created,**kwargs):
       if created:
              print(f"New User Created {instance.username}")

              subject='welcome to mohit kumar' 
              message=f'Hi{instance.username} thankyou for registration to ohit kumar website'
              from_email='deeptisinghclassx@gmail.com'
              recipient_list=[instance.email]

              send_mail(subject,message,from_email,recipient_list, fail_silently=False)
              print(f'welcome email sent sucessfully')