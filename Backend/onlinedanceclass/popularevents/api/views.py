from django.views import generic
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import generics
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.throttling import UserRateThrottle
from django.views.decorators.csrf import csrf_exempt
from .serializers import PopularEventSerializer
from popularevents.models import PopularEvent


class EventList(generics.GenericAPIView):
    throttle_classes = [UserRateThrottle]
    permission_classes = [AllowAny]
  
    def get(self, request, format=None):
        events = PopularEvent.objects.all()
        serializer = PopularEventSerializer(events, many=True)
        return Response( { "data" :serializer.data})
