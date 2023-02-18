from rest_framework import generics, permissions
from user.models import CustomUser
from video.models import Video, Style, Comment
from video.serializers import VideoSerializer, StyleSerializer, CommentSerializer

# class VideoList(generics.ListCreateAPIView):
#     queryset = Video.objects.all()
#     serializer_class = VideoSerializer 
#     permission_classes = [permissions.IsAuthenticated]

# class VideoDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Video.objects.all()
#     serializer_class = VideoSerializer
#     permission_classes = [permissions.IsAuthenticated]

from rest_framework.decorators import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from django.contrib.auth import authenticate
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication



class VideoListView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    
    queryset = Video.objects.all()
    serializer_class = VideoSerializer

    def get(self, request, format=None):
        video = Video.objects.filter(user=request.user.id)
        serializer = VideoSerializer(video, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = VideoSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 

class VideoDetailView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get_object(self, pk):
        try:
            return Video.objects.get(pk=pk)
        except Video.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        video = self.get_object(pk)
        serializer = VideoSerializer(video)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        video = self.get_object(pk)
        serializer = VideoSerializer(video, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def patch(self, request, pk):  
        video = Video.objects.get(id=pk)

        serializer = VideoSerializer(video, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        video = self.get_object(pk)
        video.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

# class StyleList(generics.ListCreateAPIView):
#     queryset = Style.objects.all()
#     serializer_class = StyleSerializer
#     permission_classes = [permissions.IsAuthenticated]

# class StyleDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Style.objects.all()
#     serializer_class = StyleSerializer
#     permission_classes = [permissions.IsAuthenticated]

class StyleListView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    
    queryset = Style.objects.all()
    serializer_class = StyleSerializer

    def get(self, request, format=None):
        style = Style.objects.filter(user=request.user.id)
        serializer = StyleSerializer(style, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = StyleSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 

class StyleDetailView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get_object(self, pk):
        try:
            return Style.objects.get(pk=pk)
        except Style.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        style = self.get_object(pk)
        serializer = StyleSerializer(style)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        style = self.get_object(pk)
        serializer = StyleSerializer(style, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def patch(self, request, pk):  
        style = Style.objects.get(id=pk)

        serializer = StyleSerializer(style, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        style = self.get_object(pk)
        style.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class CommentListView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def get(self, request, format=None):
        comment = Style.objects.filter(user=request.user.id)
        serializer = CommentSerializer(comment, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = CommentSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
    
class CommentDetailView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get_object(self, pk):
        try:
            return Comment.objects.get(pk=pk)
        except Comment.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        comment = self.get_object(pk)
        serializer = CommentSerializer(comment)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        comment = self.get_object(pk)
        serializer = CommentSerializer(comment, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def patch(self, request, pk):  
        comment = Comment.objects.get(id=pk)

        serializer = CommentSerializer(comment, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        comment = self.get_object(pk)
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
