from django.db import models

# Create your models here.

class Payment(models.Model):
    paid_amount = models.PositiveIntegerField()
    order = models.TextField()
    ordered_by = models.CharField(max_length=100)