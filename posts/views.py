from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, ListView, DeleteView, DetailView
from .models import Post 
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

class PostList(ListView):
    paginate_by = 10
    model = Post 

class CreatePost(LoginRequiredMixin, CreateView):
    login_url = '/login/'
    fields = "__all__"
    model = Post 

class EditPost(LoginRequiredMixin, UpdateView):
    login_url = '/login/'
    fields = "__all__" 
    model = Post 

class RemovePost(LoginRequiredMixin, DeleteView):
    login_url = '/login/'
    model = Post 
    success_url = reverse_lazy('posts:post-list') 

class ViewPost(DetailView):
    model = Post 

    
    

def tagged_posts(request, tag):
    post_list = Post.objects.filter(tags__name__in=[tag])
    return render(request, 'posts/post_list.html', context={'post_list': post_list})

