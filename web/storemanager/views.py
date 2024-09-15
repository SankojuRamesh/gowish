from django.shortcuts import render
from rest_framework import generics, viewsets
from .models import StoreModel
from .serializers import StoreSerializer

# Create your views here.


class StoresViewSet(viewsets.ModelViewSet):
    queryset = StoreModel.objects.all()
    serializer_class = StoreSerializer

    

