# from dj_rest_auth.registration.views import RegisterView
from authentication.views import CustomRegisterView, CustomUpdateView
from dj_rest_auth.views import LoginView, LogoutView, UserDetailsView
from dj_rest_auth.registration.views import RegisterView, VerifyEmailView, ConfirmEmailView
from django.urls import path, re_path

app_name = 'authentication'

urlpatterns = [

    path("register/", CustomRegisterView.as_view(), name="rest_register"),
    path("login/", LoginView.as_view(), name="rest_login"),
    path("logout/", LogoutView.as_view(), name="rest_logout"),
    path("user/", CustomUpdateView.as_view(), name="rest_user_details"),
    # Rutas de dj-rest-auth
    path('verify-email/', VerifyEmailView.as_view(), name='rest_verify_email'),
    re_path(
        r'^account-confirm-email/(?P<key>[-:\w]+)/$',
        ConfirmEmailView.as_view(),
        name='account_confirm_email',
    ),
]
