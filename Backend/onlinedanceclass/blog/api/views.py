from django.views import generic
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import generics
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.throttling import UserRateThrottle
from django.views.decorators.csrf import csrf_exempt
from .serializers import BlogSerializer
from blog.models import Blog



class BlogListApi(generics.GenericAPIView):
    throttle_classes = [UserRateThrottle]
    permission_classes = [AllowAny]


    def get(self, request):
        blogs = Blog.objects.all()
        serializer = BlogSerializer(blogs, many=True)
        return Response( {"data" :serializer.data})


class BlogDetailView(generics.GenericAPIView):
    throttle_classes = [UserRateThrottle]
    permission_classes = [AllowAny]

    def get(self,request , pk):
        blog = Blog.objects.get(pk=pk)
        serializer = BlogSerializer(blog)
        return Response({ "data": serializer.data})

