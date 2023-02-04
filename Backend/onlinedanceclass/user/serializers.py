from rest_framework.serializers import ModelSerializer
from video.models import Registered

class VideoSerializer(ModelSerializer):
    class Meta:
        model = Video
        fields = "__all__"