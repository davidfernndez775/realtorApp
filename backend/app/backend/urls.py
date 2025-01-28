"""
URL configuration for backend project.
"""
from drf_spectacular.views import (SpectacularAPIView, SpectacularSwaggerView,)
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from dj_rest_auth.registration.views import RegisterView, VerifyEmailView, ConfirmEmailView
from dj_rest_auth.views import LoginView, LogoutView, PasswordResetView, PasswordResetConfirmView

urlpatterns = [
    path('admin-site/', admin.site.urls),
    # *documentation paths
    path('api/schema/', SpectacularAPIView.as_view(), name='api-schema'),
    path('api/docs/', SpectacularSwaggerView.as_view(url_name='api-schema'),
         name='api-docs'),
    # *API paths
    path('app/auth/', include('authentication.urls')),
    path('app/real-estate/', include('realstateproperties.urls')),
    # for check registration email
    path('accounts/', include('allauth.urls')),
    # forgot passwords endpoints
    path('password-reset/', PasswordResetView.as_view()),
    path('password-reset-confirm/<uidb64>/<token>/',
         PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
]

admin.site.site_title = "RealtorApp admin (DEV)"
admin.site.site_header = "RealtorApp administration"
admin.site.index_title = "Site administration"

# only in development mode
if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT,
    )
