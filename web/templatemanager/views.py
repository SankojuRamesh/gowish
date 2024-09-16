from django.shortcuts import render
from rest_framework import viewsets, generics, serializers,views
from .models import TemplateModel, CompositModel, LayerModel
from .serializers import TemplateSerializer, CompositSerializer, LayerSerializer
from rest_framework.permissions import IsAuthenticated



class TempalteViewSet(viewsets.ModelViewSet):
    queryset = TemplateModel.objects.all()
    serializer_class = TemplateSerializer
    permission_classes = [IsAuthenticated]



class CompositViewSet(viewsets.ModelViewSet):
    queryset = CompositModel.objects.all()
    serializer_class = CompositSerializer
    permission_classes = [IsAuthenticated]


class LayarViewSet(viewsets.ModelViewSet):
    queryset = LayerModel.objects.all()
    serializer_class = LayerSerializer
    permission_classes = [IsAuthenticated]




# Create your views here.
