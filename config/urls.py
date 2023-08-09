from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('accounts/',include('django.contrib.auth.urls')),
    # path('accounts/',include('accounts.urls')),
    # path('',include("blog_site.urls")),
    path('users/',include("users.urls")),
    path('users/',include('django.contrib.auth.urls')),
    path('',include("pages.urls")),
]
