# from dj_rest_auth.registration.views import RegisterView
from authentication.views import CustomRegisterView, CustomUpdateView
from dj_rest_auth.views import LoginView, LogoutView
from dj_rest_auth.registration.views import VerifyEmailView
from allauth.account.views import ConfirmEmailView
from django.urls import path, re_path

app_name = 'authentication'

urlpatterns = [
    # Ruta para la confirmación de email
    path(
        'account-confirm-email/<str:key>/',
        ConfirmEmailView.as_view(),
        name='account_confirm_email',
    ),
    # Registro de usuarios
    path("register/", CustomRegisterView.as_view(), name="rest_register"),
    # Inicio y cierre de sesión
    path("login/", LoginView.as_view(), name="rest_login"),
    path("logout/", LogoutView.as_view(), name="rest_logout"),
    # Detalles del usuario
    path("user/", CustomUpdateView.as_view(), name="rest_user_details"),
    # Verificación de email
    path('verify-email/', VerifyEmailView.as_view(), name='rest_verify_email'),
]
