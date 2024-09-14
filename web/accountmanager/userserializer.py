from rest_framework import serializers
from .models import UserManager as CustomUser

class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = CustomUser
        fields = ["username", "phone",'email',   'password']

    def create(self, validated_data):
        user = CustomUser.objects.create_user( 
            phone=validated_data['phone'],
            email=validated_data['email'],
            password=validated_data['password'],
            username=validated_data['username'],
           
            
        )
        return user
