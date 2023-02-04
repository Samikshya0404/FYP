from rest_framework.serializers import ModelSerializer
from video.models import Video, Style, Comment

class VideoSerializer(ModelSerializer):
    class Meta:
        model = Video
        fields = "__all__"

class StytleSerializer(ModelSerializer):
    class Meta:
        model = Style
        fields = "__all__"

class CommnetSerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = "__all__"
