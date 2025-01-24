# from dj_rest_auth.registration.views import RegisterView
from authentication.views import CustomRegisterView, CustomUserDetailsView
from dj_rest_auth.views import LoginView, LogoutView, PasswordResetView, PasswordResetConfirmView
from dj_rest_auth.registration.views import VerifyEmailView
from allauth.account.views import ConfirmEmailView
from django.urls import path, re_path

app_name = 'authentication'

urlpatterns = [
    # email confirmation
    path(
        'account-confirm-email/<str:key>/',
        ConfirmEmailView.as_view(),
        name='account_confirm_email',
    ),
    # register
    path("register/", CustomRegisterView.as_view(), name="rest_register"),
    # session in and out
    path("login/", LoginView.as_view(), name="rest_login"),
    path("logout/", LogoutView.as_view(), name="rest_logout"),
    # user details
    path("user/", CustomUserDetailsView.as_view(), name="rest_user_details"),
    # email check
    path('verify-email/', VerifyEmailView.as_view(), name='rest_verify_email'),
]
