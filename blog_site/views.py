from django.shortcuts import render
from .models import Post
from django.views.generic import ListView

class BlogListViews(ListView):
    model= Post
    template_name = "home.html"
