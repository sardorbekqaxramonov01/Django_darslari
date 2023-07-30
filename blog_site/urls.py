from django.urls import path
from .views import BlogListView,BlogCreateView,BlogDetailView,BlogupdateView,BlogDeleteView

urlpatterns = [
    path("post/<int:pk>/delete/", BlogDeleteView.as_view(),name="post_delete"),
    path("post/<int:pk>/edit", BlogupdateView.as_view(),name="post_edit"),
    path("",BlogListView.as_view(), name="home"),
    path("post/new/",BlogCreateView.as_view(),name="post_new"),
    path("post/<int:pk>/", BlogDetailView.as_view(),name="post_detail")
]
