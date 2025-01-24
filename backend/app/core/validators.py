import re
from django.core.exceptions import ValidationError
from django.utils.translation import gettext as _


def validate_coordinates(value):
    '''Validate the property position in coordinates'''
    coordinate_pattern = re.compile(
        r"^-?\d{1,3}\.\d{5}$")  # handle negative values too
    if not coordinate_pattern.match(str(value)):
        raise ValidationError(
            f"{value} is not a valid coordinate. It must have from 1 to 3 digits before the decimals, and 5 after the comma."
        )


def validate_zip_code(value):
    '''Validate the zip code format'''
    coordinate_pattern = re.compile(r"\d{5}$")
    if not coordinate_pattern.match(str(value)):
        raise ValidationError(
            f"{value} is not a valid zip code, it must have 5 digits"
        )
