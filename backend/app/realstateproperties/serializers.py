'''
Serializers for real estate properties API
'''

from rest_framework import serializers
from core.models import RealEstateProperty, PropertyImage


class RealEstatePropertiesListSerializer(serializers.ModelSerializer):
    '''Serializer for list of properties'''

    class Meta:
        model = RealEstateProperty
        fields = ['id', 'title', 'county', 'property_type', 'for_rent_or_sale',
                  'price', 'square_ft', 'beds']
        read_only_fields = ['id']

class PropertyImageSerializer(serializers.ModelSerializer):
    '''Serializer for property images'''

    class Meta:
        model = PropertyImage
        fields = ['id', 'property', 'image', 'uploaded_at']
        read_only_fields = ['id', 'uploaded_at']

class RealEstatePropertiesDetailtSerializer(serializers.ModelSerializer):
    '''Serializer for property detail including images'''
    images = PropertyImageSerializer(many=True, read_only=True)

    class Meta:
        model = RealEstateProperty
        fields = ['id', 'title', 'county', 'address', 'zip_code', 'property_type', 'for_rent_or_sale', 'price', 'square_ft', 'beds', 'full_baths', 'half_baths', 'built', 'water_front', 'description', 'images']
        read_only_fields = ['id']

