from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from api.serializer import ManufacturerSerializer, ShoeTypeSerializer, ShoeColorSerializer, ShoeSerializer
from shoe.models import Manufacturer, ShoeType, ShoeColor, Shoe

# Create your views here.
class ManufacturerViewSet(ModelViewSet):
    serializer_class = ManufacturerSerializer
    basename = 'manufacturer'
    queryset = Manufacturer.objects.all()
    
class ShoeTypeViewSet(ModelViewSet):
    serializer_class = ShoeTypeSerializer
    basename = 'type'
    queryset = ShoeType.objects.all()
    
class ShoeColorViewSet(ModelViewSet):
    serializer_class = ShoeColorSerializer
    basename = 'color'
    queryset = ShoeColor.objects.all()
    
    
class ShoeViewSet(ModelViewSet):
    serializer_class = ShoeSerializer
    basename = 'shoe'
    queryset = Shoe.objects.all()
    
    
#Joe had a pet monkey named momo growing up on the African Savanna