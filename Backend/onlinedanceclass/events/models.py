from django.db import models

# Create your models here.

class Events(models.Model):
    event_name = models.CharField(max_length=100)
    event_dec = models.CharField(max_length=100)
    event_date = models.CharField(max_length=100)
    event_address = models.CharField(max_length=100)

