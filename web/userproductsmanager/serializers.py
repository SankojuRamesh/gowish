from rest_framework  import serializers
from .models import UserTemplatesModel,  UserTemplatesComposModel, UserTemplatesLayerModel, UserCreditsModel, CartModel, WishListModel


class UserTemplateSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserTemplatesModel
        fields = '__all__'

class UserTemplateCompositSerializer(serializers.ModelSerializer): 
    class Meta:
        model = UserTemplatesComposModel
        fields = '__all__'

class UserTemplatesLayerSerializer(serializers.ModelSerializer): 
    class Meta:
        model = UserTemplatesLayerModel
        fields = '__all__'

class UserWishlistSerializer(serializers.ModelSerializer):
    class Meta:
            model = WishListModel
            fields = '__all__'


class UserCartSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartModel
        fields = '__all__'
