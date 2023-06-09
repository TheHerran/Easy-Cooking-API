from django.urls import path

from . import views

urlpatterns = [
    path("recipe/", views.RecipeListCreateView.as_view()),
    path("recipe/<pk>/", views.RecipeRetrieveUpdateDestroyView.as_view()),
    path("user/<slug:username>/recipes/", views.RecipeListByUserView.as_view()),
]
