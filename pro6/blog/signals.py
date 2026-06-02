from django.db.models import pre_save, post_save
from django.dispatch import receiver 
from .models import Blog

@receiver(pre_save,sender='Blog')
      def before_save(sender,instance,**kwargs)
       print(f'About to save'{instance.title})

@receiver(post_save,sender='Blog')
      def after_save(sender,instance,**kwargs)
          print(f'data_saved'{instance.title})
          if created:
              print(f'this is done'{instance.title})
          else:
              print(f'not created'{instance.title})
