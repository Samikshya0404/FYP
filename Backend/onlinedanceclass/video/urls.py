from django.urls import path, include
from .views import VideoListView, VideoDetailView, StyleListView, StyleDetailView, CommentListView, CommentDetailView

urlpatterns = [
    path('api/videos/', VideoListView.as_view(), name='video-list'),
    path('api/videos/<int:pk>/', VideoDetailView.as_view(), name='video-detail'),
    path('api/styles/', StyleListView.as_view(), name='style-list'),
    path('api/styles/<int:pk>/', StyleDetailView.as_view(), name='style-detail'),
    path('api/comments/', CommentListView.as_view(), name='comment-list'),
    path('api/comments/<int:pk>/', CommentDetailView.as_view(), name='comment-detail'),
]
