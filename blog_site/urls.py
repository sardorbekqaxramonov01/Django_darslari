from django.urls import path
from .views import BlogListView,BlogCreateView,BlogContactView

urlpatterns = [
    path("",BlogListView.as_view(), name="home"),
    path("post/new/",BlogCreateView.as_view(),name="about"),
    path("post/<int:pk>/", BlogContactView.as_view(),name="contact")
]
