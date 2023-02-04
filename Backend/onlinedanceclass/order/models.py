from django.db import models
from django.db import models
from django.contrib.auth.models import User
from video.models import Video
from payment.models import Payment

# Create your models here.

class Order(models.Model):
    video_id = models.ForeignKey(Video, on_delete=models.CASCADE)
    payemnt_id = models.ForeignKey(Payment, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    amount = models.PositiveIntegerField()