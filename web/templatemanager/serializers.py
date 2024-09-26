from rest_framework import serializers
from .models import TemplateModel, CompositModel, LayerModel





class TemplateSerializer(serializers.ModelSerializer):
    category_name = serializers.SerializerMethodField()
    

    class Meta:
        model = TemplateModel
        fields = '__all__'
    
    def get_category(self, obj):
        print(obj.category)
        return obj.category.name



class CompositSerializer(serializers.ModelSerializer): 
    class Meta:
        model = CompositModel
        fields = '__all__'


class LayerSerializer(serializers.ModelSerializer): 
    class Meta:
        model = LayerModel
        fields = '__all__'