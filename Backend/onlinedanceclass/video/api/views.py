from django.views import generic
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import generics
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.throttling import UserRateThrottle
from django.views.decorators.csrf import csrf_exempt
from .serializers import StyleSerializer
from video.models import Style , Video
from video.api.serializers import VideoSerializer

class StyleListAPI(generics.GenericAPIView):
    throttle_classes = [UserRateThrottle]
    permission_classes = [AllowAny]

    def get(self, request, format=None):
        styles = Style.objects.all()
        serializer = StyleSerializer(styles, many=True)
        return Response( {"data": serializer.data})

    
class StyleListAPI(generics.RetrieveAPIView):
    throttle_classes = [UserRateThrottle]
    permission_classes = [AllowAny]

    # def get(self, request, format=None):
    #     styles = Style.objects.all()
    #     serializer = StyleSerializer(styles, many=True)
    #     return Response( {"data": serializer.data})

    
class VideoRetrieveAPI(generics.RetrieveAPIView):
    throttle_classes = [UserRateThrottle]
    permission_classes = [AllowAny]

    models = Video
    queryset = Video.objects.all()
    serializer_class = VideoSerializer
    