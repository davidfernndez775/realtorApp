'''
Views for user's endpoints
'''

from dj_rest_auth.registration.views import RegisterView
from dj_rest_auth.views import UserDetailsView
from allauth.account.utils import send_email_confirmation
from authentication.serializers import CustomRegisterSerializer, CustomUserDetailsSerializer

from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework import status, viewsets, mixins
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from authentication.serializers import FavoritePropertySerializer
from core.models import FavoriteProperty



class CustomRegisterView(RegisterView):
    serializer_class = CustomRegisterSerializer
    # this is to avoid account-confirm-email not found

    def perform_create(self, serializer):
        user = serializer.save(self.request)
        # Aquí puedes realizar lógica adicional si es necesario
        send_email_confirmation(self.request, user)
        return user

    # this is for send token after email confirmation
    def create(self, request, *args, **kwargs):
        # Serialize and save the user
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = self.perform_create(serializer)

        # Create or retrieve the user's token
        token, created = Token.objects.get_or_create(user=user)

        # Return the response with the token
        return Response({
            "key": token.key,
        }, status=status.HTTP_201_CREATED)


class CustomUserDetailsView(UserDetailsView):
    serializer_class = CustomUserDetailsSerializer


class FavoritePropertyViewSet(mixins.ListModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, mixins.CreateModelMixin, viewsets.GenericViewSet):
    '''Base viewset for favorites properties'''
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = FavoritePropertySerializer
    queryset = FavoriteProperty.objects.all()

    def get_queryset(self):
        '''Filter queryset to authenticated user'''
        return self.queryset.filter(user=self.request.user).order_by('-name')
