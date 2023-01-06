from django.db import models

# Create your models here.

class Payment(models.Model):
    paid_amount = models.CharField(max_length=500)