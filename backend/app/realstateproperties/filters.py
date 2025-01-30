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
    # Rango de valores para price
    price_min = django_filters.NumberFilter(
        field_name='price', lookup_expr='gte')
    price_max = django_filters.NumberFilter(
        field_name='price', lookup_expr='lte')

    # Rango de valores para beds
    beds_min = django_filters.NumberFilter(
        field_name='beds', lookup_expr='gte')
    beds_max = django_filters.NumberFilter(
        field_name='beds', lookup_expr='lte')

    # Rango de valores para full_baths
    full_baths_min = django_filters.NumberFilter(
        field_name='full_baths', lookup_expr='gte')
    full_baths_max = django_filters.NumberFilter(
        field_name='full_baths', lookup_expr='lte')

    # Rango de valores para half_baths
    half_baths_min = django_filters.NumberFilter(
        field_name='half_baths', lookup_expr='gte')
    half_baths_max = django_filters.NumberFilter(
        field_name='half_baths', lookup_expr='lte')

    # Rango de valores para built (año de construcción)
    built_min = django_filters.NumberFilter(
        field_name='built', lookup_expr='gte')
    built_max = django_filters.NumberFilter(
        field_name='built', lookup_expr='lte')

    class Meta:
        model = RealEstateProperty
        fields = [
            'property_type', 'county', 'for_rent_or_sale',
            'price_min', 'price_max', 'beds_min', 'beds_max',
            'full_baths_min', 'full_baths_max', 'half_baths_min', 'half_baths_max',
            'built_min', 'built_max'
        ]

