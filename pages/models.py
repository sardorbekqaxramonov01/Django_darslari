from django.db import models

class post(models.Model):
    email = models.EmailField()
    text = models.TextField()
    def __str__(self):
        return self.text[:50]

