from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from .models import *

GENDER_CHOICES = (
    ("Male", "Male"),
    ("Female", "Female"),
    ("Others", "Others"),
)

class UserForm(UserCreationForm):
    first_name = forms.CharField(max_length=250)
    last_name = forms.CharField(max_length=250)
    email = forms.EmailField()
    gender = forms.ChoiceField(choices=GENDER_CHOICES)  
    contact_number = forms.CharField(max_length=10)
    profile_photo = forms.ImageField(required=False)

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['username']
    
    @transaction.atomic
    def save(self):
        user = super().save(commit=False)

        user.is_normal_user = True
        user.save()
        registered = Users.objects.create(user=user)
        registered.first_name = self.cleaned_data.get('first_name')
        registered.last_name = self.cleaned_data.get('last_name')
        registered.email = self.cleaned_data.get('email')
        registered.gender = self.cleaned_data.get('gender')
        registered.contact_number = self.cleaned_data.get('contact_number')
        registered.profile_photo = self.cleaned_data.get('profile_photo')
        registered.save()

        return registered



