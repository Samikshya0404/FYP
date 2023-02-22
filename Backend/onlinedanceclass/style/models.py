from django.db import models

# Create your models here.


class Style(models.Model):
    name = models.CharField(max_length=100, primary_key=True)
    thumbnail = models.ImageField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)