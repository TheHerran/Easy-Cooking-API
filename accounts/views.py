from django.contrib.auth import authenticate
from rest_framework import generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.views import Request, Response, status
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

from utils.mixins import SerializerByMethodMixin

from .models import Account
from .permissions import IsProfileOwner
from .serializers import (
    AccountSerializer,
    LoginAccountSerializer,
    UpdateAccountSerializer,
    LoginJWTSerializer
)


class LoginJWTView(TokenObtainPairView):
    serializer_class = LoginJWTSerializer

class CreateAccountsView(generics.ListCreateAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer


# class LoginAccountView(ObtainAuthToken):
#     def post(self, request: Request) -> Response:
#         serializer = LoginAccountSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         user = authenticate(**serializer.validated_data)

#         if not user:
#             return Response(
#                 {"detail": "Invalid username or password!"}, status.HTTP_400_BAD_REQUEST
#             )
#         token, _ = Token.objects.get_or_create(user=user)
#         return Response(token.key)


class UpdateAccountView(SerializerByMethodMixin, generics.UpdateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, IsProfileOwner]

    queryset = Account.objects.all()
    serializer_map = {
        "PATCH": UpdateAccountSerializer,
    }
