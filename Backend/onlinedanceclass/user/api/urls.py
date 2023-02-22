from django.urls import path
from user.api.views import UserRegistrationAPIView, MyObtainTokenPairView

urlpatterns = [
    path('register/', UserRegistrationAPIView.as_view()),
    path('login/', MyObtainTokenPairView.as_view()),

]
