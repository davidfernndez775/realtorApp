# from dj_rest_auth.registration.views import RegisterView
from authentication.views import CustomRegisterView, CustomUpdateView
from dj_rest_auth.views import LoginView, LogoutView, UserDetailsView
from dj_rest_auth.registration.views import RegisterView, VerifyEmailView
# only while the frontend is no develop yet
from allauth.account.views import ConfirmEmailView
from django.urls import path, re_path, include

app_name = 'authentication'

urlpatterns = [
    # re_path(
    #     r'^account-confirm-email/(?P<key>[-:\w]+)/$',
    #     ConfirmEmailView.as_view(),
    #     name='account_confirm_email',
    # ),
    path("register/", CustomRegisterView.as_view(), name="rest_register"),
    path("login/", LoginView.as_view(), name="rest_login"),
    path("logout/", LogoutView.as_view(), name="rest_logout"),
    path("user/", CustomUpdateView.as_view(), name="rest_user_details"),
    # path("auth/registration/", include("dj_rest_auth.registration.urls")),
    # Rutas de dj-rest-auth
    # path('registration/account-confirm-email/<str:key>/', ConfirmEmailView.as_view()),
    # path('registration/', include('dj_rest_auth.registration.urls'))
    # path('registration/verify-email/',
    #      VerifyEmailView.as_view(), name='rest_verify_email'),
    path('registration/account-confirm-email/',
         VerifyEmailView.as_view(), name='account_email_verification_sent'),
    # re_path(r'^registration/account-confirm-email/(?P<key>[-:\w]+)/$',
    #      VerifyEmailView.as_view(), name='account_confirm_email'),
]
