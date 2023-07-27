from django.views.generic import ListView
from .models import post

class HomePageView(ListView):
    model = post
    template_name = 'home.html'
    context_object_name = "Barcha_postlar"

class AboutPageView(ListView):
    model = post
    template_name = 'about.html'
    context_object_name = "Barcha_postlar"