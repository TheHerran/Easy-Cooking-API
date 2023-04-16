from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .models import Rating
from .serializers import RatingSerializer


class RatingListCreateView(generics.ListCreateAPIView):
    serializer_class = RatingSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        recipe = self.kwargs.get("recipe_id")
        queryset = Rating.objects.filter(recipe=recipe)
        return queryset

    def perform_create(self, serializer):
        user = self.request.user
        recipe = self.kwargs["recipe_id"]
        rating = Rating.objects.filter(user=user, recipe=recipe).first()
        
        if rating:
            serializer.instance = rating
            serializer.validated_data["rating"] = serializer.validated_data["rating"]
            serializer.update(rating, serializer.validated_data)
        else:
            serializer.save(user=user, recipe=recipe)
