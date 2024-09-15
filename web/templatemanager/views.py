from django.shortcuts import render
from rest_framework import viewsets, generics, serializers,views
from .models import TemplateModel, CompositModel, LayerModel
from .serializers import TemplateSerializer, CompositSerializer, LayerSerializer



class TempalteViewSet(viewsets.ModelViewSet):
    queryset = TemplateModel
    serializer_class = TemplateSerializer



class CompositViewSet(viewsets.ModelViewSet):
    queryset = CompositModel
    serializer_class = CompositSerializer


class LayarViewSet(viewsets.ModelViewSet):
    queryset = LayerModel
    serializer_class = LayerSerializer




# Create your views here.
