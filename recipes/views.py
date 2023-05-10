from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django.shortcuts import get_object_or_404

from utils.permissions import IsOwner
from accounts.models import Account

from .models import Recipe
from .serializers import RecipesSerializer, RecipesUpdateSerializer


class RecipeListCreateView(generics.ListCreateAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipesSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save()


class RecipeRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipesUpdateSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwner]


class RecipeListByUserView(generics.ListAPIView):
    serializer_class = RecipesSerializer
    lookup_field = "username"

    def get_queryset(self):
        username = self.kwargs["username"]
        user = get_object_or_404(Account, username=username)
        queryset = Recipe.objects.filter(user=user)
        return queryset