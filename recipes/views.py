from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from utils.permissions import IsRecipeOwner

from .models import Recipe
from .serializers import RecipesSerializer


class RecipeListCreateView(generics.ListCreateAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipesSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save()


class RecipeRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipesSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsRecipeOwner]

    # def perform_destroy(self, instance):
    #     instance.soft_delete()