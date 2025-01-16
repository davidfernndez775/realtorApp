from dj_rest_auth.registration.views import RegisterView
from dj_rest_auth.views import UserDetailsView
from authentication.serializers import CustomRegisterSerializer, CustomUserDetailsSerializer
from django.urls import reverse
from allauth.account.utils import send_email_confirmation
from allauth.account.adapter import get_adapter
from allauth.account.models import EmailConfirmationHMAC


class CustomRegisterView(RegisterView):
    serializer_class = CustomRegisterSerializer

    def perform_create(self, serializer):
        # Guardar el usuario y pasar el objeto request
        user = serializer.save(request=self.request)
        # Enviar confirmación de correo electrónico
        send_email_confirmation(request=self.request, user=user)
        # Update the reverse call to include the app_name for email confirmation
        email_confirmation = EmailConfirmationHMAC(user)
        activate_url = reverse('authentication:account_confirm_email', args=[
                               email_confirmation.key])
        get_adapter().send_confirmation_mail(
            self.request, email_confirmation, signup=True)
        return user


class CustomUpdateView(UserDetailsView):
    serializer_class = CustomUserDetailsSerializer
