# test_settings.py
from .settings import *

# Cambia el backend de correo solo para las pruebas
EMAIL_BACKEND = 'django.core.mail.backends.locmem.EmailBackend'