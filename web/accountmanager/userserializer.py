from rest_framework import serializers
from .models import User as CustomUser


class EmployeeRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ["name", "phone",'email',   'password' ]

    def create(self, validated_data):
        user = CustomUser.objects.create_employee( 
            phone=validated_data['phone'],
            email=validated_data['email'],
            password=validated_data['password'],
            name=validated_data['name'], 
            
        )
        return user


class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)  
    class Meta:
        model = CustomUser
        fields = ["name", "phone",'email',   'password' ]

    def create(self, validated_data):
        user = CustomUser.objects.create_user( 
            phone=validated_data['phone'],
            email=validated_data['email'],
            password=validated_data['password'],
            name=validated_data['name'],   )
        return user
