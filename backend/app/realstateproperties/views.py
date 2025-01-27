'''
Views for the realstateproperties API
'''
from rest_framework import generics


class RealStatePropertyList(generics.ListAPIView):
    '''Return a list of properties, also filtered according to a search'''


class RealStatePropertyDetail(generics.RetrieveAPIView):
    '''Return a detail page of a property'''
