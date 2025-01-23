from dj_rest_auth.registration.views import RegisterView
from dj_rest_auth.views import UserDetailsView
from allauth.account.utils import send_email_confirmation
from authentication.serializers import CustomRegisterSerializer, CustomUserDetailsSerializer
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework import status


class CustomRegisterView(RegisterView):
    serializer_class = CustomRegisterSerializer
    # this is to avoid account-confirm-email not found

    def perform_create(self, serializer):
        user = serializer.save(self.request)
        # Aquí puedes realizar lógica adicional si es necesario
        send_email_confirmation(self.request, user)
        return user

    # this is for sent token after email confirmation
    def create(self, request, *args, **kwargs):
        # Serializa y guarda el usuario
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = self.perform_create(serializer)

        # Genera o recupera el token del usuario
        token, created = Token.objects.get_or_create(user=user)

        # Devuelve la respuesta con el token
        return Response({
            "key": token.key,
        }, status=status.HTTP_201_CREATED)


class CustomUpdateView(UserDetailsView):
    serializer_class = CustomUserDetailsSerializer
