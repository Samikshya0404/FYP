from rest_framework.serializers import ModelSerializer
from style.models import  Style
from video.api.serializers import VideoSerializer
class StyleSerializer(ModelSerializer):
    video_style = VideoSerializer(many=True)
    class Meta:
        model = Style
        fields = ("name", "thumbnail" , "video_style" )