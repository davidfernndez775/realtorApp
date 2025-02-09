'''
Django admin customization
'''

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _

from core import models

# *USER MODEL
# define actions for admin panel


@admin.action(description="Activate selected users")
def activate_users(modeladmin, request, queryset):
    queryset.update(is_active=True)


@admin.action(description="Deactivate selected users")
def deactivate_users(modeladmin, request, queryset):
    queryset.update(is_active=False)

class FavoritePropertyInline(admin.TabularInline):
    model = models.FavoriteProperty
    extra = 0  # No mostrar filas vacías por defecto
    readonly_fields = ['added_at']  # Mostrar solo lectura para la fecha
    autocomplete_fields = ['property']  # Permite búsqueda rápida de propiedades


class UserAdmin(BaseUserAdmin):
    '''Define the admin pages for users'''
    inlines = [FavoritePropertyInline]  # Agregar favoritos dentro del usuario
    ordering = ['id']   # order the list by id
    list_display = ['email', 'username']    # show fields email and username
    actions = [activate_users, deactivate_users]
    fieldsets = ((None, {'fields': ('email', 'password', 'username', 'phone')}),
                 (_('Permissions'), {'fields': (
                     'is_active', 'is_staff', 'is_superuser')}),
                 (_('Important dates'), {'fields': ('last_login',)}))
    readonly_fields = ['last_login']
    # in add_fieldsets I use 'classes' only for custom the appereance of the page
    # is opcional
    add_fieldsets = ((None, {'classes': ('wide',),
                             'fields': ('email', 'password1', 'password2', 'username', 'is_active', 'is_staff', 'is_superuser',)}),)


# register the model
admin.site.register(models.User, UserAdmin)
admin.site.register(models.FavoriteProperty)


# *REALSTATEPROPERTY MODEL
# PropertyImage is register throw RealEstateProperty
class PropertyImageInline(admin.TabularInline):
    model = models.PropertyImage
    extra = 1


@admin.register(models.RealEstateProperty)
class RealEstatePropertyAdmin(admin.ModelAdmin):
    inlines = [PropertyImageInline]
    list_display = ['title', 'price', 'owner']
    search_fields = ['title', 'owner']
    list_filter = ['property_type', 'price', 'for_rent_or_sale', 'county',
                   'beds', 'full_baths', 'half_baths', 'square_ft', 'water_front', 'built']
    fieldsets = ((None, {'fields': ('title', 'lon', 'lat', 'property_type', 'county', 'address', 'zip_code', 'for_rent_or_sale', 'price')}), (_('DESCRIPTION'), {'fields': ('beds', 'full_baths', 'half_baths',
                 'water_front', 'built', 'square_ft', 'description')}), (_('OWNER INFO'), {'fields': ('owner', 'phone_number')}), (_('IMPORTANT DATES'), {'fields': ('created_at', 'updated_at')}))
    readonly_fields = ['created_at', 'updated_at']

# *COMMENT MODEL


@admin.register(models.Comments)
class CommentsAdmin(admin.ModelAdmin):
    list_display = ['content', 'in_use']
    list_filter = ['in_use']


# TODO implement DjangQL for queries and import-export for Excel, CSV and JSON
