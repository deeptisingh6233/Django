from django.urls import path
from .views import set_session, get_session, delete_session

urlpatterns = [
    path('set_session/', set_session, name='set_session'),
    path('get_session/', get_session, name='get_session'),
    path('delete_session/', delete_session, name='delete_session'),
]