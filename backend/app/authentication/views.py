'''
Views for user's endpoints
'''

from dj_rest_auth.registration.views import RegisterView
from dj_rest_auth.views import UserDetailsView
from allauth.account.utils import send_email_confirmation
from authentication.serializers import CustomRegisterSerializer, CustomUserDetailsSerializer

from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework import status, generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from authentication.serializers import FavoritePropertySerializer
from core.models import FavoriteProperty, RealEstateProperty


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


class FavoritePropertyToggleView(generics.GenericAPIView):
    '''Add or remove a property from the user's favorites'''
    serializer_class = FavoritePropertySerializer
    permission_classes = [IsAuthenticated]

    # as I use a toggleview I only need implement a post method because if the property is
    # in the list of favorites when I made the post, it gets remove from the list
    def post(self, request, *args, **kwargs):
        property_id = kwargs.get("property_id")
        user = request.user

        try:
            property_obj = RealEstateProperty.objects.get(id=property_id)
        except RealEstateProperty.DoesNotExist:
            return Response({"detail": "Property not found."}, status=status.HTTP_404_NOT_FOUND)

        favorite, created = FavoriteProperty.objects.get_or_create(
            user=user, property=property_obj)

        if not created:
            favorite.delete()
            return Response({"detail": "Property removed from favorites."}, status=status.HTTP_200_OK)

        return Response({"detail": "Property added to favorites."}, status=status.HTTP_201_CREATED)
