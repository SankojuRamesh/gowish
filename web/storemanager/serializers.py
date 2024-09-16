from rest_framework import serializers
from .models import StoreModel
from accountmanager.models import User as CustomUser



class StoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = StoreModel
        fields = [ "phone",'email','title',"address"]

    def create(self, validated_data):
        user = CustomUser.objects.create_storeadmin(  
            phone=validated_data['phone'],
            email=validated_data['email'],
            password="admin@123",
            name=validated_data['title']  )
        validated_data['user'] = user
        
        instance = StoreModel.objects.create(**validated_data)

        return instance