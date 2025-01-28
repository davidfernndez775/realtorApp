from django.urls import path
from .views import RealEstatePropertyListView

app_name = 'realstateproperties'

urlpatterns = [
    path(
        'list/',
        RealEstatePropertyListView.as_view(),
        name='real-estate',
    ),
]
