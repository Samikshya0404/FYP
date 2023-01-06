from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Style(models.Model):
    name = models.CharField(max_length=100, primary_key=True)


LEVEL = (
    (1, "Beginner"),
    (2, "Intermediate"),
    (3, "Advanced"),
)


class Video(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    price = models.PositiveIntegerField()
    thumbnail = models.ImageField()
    preview_url = models.TextField()
    url = models.TextField()
    style = models.ForeignKey(Style, on_delete=models.CASCADE)
    level = models.IntegerField(choices=LEVEL, default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)



class Comment(models.Model):
    content = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    video = models.ForeignKey(Video, on_delete=models.CASCADE)