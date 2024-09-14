from django.shortcuts import render

from rest_framework import viewsets
from rest_framework.response import Response
from .models import ProjectModel, CompositModel, LayerModel
from rest_framework import serializers
from django_filters import rest_framework as filters,CharFilter
from rest_framework.parsers import MultiPartParser, FormParser
from django.forms.models import model_to_dict
from drf_yasg.utils import swagger_auto_schema
from rest_framework.permissions import IsAuthenticated
from drf_yasg import openapi  
# Create your views here.



def home(request):
    return render(request, "index.html")
class ProjectSerializer(serializers.ModelSerializer): 
    class Meta:
        model = ProjectModel
        fields =  "__all__"
       
       



class ProjectFilter(filters.FilterSet): 
    class Meta:
        model = ProjectModel
        fields = "__all__"
class ProjectViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing user instances.
    """
    serializer_class = ProjectSerializer
    queryset = ProjectModel.objects.all()
    filterset_class  = ProjectFilter





# Composestion start

class CompositSerializer(serializers.ModelSerializer): 
    class Meta:
        model = CompositModel
        fields =  "__all__"
        




class CompositFilter(filters.FilterSet): 
    class Meta:
        model = CompositModel
        fields = "__all__"



class CompositViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing user instances.
    """
    serializer_class = CompositSerializer
    queryset = CompositModel.objects.all()
    filterset_class  = CompositFilter



class LayerSerializer(serializers.ModelSerializer): 
    class Meta:
        model = LayerModel
        fields =  "__all__"
       




class LayerFilter(filters.FilterSet): 
    class Meta:
        model = LayerModel
        fields = ['name',"compositid" ] 
        

class LayerViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing user instances.
    """
    serializer_class = LayerSerializer
    queryset = LayerModel.objects.all()
    filterset_class  = LayerFilter
    parser_classes = (MultiPartParser, FormParser)


class LayerModelSerializer(serializers.ModelSerializer): 

    class Meta:
        model = LayerModel
        fields =  '__all__'
        # Adjust depth as needed
        depth = 2
 
 

class DeepLayerViewSet(viewsets.ViewSet): 
    # permission_classes = [IsAuthenticated]  # Ensure the user is authenticated
    
    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter('project_id', openapi.IN_QUERY, description="Filter by project ID", type=openapi.TYPE_INTEGER, required=False, explode=True),
             
        ]
    )
    def list(self, request): 
        user = request.user 
        pid = request.query_params.get('project_id') 
        project = ProjectModel.objects.filter(id=pid).first()
        if not project:
            return Response([])
        data =  model_to_dict(project)
        data["user"] = user.username
        data['data']= []
        for l in project.project_composit.all(): 
            composit = model_to_dict(l)
            composit["layers"] = list(l.project_composit_layer.all().values())
            data['data'].append(composit)

        return Response(data)
    
