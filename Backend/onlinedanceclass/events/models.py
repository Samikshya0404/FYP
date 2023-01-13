from django.db import models

# Create your models here.

class Event(models.Model):
    event_name = models.CharField(max_length=100)
    event_dec = models.TextField()
    event_date = models.DateTimeField()
    event_address = models.CharField(max_length=100)