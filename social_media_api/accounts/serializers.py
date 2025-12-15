from .models import CustomUser
from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'password']

    def create(self, validated_data):
        user = CustomUser.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        return user

class CustomUserSerializer(serializers.ModelSerializer):
    
    password = serializers.CharField()
    
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'bio', 'profile_picture']

    
    def create(self, validated_data):
        user = get_user_model().objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'], 
            bio=validated_data['bio'], 
            profile_picture=validated_data['profile_picture'], **validated_data)
        
    
        Token.objects.create(user=user)
        return user
    
    
class LoginUserSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        user = get_user_model().objects.filter(username=data['username']).first()
        if user is None:
            raise serializers.ValidationError('User does not exist')
        if not user.check_password(data['password']):
            raise serializers.ValidationError('Incorrect password')
        return user
