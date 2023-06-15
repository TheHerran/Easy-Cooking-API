from django.urls import path
from .views import RatingListCreateView

urlpatterns = [
    path('rating/<uuid:recipe_id>/', RatingListCreateView.as_view()),
]