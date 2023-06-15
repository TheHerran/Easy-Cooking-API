from rest_framework import generics
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from recipes.models import Recipe

from .models import Rating
from .serializers import RatingSerializer


class RatingListCreateView(generics.ListCreateAPIView):
    serializer_class = RatingSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        recipe = self.kwargs.get("recipe_id")
        return Rating.objects.filter(recipe=recipe)

    def perform_create(self, serializer):
        user = self.request.user
        recipe = self.kwargs["recipe_id"]
        recipe = get_object_or_404(Recipe, id=self.kwargs["recipe_id"])
        rating = Rating.objects.filter(user=user, recipe=recipe).first()

        if rating:
            serializer.instance = rating
            serializer.validated_data["rating"] = serializer.validated_data["rating"]
            serializer.update(rating, serializer.validated_data)
        else:
            serializer.save(user=user, recipe=recipe)
