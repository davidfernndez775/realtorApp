'''
URLs for real state property endpoints
'''

from django.urls import path

from .views import RealEstatePropertyListView, RealEstatePropertyDetailView, PropertyImageListView

app_name = 'realstateproperties'

urlpatterns = [
    path(
        'list/',
        RealEstatePropertyListView.as_view(),
        name='real-estate',
    ),
    path('property/<int:pk>', RealEstatePropertyDetailView.as_view(), name='real-state-property'),
    path('property-images/', PropertyImageListView.as_view(), name='property-images'),
]
