from django.db import models
from user.models import CustomUser
from video.models import Video
from payment.models import Payment

class Order(models.Model):
    video = models.ForeignKey(Video, on_delete=models.CASCADE, related_name='orders')
    payment = models.ForeignKey(Payment, on_delete=models.CASCADE, related_name='orders')
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='orders')
    created_at = models.DateTimeField(auto_now_add=True)
    amount = models.PositiveIntegerField()
