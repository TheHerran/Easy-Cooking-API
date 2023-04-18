from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.exceptions import ValidationError

from recipes.models import Recipe

from .models import Favorite
from .serializers import FavoriteSerializer


class FavoriteListCreateView(generics.ListCreateAPIView):
    queryset = Favorite.objects.all()
    serializer_class = FavoriteSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        recipe = self.kwargs["recipe_id"]
        user = self.request.user

        if Favorite.objects.filter(user=user, recipe=recipe).exists():
            raise ValidationError("This recipe is already in your favorites.")

        try:
            recipe = Recipe.objects.get(pk=recipe)
        except recipe.DoesNotExist:
            raise ValidationError("This recipe does not exist")

        serializer.save(user=user, recipe=recipe)

    def get_queryset(self):
        return Favorite.objects.filter(
            user=self.request.user, recipe=self.kwargs["recipe_id"]
        )


class FavoriteRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Favorite.objects.all()
    serializer_class = FavoriteSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_object(self):
        user = self.request.user
        recipe = self.kwargs["recipe_id"]

        try:
            return Favorite.objects.get(user=user, recipe=recipe)
        except Favorite.DoesNotExist:
            raise ValidationError("This recipe is not in your favorite list")
