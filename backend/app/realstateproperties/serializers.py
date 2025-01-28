'''
Serializers for real estate properties API
'''

from rest_framework import serializers
from core.models import RealEstateProperty


class RealEstatePropertiesListSerializer(serializers.ModelSerializer):
    '''Serializer for list of properties'''

    class Meta:
        model = RealEstateProperty
        fields = ['id', 'county', 'property_type']
        read_only_fields = ['id']
