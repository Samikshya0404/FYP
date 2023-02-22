from user.models import CustomUser
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework.permissions import  AllowAny
from rest_framework import status

from .serializers import MyTokenObtainPairSerializer
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView
class UserRegistrationAPIView(CreateAPIView):
    permission_classes=[AllowAny]

    queryset = CustomUser.objects.all()

    def post(self, request, *args, **kwargs):
        email = request.data.get('email')
        first_name = request.data.get('first_name')
        last_name = request.data.get('last_name')
        username = request.data.get('username')
        gender = request.data.get('gender')
        password = request.data.get('password')
        contact_number = request.data.get('contact_number')

        try:
            user = CustomUser.objects.create(email=email, first_name=first_name, last_name=last_name, username=username, gender=gender,  contact_number=contact_number)
               
            user.set_password(password)

            user.save()

            return Response({'message': 'User created successfully'}, status=status.HTTP_201_CREATED)

        except:
            return Response( {'message': 'User already exists'}, status=status.HTTP_400_BAD_REQUEST)


class MyObtainTokenPairView(TokenObtainPairView):
    permission_classes = (AllowAny,)
    serializer_class = MyTokenObtainPairSerializer
