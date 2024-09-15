from rest_framework import serializers
from .models import StoreModel
from accountmanager.models import User as CustomUser



class StoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = StoreModel
        fields = [ "phone",'email','title']

    def create(self, validated_data):
        print(validated_data)
        print("________________________________")
        user = CustomUser.objects.create_employee( 
             
            phone=validated_data['phone'],
            email=validated_data['email'],
            password="admin@123",
            name=validated_data['title'] 
            
        )
        validated_data['user'] = user
        
        instance = StoreModel.objects.create(**validated_data)

        return instance