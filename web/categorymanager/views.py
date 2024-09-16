from django.shortcuts import render
from rest_framework import generics,serializers, viewsets, parsers
from .models import CategoryModel, SubcategoryModel
from .serializer import CatSerializer, SubCatSerializer
from rest_framework.permissions import IsAuthenticated

# Create your views here.



class CategoryView(viewsets.ModelViewSet):
    queryset = CategoryModel.objects.all()
    serializer_class = CatSerializer
    parser_classes = (parsers.FormParser,  parsers.MultiPartParser)
    permission_classes = [IsAuthenticated]




class SubCategoryView(viewsets.ModelViewSet):
    queryset = SubcategoryModel.objects.all()
    serializer_class = SubCatSerializer
    permission_classes = [IsAuthenticated]

