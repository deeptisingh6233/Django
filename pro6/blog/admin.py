from django.contrib import admin

# Register your models here.
@admin.Register(Blog)
class BlogAdmin(admin.Model.Admin):
       list_display=['title' ,'content' , 'created_at']
       