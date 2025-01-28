'''
Views for the realstateproperties API
'''
from rest_framework import generics
from drf_spectacular.utils import extend_schema_view, extend_schema, OpenApiParameter, OpenApiTypes
from django_filters.rest_framework import DjangoFilterBackend
from .serializers import RealEstatePropertiesListSerializer
from core.models import RealEstateProperty

# this is only for drf-spectacular


# @extend_schema_view(
#     list=extend_schema(
#         # define the parameters to filter by
#         parameters=[
#             OpenApiParameter(
#                 'county',
#                 OpenApiTypes.STR,
#                 description='Comma-separated list of county IDs to filter',
#             ), s
#             OpenApiParameter(
#                 'property_type',
#                 OpenApiTypes.STR,
#                 description='Type of property to filter (e.g., "house", "apartment")',
#             ),
#             OpenApiParameter(
#                 'price',
#                 OpenApiTypes.INT,
#                 description='Maximum price of the property to filter',
#             ),
#             OpenApiParameter(
#                 'for_rent_or_sale',
#                 OpenApiTypes.STR,
#                 description='Filter by "rent" or "sale"',
#             ),
#             OpenApiParameter(
#                 'beds',
#                 OpenApiTypes.INT,
#                 description='Minimum number of bedrooms to filter',
#             ),
#             OpenApiParameter(
#                 'full_baths',
#                 OpenApiTypes.INT,
#                 description='Minimum number of full bathrooms to filter',
#             ),
#             OpenApiParameter(
#                 'half_baths',
#                 OpenApiTypes.INT,
#                 description='Minimum number of half bathrooms to filter',
#             ),
#             OpenApiParameter(
#                 'water_front',
#                 OpenApiTypes.BOOL,
#                 description='Filter properties with waterfront (true/false)',
#             ),
#             OpenApiParameter(
#                 'built',
#                 OpenApiTypes.INT,
#                 description='Year the property was built to filter',
#             ),
#         ]
#     )
# )
class RealEstatePropertyListView(generics.ListAPIView):
    '''Return a list of properties, also filtered according to a search'''
    serializer_class = RealEstatePropertiesListSerializer
    queryset = RealEstateProperty.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['property_type', 'price', 'county']

    # to separate the queryparams in ints
    def _params_to_ints(self, qs):
        '''Convert a list of strings to integers'''
        return [int(str_id) for str_id in qs.split(',')]

    def get_queryset(self):
        '''Retrieve filtered properties'''
        # get the params from the request
        property_type = self.request.query_params.get('property_type')
        price = self.request.query_params.get('price')
        for_rent_or_sale = self.request.query_params.get('for_rent_or_sale')
        county = self.request.query_params.get('county')
        beds = self.request.query_params.get('beds')
        full_baths = self.request.query_params.get('full_baths')
        half_baths = self.request.query_params.get('half_baths')
        water_front = self.request.query_params.get('water_front')
        built = self.request.query_params.get('built')

        # redefine the queryset
        queryset = self.queryset

        # check for query_params in request

        if property_type:
            property_type = self._params_to_ints(property_type)
            queryset = queryset.filter(property_type__id__in=property_type)

        if price:
            queryset = queryset.filter(price__lte=price)

        if for_rent_or_sale:
            queryset = queryset.filter(for_rent_or_sale=for_rent_or_sale)

        if county:
            county_ids = self._params_to_ints(county)
            queryset = queryset.filter(county__id__in=county_ids)

        if beds:
            queryset = queryset.filter(beds__gte=beds)

        if full_baths:
            queryset = queryset.filter(full_baths__gte=full_baths)

        if half_baths:
            queryset = queryset.filter(half_baths__gte=half_baths)

        if water_front:
            queryset = queryset.filter(
                water_front=water_front.lower() == 'true')

        if built:
            queryset = queryset.filter(built__year=built)

        return queryset.order_by('-id').distinct()


class RealEstatePropertyDetailView(generics.RetrieveAPIView):
    '''Return a detail page of a property'''
