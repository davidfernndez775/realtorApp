# from dj_rest_auth.registration.views import RegisterView
from authentication.views import CustomRegisterView
from dj_rest_auth.views import LoginView, LogoutView, UserDetailsView
from django.urls import path


urlpatterns = [
    path("register/", CustomRegisterView.as_view(), name="rest_register"),
    path("login/", LoginView.as_view(), name="rest_login"),
    path("logout/", LogoutView.as_view(), name="rest_logout"),
    path("user/", UserDetailsView.as_view(), name="rest_user_details"),
]
