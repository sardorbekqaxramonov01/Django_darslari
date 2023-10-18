from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class CustomUser(AbstractUser):
    name = models.TextField(max_length=50)
    age = models.PositiveIntegerField(null=True,blank=True)
    address = models.CharField(max_length=200)