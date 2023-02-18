from django.urls import path
from user.views import UserListView, UserDetailView, RegistrationAPIView

urlpatterns = [
    path('users/', UserListView.as_view()),
    path('users/<int:pk>/', UserDetailView.as_view()),
    path('api/register/', RegistrationAPIView.as_view(), name='register'),
]
