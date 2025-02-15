'''
Views for the realstateproperties API
'''

from django_filters.rest_framework import DjangoFilterBackend

from rest_framework import generics

from core.models import RealEstateProperty
from .serializers import RealEstatePropertiesListSerializer
from .filters import RealEstatePropertyFilter


class RealEstatePropertyListView(generics.ListAPIView):
    '''Return a list of properties, also filtered according to a search'''
    serializer_class = RealEstatePropertiesListSerializer
    queryset = RealEstateProperty.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_class = RealEstatePropertyFilter


class RealEstatePropertyDetailView(generics.RetrieveAPIView):
    '''Return a detail page of a property'''
    serializer_class=RealEstatePropertiesListSerializer
    queryset = RealEstateProperty.objects.all()






