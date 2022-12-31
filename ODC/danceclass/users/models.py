from django.contrib.auth.models import User
from django.db import models

GENDER_CHOICES = (
    ("Male", "Male"),
    ("Female", "Female"),
    ("Others", "Others"),
)

    
class Users(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    email = models.EmailField(unique=True)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)    
    contact_number = models.CharField(max_length=10, unique=True)
    profile_photo = models.ImageField(null=True, blank=True)




    
    
