from django.urls import path
from . import views


urlpatterns = [

    path('student/' ,views.get_student , name='get_student'),
    path('student/add', views.add_student, name='add_student'),
    path('patch/<int:pk>/', views.partially_add , name='partially_add'),
    path('put/<int:pk>/',views.fully_update , name='fully_update'),
    path('delete/<int:pk>/' ,views.delete_student , name='delete_student'),
]
