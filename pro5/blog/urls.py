from django.urls import path
from .views import PostListviews,postDetailsViews,PostUpdateView,PostDeleteView

urlpatterns=[
       path('' , PostListviews.as_view() , name='PostList'),
       path('post/<int:pk>/', postDetailsView.as_view() ,name='postDetails' ),
       path('post/new' , PostUpdateView.as_view() , name='PostUpdateView'),
       path('post/<int:pk>/delete/', PostDeleteView.as_view() , name='PostDelete'),
      
]