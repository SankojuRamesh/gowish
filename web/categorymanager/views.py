from django.shortcuts import render
from rest_framework import generics,serializers, viewsets
from .models import CategoryModel, SubcategoryModel
from .serializer import CatSerializer, SubCatSerializer

# Create your views here.



class CategoryView(viewsets.ModelViewSet):
    queryset = CategoryModel
    serializer_class = CatSerializer




class SubCategoryView(viewsets.ModelViewSet):
    queryset = SubcategoryModel
    serializer_class = SubCatSerializer

