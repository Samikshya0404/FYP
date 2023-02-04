from django.db import models


# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length=100)
    decription = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    thumbnail = models.ImageField()
    content = models.TextField()
    