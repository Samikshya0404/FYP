from django.db import models


# Create your models here.

class Blog(models.Model):
    blog_name = models.CharField(max_length=100)
    blog_dec = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)