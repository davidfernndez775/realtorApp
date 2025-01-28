'''
Views for the realstateproperties API
'''
from rest_framework import generics
from drf_spectacular.utils import extend_schema_view, extend_schema, OpenApiParameter, OpenApiTypes
from .serializers import RealEstatePropertiesListSerializer
from core.models import RealEstateProperty

# this is only for drf-spectacular


@extend_schema_view(
    list=extend_schema(
        # define the parameters to filter by
        parameters=[
            OpenApiParameter(
                'county',
                OpenApiTypes.STR,
                description='Comma separated list of counties IDs to filter',
            ),
        ]
    )
)
class RealEstatePropertyListView(generics.ListAPIView):
    '''Return a list of properties, also filtered according to a search'''
    serializer_class = RealEstatePropertiesListSerializer
    queryset = RealEstateProperty.objects.all()

    # # to separate the queryparams in ints
    # def _params_to_ints(self, qs):
    #     '''Convert a list of strings to integers'''
    #     return [int(str_id) for str_id in qs.split(',')]

    # def get_queryset(self):
    #     '''Retrieve filtered properties'''
    #     # get the params from the request
    #     property_type = self.request.query_params.get('property_type')
    #     price = self.request.query_params.get('price')
    #     for_rent_or_sale = self.request.query_params.get('for_rent_or_sale')
    #     county = self.request.query_params.get('county')
    #     beds = self.request.query_params.get('beds')
    #     full_baths = self.request.query_params.get('full_baths')
    #     half_baths = self.request.query_params.get('half_baths')
    #     water_front = self.request.query_params.get('water_front')
    #     built = self.request.query_params.get('built')

    #     # redefine the queryset
    #     queryset = self.queryset

    #     # check for query_params in request
    #     if county:
    #         county_ids = self._params_to_ints(county)
    #         queryset = queryset.filter(county__id__in=county_ids)

    #     # return queryset.order_by('-id').distinct()
    #     return queryset


class RealEstatePropertyDetailView(generics.RetrieveAPIView):
    '''Return a detail page of a property'''
