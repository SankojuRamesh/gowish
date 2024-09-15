from django.shortcuts import render
from rest_framework import generics,serializers, viewsets
from .models import CategoryModel, SubcategoryModel
from .serializer import CatSerializer, SubCatSerializer

# Create your views here.



class CategoryView(viewsets.ModelViewSet):
    queryset = CategoryModel.objects.all()
    serializer_class = CatSerializer




class SubCategoryView(viewsets.ModelViewSet):
    queryset = SubcategoryModel.objects.all()
    serializer_class = SubCatSerializer

