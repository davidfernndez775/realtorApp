from dj_rest_auth.registration.views import RegisterView
from authentication.serializers import CustomRegisterSerializer


class CustomRegisterView(RegisterView):
    serializer_class = CustomRegisterSerializer
