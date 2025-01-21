"""
URL configuration for backend project.
"""
from drf_spectacular.views import (SpectacularAPIView, SpectacularSwaggerView,)
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from dj_rest_auth.registration.views import RegisterView, VerifyEmailView, ConfirmEmailView

urlpatterns = [
    path('admin/', admin.site.urls),
    # *documentation paths
    path('api/schema/', SpectacularAPIView.as_view(), name='api-schema'),
    path('api/docs/', SpectacularSwaggerView.as_view(url_name='api-schema'),
         name='api-docs'),
    # *API paths
    path('app/auth/', include('authentication.urls')),
    # for check registration email
    path('accounts/', include('allauth.urls')),
]

# only in development mode
if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT,
    )
