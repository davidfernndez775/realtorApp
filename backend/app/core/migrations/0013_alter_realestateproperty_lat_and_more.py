# Generated by Django 5.1.4 on 2025-01-24 18:36

import core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_realestateproperty_for_rent_or_sale'),
    ]

    operations = [
        migrations.AlterField(
            model_name='realestateproperty',
            name='lat',
            field=models.DecimalField(decimal_places=5, help_text='Enter a valid coordinate, 1 to 3 digits before the comma and 5 after.', max_digits=8, validators=[core.validators.validate_coordinates]),
        ),
        migrations.AlterField(
            model_name='realestateproperty',
            name='lon',
            field=models.DecimalField(decimal_places=5, help_text='Enter a valid coordinate, 1 to 3 digits before the comma and 5 after.', max_digits=8, validators=[core.validators.validate_coordinates]),
        ),
        migrations.AlterField(
            model_name='realestateproperty',
            name='zip_code',
            field=models.IntegerField(validators=[core.validators.validate_coordinates]),
        ),
    ]
