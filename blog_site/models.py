from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(
        'auth.user',on_delete=models.CASCADE,
    )
    Body = models.TextField(max_length=255)
    def __str__(self):
        return self.title