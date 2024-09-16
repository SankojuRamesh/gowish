from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated

from rest_framework import viewsets, generics, serializers, views
from .models import UserTemplatesModel, UserTemplatesComposModel, UserTemplatesLayerModel, CartModel, WishListModel

from .serializers import  (UserTemplateSerializer,
                            UserTemplateCompositSerializer,
                              UserTemplatesLayerSerializer, 
                              UserWishlistSerializer, UserCartSerializer)



class UserTemplatesViewSet(viewsets.ModelViewSet):
    queryset = UserTemplatesModel.objects.all()
    serializer_class = UserTemplateSerializer
    permission_classes = [IsAuthenticated]


class UserTemplatesCompositViewSet(viewsets.ModelViewSet):
    queryset = UserTemplatesComposModel.objects.all()
    serializer_class = UserTemplateCompositSerializer
    permission_classes = [IsAuthenticated]



class UserTemplatesLayerViewSet(viewsets.ModelViewSet):
    queryset = UserTemplatesLayerModel
    serializer_class = UserTemplatesLayerSerializer
    permission_classes = [IsAuthenticated]


class CartViewSet(viewsets.ModelViewSet):
    queryset = CartModel.objects.all()
    serializer_class = UserCartSerializer
    permission_classes = [IsAuthenticated]

class WishListViewSet(viewsets.ModelViewSet):
    queryset = WishListModel.objects.all()
    serializer_class = UserWishlistSerializer
    permission_classes = [IsAuthenticated]
