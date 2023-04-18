from django.urls import path

from .views import FavoriteListCreateView, FavoriteRetrieveUpdateDestroyView

urlpatterns = [
    path("<uuid:recipe_id>/favorites/", FavoriteListCreateView.as_view()),
    path("<uuid:recipe_id>/favorites/<uuid:pk>/", FavoriteRetrieveUpdateDestroyView.as_view()),
]