# Generated by Django 5.1.4 on 2025-01-24 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_remove_realestateproperty_for_sale_or_rent_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='realestateproperty',
            name='for_rent_or_sale',
            field=models.CharField(choices=[('for_sale', 'En venta'), ('for_rent', 'En renta')], default=(
                'for_sale', 'En venta'), max_length=100),
        ),
    ]
