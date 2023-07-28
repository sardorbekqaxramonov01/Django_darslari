from django.shortcuts import render
from .models import Post
from django.views.generic import ListView
from django.views.generic import CreateView

class BlogListView(ListView):
    model= Post
    template_name = "home.html"

class BlogContactView(ListView):
    model= Post
    template_name = "contact.html"

class BlogCreateView(CreateView):
    model= Post
    template_name = "about.html"
    fields = ['title','author','body']
