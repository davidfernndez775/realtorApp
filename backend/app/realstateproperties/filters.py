import django_filters
from core.models import RealEstateProperty


class RealEstatePropertyFilter(django_filters.FilterSet):
    property_type = django_filters.ChoiceFilter(
        field_name='property_type',
        choices=RealEstateProperty.PropertyType.choices
    )
    county = django_filters.ChoiceFilter(
        field_name='county',
        choices=RealEstateProperty.CountyList.choices
    )
    for_rent_or_sale = django_filters.ChoiceFilter(
        field_name='for_rent_or_sale',
        choices=RealEstateProperty.PropertyStatus.choices
    )
    price = django_filters.NumberFilter(field_name='price', lookup_expr='lte')
    beds = django_filters.NumberFilter(field_name='beds', lookup_expr='gte')
    full_baths = django_filters.NumberFilter(
        field_name='full_baths', lookup_expr='gte')
    half_baths = django_filters.NumberFilter(
        field_name='half_baths', lookup_expr='gte')
    water_front = django_filters.BooleanFilter(field_name='water_front')
    built = django_filters.NumberFilter(
        field_name='built', lookup_expr='exact')

    class Meta:
        model = RealEstateProperty
        fields = ['property_type', 'price', 'county', 'beds',
                  'full_baths', 'half_baths', 'water_front', 'built']
