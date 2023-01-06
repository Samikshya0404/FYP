from django.contrib.auth.models import User
from django.db import models

GENDER_CHOICES = (
    ("Male", "Male"),
    ("Female", "Female"),
    ("Others", "Others"),
)

class RegisteredUser(User):
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)   
    contact_number = models.CharField(max_length=10, unique=True)

class Styles(models.Model):
    style_name = models.CharField(max_length=100)

class Level(models.Model):
    levle_name = models.CharField(max_length=100)

class Video(models.Model):
    video_name = models.CharField(max_length=100)
    video_desc = models.CharField(max_length=100)
    video_price = models.CharField(max_length=500)

class Payment(models.Model):
    paid_amount = models.CharField(max_length=500)

class Events(models.Model):
    event_name = models.CharField(max_length=100)
    event_dec = models.CharField(max_length=100)
    event_date = models.CharField(max_length=100)
    event_address = models.CharField(max_length=100)

class Blog(models.Model):
    blog_name = models.CharField(max_length=100)
    blog_dec = models.CharField(max_length=100)
    event_date = models.CharField(max_length=100)
    






