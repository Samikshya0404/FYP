from rest_framework import serializers
from user.models import CustomUser

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = "__all__"


class RegistrationSerializer(serializers.ModelSerializer):

    email = serializers.EmailField(max_length=100, min_length=11)
    first_name = serializers.CharField(max_length=50, min_length=2)
    password = serializers.CharField(max_length=150, write_only=True)

    class Meta:
        model = CustomUser
        fields = ('id', 'first_name', 'last_name', 'email', 'password')

    def validate(self, args):
        email = args.get('email', None)
        if CustomUser.objects.filter(email=email).exists():
            raise serializers.ValidationError(
                {'email': ('email already exists')})

        return super().validate(args)

    def create(self, validated_data):
        return CustomUser.objects.create_user(**validated_data)