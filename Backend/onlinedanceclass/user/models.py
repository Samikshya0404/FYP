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
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    





    






