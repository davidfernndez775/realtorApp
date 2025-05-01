'''
Views for the realstateproperties API
'''

from django_filters.rest_framework import DjangoFilterBackend

from rest_framework import generics

from core.models import RealEstateProperty, PropertyImage
from .serializers import RealEstatePropertiesSerializer, PropertyImageSerializer
from .filters import RealEstatePropertyFilter


class RealEstatePropertyListView(generics.ListAPIView):
    '''Return a list of properties, also filtered according to a search'''
    serializer_class = RealEstatePropertiesSerializer
    queryset = RealEstateProperty.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_class = RealEstatePropertyFilter


class RealEstatePropertyDetailView(generics.RetrieveAPIView):
    '''Return a detail page of a property'''
    serializer_class = RealEstatePropertiesSerializer

    # redefine the queryset for retrieve only the property
    def get_queryset(self):
        return RealEstateProperty.objects.filter(pk=self.kwargs["pk"])


class PropertyImageListView(generics.ListAPIView):
    '''Vista para listar imágenes de propiedades'''
    serializer_class = PropertyImageSerializer
    queryset = PropertyImage.objects.all()  # Base queryset
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['property']
