
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth import get_user_model
from rest_framework import generics,serializers
from rest_framework_simplejwt import serializers as jwt_serializers
from rest_framework.permissions import AllowAny 
from rest_framework import generics, parsers, permissions, status
from .userserializer import UserRegistrationSerializer
from rest_framework_simplejwt import views as jwt_views
from .models import RolesModel

User = get_user_model()

class UserRegistrationView(generics.CreateAPIView):
    serializer_class = UserRegistrationSerializer
    permission_classes = [AllowAny]


class UserRoleSerializer(serializers.ModelSerializer):
    """
    Serializer to view all Users """
    class Meta:
        model = RolesModel
        fields = "__all__"
class UserSerializer(serializers.ModelSerializer):
 

     

    class Meta:
        model = User
        fields = ('id', 'name', 'email', 'address', 'contact', 'roles', 'is_active')
        read_only_fields = ('email', 'is_active')

class SignInSerializer(jwt_serializers.TokenObtainPairSerializer):
    """
    Return Access, Refresh tokens along with User data
    """

    def validate(self, attrs):
        data = super().validate(attrs)
        user = UserSerializer(self.user, context=self.context).data
        data.update(user)
        return data



class CreateUserSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(
        write_only=True, required=True, min_length=5, max_length=24
    )
    roles = UserRoleSerializer(source='s', read_only=True)

    class Meta:
        model = User
        fields = (
            'id',
            'email',
            'password',
            'confirm_password',
            'name',
            'address',
            'contact',
            
            'roles',
            
        )
        extra_kwargs = {
            'password': {'write_only': True, 'min_length': 5, 'max_length': 24},
            'roles': {'write_only': True, 'required': True},
        }

    def validate(self, data):
        password = data.get('password')
        confirm_password = data.get('confirm_password')
        if password != confirm_password:
            raise serializers.ValidationError({'password': _("Passwords not matching!")})
        return data

    def create(self, validated_data):
        validated_data.pop('confirm_password')
        return User.objects.create_user(**validated_data)

class SignInView(jwt_views.TokenObtainPairView):
    """
    SignIn Endpoint using email & password
    Response: access & refresh tokens
    """

    serializer_class = SignInSerializer

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context.update({"request": self.request})
        return context

class CreateUserView(generics.CreateAPIView):
    """
    Create User API
    Only Admins can access this API
    """
    serializer_class = CreateUserSerializer
    parser_classes = [parsers.MultiPartParser, parsers.FormParser]
    permission_classes = [permissions.IsAuthenticated ]