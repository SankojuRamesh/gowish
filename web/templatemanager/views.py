from django.shortcuts import render
from rest_framework import viewsets, generics, serializers,views
from .models import TemplateModel, CompositModel, LayerModel
from .serializers import TemplateSerializer, CompositSerializer, LayerSerializer



class TempalteViewSet(viewsets.ModelViewSet):
    queryset = TemplateModel.objects.all()
    serializer_class = TemplateSerializer



class CompositViewSet(viewsets.ModelViewSet):
    queryset = CompositModel.objects.all()
    serializer_class = CompositSerializer


class LayarViewSet(viewsets.ModelViewSet):
    queryset = LayerModel.objects.all()
    serializer_class = LayerSerializer




# Create your views here.
