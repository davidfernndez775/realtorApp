'''
Views for the realstateproperties API
'''
from rest_framework import generics
from drf_spectacular.utils import extend_schema_view, extend_schema, OpenApiParameter, OpenApiTypes
from django_filters.rest_framework import DjangoFilterBackend
from .serializers import RealEstatePropertiesListSerializer
from core.models import RealEstateProperty
from .filters import RealEstatePropertyFilter


class RealEstatePropertyListView(generics.ListAPIView):
    '''Return a list of properties, also filtered according to a search'''
    serializer_class = RealEstatePropertiesListSerializer
    queryset = RealEstateProperty.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_class = RealEstatePropertyFilter


class RealEstatePropertyDetailView(generics.RetrieveAPIView):
    '''Return a detail page of a property'''

