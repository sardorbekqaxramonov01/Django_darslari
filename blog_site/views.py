from .models import Post
from django.views.generic import ListView
from django.views.generic import CreateView , UpdateView, DeleteView
from django.urls import reverse_lazy

class BlogListView(ListView):
    model= Post
    template_name = "home.html"

class BlogDetailView(ListView):
    model= Post
    template_name = "post_detail.html"

class BlogCreateView(CreateView):
    model= Post
    template_name = "post_new.html"
    fields = ['title','author','body']

class BlogupdateView(UpdateView):
    model = Post
    template_name = 'post_edit.html'
    fields = ['title','body']

class BlogDeleteView(DeleteView):
    model = Post
    template_name = 'post_delete.html'
    fields = ['title','body']
    success_url = reverse_lazy('home')
