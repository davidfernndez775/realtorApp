# from dj_rest_auth.registration.views import RegisterView
from authentication.views import CustomRegisterView, CustomUpdateView
from dj_rest_auth.views import LoginView, LogoutView, UserDetailsView
from django.urls import path, include

app_name = 'authentication'

urlpatterns = [
    path("register/", CustomRegisterView.as_view(), name="rest_register"),
    path("login/", LoginView.as_view(), name="rest_login"),
    path("logout/", LogoutView.as_view(), name="rest_logout"),
    path("user/", CustomUpdateView.as_view(), name="rest_user_details"),
    # Rutas de dj-rest-auth
    path("", include('dj_rest_auth.urls')),  # Incluye las URLs de dj-rest-auth
    path("registration/", include('dj_rest_auth.registration.urls')),  # Para registro
]
