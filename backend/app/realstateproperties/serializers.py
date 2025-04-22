'''
Serializers for real estate properties API
'''

from rest_framework import serializers
from PIL import Image
from io import BytesIO
from django.core.files.base import ContentFile
from core.models import RealEstateProperty, PropertyImage





class PropertyImageSerializer(serializers.ModelSerializer):
    '''Serializer for property images'''

    class Meta:
        model = PropertyImage
        fields = ['id', 'property', 'image', 'uploaded_at']
        read_only_fields = ['id', 'uploaded_at']

    def validate_image(self, image):
        # # Tamaño estándar: por ejemplo 800x600 (relación 4:3)
        # target_size = (800, 600)

        # img = Image.open(image)
        # img = img.convert('RGB')  # Por si suben PNGs con transparencia, etc.

        # # Redimensionar con relación de aspecto respetada + relleno (opcional)
        # img.thumbnail(target_size, Image.ANTIALIAS)

        # # Crear lienzo del tamaño exacto y pegar la imagen centrada (relleno blanco)
        # new_img = Image.new('RGB', target_size, (255, 255, 255))
        # offset = ((target_size[0] - img.size[0]) // 2,
        #           (target_size[1] - img.size[1]) // 2)
        # new_img.paste(img, offset)

        # buffer = BytesIO()
        # new_img.save(fp=buffer, format='JPEG')
        # buffer.seek(0)

        # # Reemplazar el archivo original en memoria
        # image_file = ContentFile(buffer.read(), name=image.name)

        # return image_file

        max_size_mb = 0.5  # Tamaño máximo en MB
        max_size_bytes = max_size_mb * 1024 * 1024

        if image.size > max_size_bytes:
            raise serializers.ValidationError(
                f'La imagen no puede superar los {max_size_mb} MB.'
            )

        # Tamaño estándar: 800x600 (relación 4:3)
        target_size = (800, 600)

        img = Image.open(image)
        img = img.convert('RGB')

        img.thumbnail(target_size, Image.ANTIALIAS)

        new_img = Image.new('RGB', target_size, (255, 255, 255))
        offset = (
            (target_size[0] - img.size[0]) // 2,
            (target_size[1] - img.size[1]) // 2
        )
        new_img.paste(img, offset)

        buffer = BytesIO()
        # `quality` puede ayudarte a reducir aún más el peso
        new_img.save(fp=buffer, format='JPEG', quality=85)
        buffer.seek(0)

        final_image = ContentFile(buffer.read(), name=image.name)

        return final_image


class RealEstatePropertiesListSerializer(serializers.ModelSerializer):
    '''Serializer for list of properties'''

    main_image = serializers.SerializerMethodField()

    class Meta:
        model = RealEstateProperty
        fields = ['id', 'title', 'lon', 'lat','county', 'property_type', 'for_rent_or_sale',
                  'price', 'square_ft', 'beds', 'new', 'price_decrease', 'water_front', 'main_image']
        read_only_fields = ['id']

    def get_main_image(self, obj):
        image = obj.images.first()  # 'images' es el related_name en PropertyImage
        if image and image.image:
            return self.context['request'].build_absolute_uri(image.image.url)
        return None

class RealEstatePropertiesDetailtSerializer(serializers.ModelSerializer):
    '''Serializer for property detail including images'''
    images = PropertyImageSerializer(many=True, read_only=True)

    class Meta:
        model = RealEstateProperty
        fields = ['id', 'title', 'county', 'address', 'zip_code', 'property_type', 'for_rent_or_sale', 'price', 'square_ft',
                  'beds', 'new', 'price_decrease', 'full_baths', 'half_baths', 'built', 'water_front', 'description', 'images']
        read_only_fields = ['id']
