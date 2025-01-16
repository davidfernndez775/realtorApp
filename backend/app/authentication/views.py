from dj_rest_auth.registration.views import RegisterView
from dj_rest_auth.views import UserDetailsView
from authentication.serializers import CustomRegisterSerializer, CustomUserDetailsSerializer
from allauth.account.utils import send_email_confirmation


class CustomRegisterView(RegisterView):
    serializer_class = CustomRegisterSerializer

    def perform_create(self, serializer):
        # Guardar el usuario y pasar el objeto request
        user = serializer.save(request=self.request)
        # Enviar confirmación de correo electrónico
        send_email_confirmation(request=self.request, user=user)
        return user


class CustomUpdateView(UserDetailsView):
    serializer_class = CustomUserDetailsSerializer
