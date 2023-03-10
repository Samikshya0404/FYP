from django.db import models
from user.models import CustomUser
from style.models import Style
# Create your models here.

# class Style(models.Model):
#     name = models.CharField(max_length=100, primary_key=True)
#     thumbnail = models.ImageField()
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)


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
    video_file = models.FileField(upload_to='videos/', null=True)
    style = models.ForeignKey(Style, on_delete=models.CASCADE , related_name="video_style" )
    level = models.IntegerField(choices=LEVEL, default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    creator = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

class Comment(models.Model):
    content = models.TextField()
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    video = models.ForeignKey(Video, on_delete=models.CASCADE)

    