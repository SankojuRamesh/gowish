from django.shortcuts import render

from rest_framework import viewsets, generics, serializers, views
from .models import UserTemplatesModel, UserTemplatesComposModel, UserTemplatesLayerModel, CartModel, WishListModel

from .serializers import  (UserTemplateSerializer,
                            UserTemplateCompositSerializer,
                              UserTemplatesLayerSerializer, 
                              UserWishlistSerializer, UserCartSerializer)



class UserTemplatesViewSet(viewsets.ModelViewSet):
    queryset = UserTemplatesModel
    serializer_class = UserTemplateSerializer


class UserTemplatesCompositViewSet(viewsets.ModelViewSet):
    queryset = UserTemplatesComposModel
    serializer_class = UserTemplateCompositSerializer



class UserTemplatesLayerViewSet(viewsets.ModelViewSet):
    queryset = UserTemplatesLayerModel
    serializer_class = UserTemplatesLayerSerializer


class CartViewSet(viewsets.ModelViewSet):
    queryset = CartModel
    serializer_class = UserCartSerializer

class WishListViewSet(viewsets.ModelViewSet):
    queryset = WishListModel
    serializer_class = UserWishlistSerializer
