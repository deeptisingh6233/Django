from django.shortcuts import render
from django.views.generic import ListView,DetailView,CreateView,UpdateView
from .models import Post

# Create your views here.
class PostListviews( ListView):
       model=Post
       template_name='blog/post_details.html'
       context_object_name='post'



class postDetailsView(DetailView):
      
      model=Post
      template_name='blog/post_form.html'
      context_obj_name="post"


class PostUpdateView(CreateView):
       model=Post
       template_name='blog/post_form.html'
       fields=['title' , 'content']


class PostDeleteView
      model=Post
      template_name='blog/post_confirm_delete.html'
      success_url=reverse_lazy('post_list')