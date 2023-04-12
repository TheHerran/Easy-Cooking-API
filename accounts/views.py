from rest_framework import generics
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

from utils.mixins import SerializerByMethodMixin

from .models import Account
from .permissions import IsProfileOwner
from .serializers import (
    AccountSerializer,
    UpdateAccountSerializer,
    LoginJWTSerializer,
)


class LoginJWTView(TokenObtainPairView):
    serializer_class = LoginJWTSerializer


class CreateAccountsView(generics.ListCreateAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer


class RetrieveAccountsView(generics.RetrieveAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, IsProfileOwner]

    queryset = Account.objects.all()
    serializer_class = AccountSerializer


class UpdateAccountView(SerializerByMethodMixin, generics.UpdateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, IsProfileOwner]

    queryset = Account.objects.all()
    serializer_map = {
        "PATCH": UpdateAccountSerializer,
    }
