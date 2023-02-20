from django.db import models

# Create your models here.


class PopularEvent(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    event_date = models.DateTimeField()
    venue = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)