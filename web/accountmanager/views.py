
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth import get_user_model
from rest_framework import generics,serializers
from rest_framework_simplejwt import serializers as jwt_serializers
from rest_framework.permissions import AllowAny, IsAuthenticated

 
from .userserializer import UserRegistrationSerializer, EmployeeRegistrationSerializer
from rest_framework_simplejwt import views as jwt_views

User = get_user_model()

class UserRegistrationView(generics.CreateAPIView):
    serializer_class = UserRegistrationSerializer
    permission_classes = [AllowAny]


class EmployeeRegistrationView(generics.CreateAPIView):
    serializer_class = EmployeeRegistrationSerializer
    permission_classes = [IsAuthenticated]


class UserSerializer(serializers.ModelSerializer):
    """
    Serializer to view all Users """
     

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


class EmployeeListView(generics.ListAPIView):
    queryset = User.objects.filter(roles=2)
    serializer_class= UserSerializer
    permission_classes = IsAuthenticated

    

