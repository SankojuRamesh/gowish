

from rest_framework import serializers
from .models import CategoryModel, SubcategoryModel

class CatSerializer(serializers.ModelSerializer):

    class Meta:
        model = CategoryModel
        fields = "__all__"



class SubCatSerializer(serializers.ModelSerializer):

    class Meta:
        model = SubcategoryModel
        fields = ["id", "category", 'subcategory_name', 'price',"subcategory_state"]