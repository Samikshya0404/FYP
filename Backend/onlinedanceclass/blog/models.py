from django.db import models

# Create your models here.

class Blog(models.Model):
    blog_name = models.CharField(max_length=100)
    blog_dec = models.CharField(max_length=100)
    event_date = models.CharField(max_length=100)