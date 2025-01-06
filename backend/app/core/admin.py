'''
Django admin customization
'''

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _

from core import models


class UserAdmin(BaseUserAdmin):
    '''Define the admin pages for users'''
    ordering = ['id']   # order the list by id
    list_display = ['email', 'name']    # show fields email and name
    fieldsets = ((None, {'fields': ('email', 'password')}),
                 (_('Permissions'), {'fields': (
                     'is_active', 'is_staff', 'is_superuser')}),
                 (_('Important dates'), {'fields': ('last_login',)}))
    readonly_fields = ['last_login']
    # in add_fieldsets I use 'classes' only for custom the appereance of the page
    # is opcional
    add_fieldsets = ((None, {'classes': ('wide',),
                             'fields': ('email', 'password1', 'password2', 'name', 'is_active', 'is_staff', 'is_superuser',)}),)


admin.site.register(models.User, UserAdmin)