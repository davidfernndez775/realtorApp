# test_settings.py
from .settings import *

# change the email backend only for tests
EMAIL_BACKEND = 'django.core.mail.backends.locmem.EmailBackend'