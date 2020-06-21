from rest_framework.serializers import ModelSerializer, HyperlinkedModelSerializer
from shoe.models import Manufacturer, ShoeType, ShoeColor, Shoe

class ManufacturerSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Manufacturer
        fields = ('name', 'website',)

class ShoeTypeSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = ShoeType
        fields = ('style',)


class ShoeColorSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = ShoeColor
        fields = ('color_name',)

class ShoeSerializer(ModelSerializer):
    class Meta:
        model = Shoe
        fields = ('size', 'brand', 'manufacturer', 'color', 'material', 'shoe_type', 'fasten_type',)
