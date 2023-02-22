from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import  BaseUserManager
from django.core.validators import ValidationError


# Create your models here.
class CustomAccountManager(BaseUserManager):
    def create_user(self, email, username,password, **extra_fields):

        # Validating email
        if not email:
            raise ValueError(_('You must provide an email address'))
        
        
        user = self.model(email=email, username=username, **extra_fields)
        user.set_password(password)
        user.save()
        return user


    def create_superuser(self, email, username,  password, **other_fields):
        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)

        if other_fields.get('is_staff') is not True:
            raise ValueError(
                'Superuser must be assigned to is_staff = True.'
            )

        if other_fields.get('is_superuser') is not True:
            raise ValueError(
                'Superuser must be assigned to is_superuser = True.'
            )

        return self.create_user(email, username, password, **other_fields)

GENDER_CHOICES = (
    ("Male", "Male"),
    ("Female", "Female"),
    ("Others", "Others"),
)

class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    username = models.CharField(max_length=30, unique=True)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)  
    password = models.CharField(max_length=30)
    contact_number = models.CharField(max_length=10, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    is_staff = models.BooleanField(default = False)
    is_active = models.BooleanField(default = True) # set to false on creation of account as we are assuming there will be some secondary check.
                                                     # example: email will be sent to user and only on click will be activated.
    objects = CustomAccountManager()

    def __str__(self):
        return self.username
