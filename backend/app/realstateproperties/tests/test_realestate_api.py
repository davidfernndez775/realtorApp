from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from core.models import RealEstateProperty


class RealEstatePropertyAPITests(TestCase):
    """Tests for the real estate property API"""

    def setUp(self):
        """Set up test data"""
        self.client = APIClient()

        # Crear algunas propiedades de prueba
        self.property1 = RealEstateProperty.objects.create(
            title="Casa en Miami",
            lon=80.14534,
            lat=25.15476,
            county="Miami Dade",
            property_type="Single Family",
            address="241 93th ave",
            zip_code=33131,
            for_rent_or_sale="for_sale",
            price=300000,
            square_ft=2600,
            beds=3,
            full_baths=2,
            half_baths=1,
            built=2010,
            water_front=True
        )

        self.property2 = RealEstateProperty.objects.create(
            title="Apartamento en Broward",
            lon=80.14134,
            lat=25.15478,
            county="Broward",
            property_type="Condo/Co-Op/Villa/Townhouse",
            address="261 62th ave",
            zip_code=33101,
            for_rent_or_sale="for_rent",
            price=200000,
            square_ft=5200,
            beds=2,
            full_baths=1,
            half_baths=0,
            built=2015,
            water_front=False
        )

    def test_list_properties(self):
        """Test retrieving a list of properties"""
        response = self.client.get("/app/real-estate/list/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_filter_by_county(self):
        """Test filtering properties by county"""
        response = self.client.get(
            "/app/real-estate/list/", {"county": "Miami Dade"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["county"], "Miami Dade")

    def test_filter_by_price_range(self):
        """Test filtering properties by price range"""
        response = self.client.get(
            "/app/real-estate/list/", {"price_min": 250000, "price_max": 350000})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["price"], 300000)

    def test_filter_by_square_ft_range(self):
        """Test filtering properties by square_ft range"""
        response = self.client.get(
            "/app/real-estate/list/", {"square_ft_min": 2500, "square_ft_max": 3500})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["square_ft"], 2600)

    def test_filter_by_beds(self):
        """Test filtering properties by number of beds"""
        response = self.client.get(
            "/app/real-estate/list/", {"beds_min": 2, "beds_max": 3})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_filter_by_for_rent_or_sale(self):
        """Test filtering properties by for_rent_or_sale"""
        response = self.client.get(
            "/app/real-estate/list/", {"for_rent_or_sale": "for_sale"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["for_rent_or_sale"], "for_sale")
