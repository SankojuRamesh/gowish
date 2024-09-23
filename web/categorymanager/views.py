from django.shortcuts import render
from rest_framework import generics,serializers, viewsets, parsers
from .models import CategoryModel, SubcategoryModel
from .serializer import CatSerializer, SubCatSerializer
from rest_framework.permissions import IsAuthenticated

from .filters import SubCategoryFilter, CategoryFilter

# Create your views here.



class CategoryView(viewsets.ModelViewSet):
    queryset = CategoryModel.objects.all()
    serializer_class = CatSerializer
    filterset_class  = CategoryFilter
    parser_classes = (parsers.FormParser,  parsers.MultiPartParser)
    permission_classes = [IsAuthenticated]




class SubCategoryView(viewsets.ModelViewSet):
    queryset = SubcategoryModel.objects.all()
    serializer_class = SubCatSerializer
    filterset_class  = SubCategoryFilter
    permission_classes = [IsAuthenticated]

