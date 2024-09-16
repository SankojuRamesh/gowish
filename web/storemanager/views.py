from django.shortcuts import render
from rest_framework import generics, viewsets, views, serializers
from .models import StoreModel
from .serializers import StoreSerializer
from rest_framework.response import Response
from geopy.geocoders import Nominatim
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from rest_framework.permissions import IsAuthenticated
 
# Create your views here.
class getaddress_Serializer(serializers.Serializer):
    address = serializers.CharField()

     
class get_address(views.APIView):
    id_param = openapi.Parameter(
        'pincode', 
        openapi.IN_QUERY, 
        description="Filter books by ID", 
        type=openapi.TYPE_INTEGER
    )

    @swagger_auto_schema(manual_parameters=[id_param])
    def get(self, request):
        try:
            geolocator = Nominatim(user_agent="address_lookup")
            zipcode = request.query_params.get('pincode', None) 
            # Using geocode()
            location = geolocator.geocode(zipcode)
            # data = [{"address": location}]
            # adress_serializer = getaddress_Serializer(data, many=True)
        
            return  Response({ "address": location.address})
        except:
            return Response({ "address": None})

    



class StoresViewSet(viewsets.ModelViewSet):
    queryset = StoreModel.objects.all()
    serializer_class = StoreSerializer
    permission_classes = IsAuthenticated


    

