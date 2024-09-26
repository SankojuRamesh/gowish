from rest_framework import serializers
from .models import TemplateModel, CompositModel, LayerModel





class TemplateSerializer(serializers.ModelSerializer):
    

    class Meta:
        model = TemplateModel
        fields = '__all__'



class CompositSerializer(serializers.ModelSerializer): 
    class Meta:
        model = CompositModel
        fields = '__all__'


class LayerSerializer(serializers.ModelSerializer): 
    class Meta:
        model = LayerModel
        fields = '__all__'