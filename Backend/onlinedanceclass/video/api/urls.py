from django.urls import path


from video.api.views import VideoRetrieveAPI
# from video

urlpatterns = [
    path('video_details/<int:pk>', VideoRetrieveAPI.as_view(), name="video_details")
]