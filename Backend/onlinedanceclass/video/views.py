from rest_framework import viewsets
from video.models import Video
from video.serializers import VideoSerializer


class VideoViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing accounts.
    """
    queryset = Video.objects.all()
    serializer_class = VideoSerializer