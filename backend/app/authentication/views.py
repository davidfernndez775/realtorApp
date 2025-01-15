from dj_rest_auth.registration.views import RegisterView
from dj_rest_auth.views import UserDetailsView
from authentication.serializers import CustomRegisterSerializer, CustomUserDetailsSerializer


class CustomRegisterView(RegisterView):
    serializer_class = CustomRegisterSerializer


class CustomUpdateView(UserDetailsView):
    serializer_class = CustomUserDetailsSerializer
