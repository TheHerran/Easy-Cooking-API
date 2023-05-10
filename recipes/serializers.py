from rest_framework import serializers

from ratings.serializers import RatingSerializer
from ingredients.serializers import IngredientSerializer
from ingredients.models import Ingredient

from .models import Recipe


class RecipesSerializer(serializers.ModelSerializer):
    rating = RatingSerializer(read_only=True, many=True)
    ingredients = IngredientSerializer(many=True)

    class Meta:
        model = Recipe
        fields = "__all__"
        read_only_fields = [
            "id",
            "created_at",
        ]

    def create(self, validated_data):
        ingredients_data = validated_data.pop("ingredients")
        recipe = Recipe.objects.create(user=self.context["request"].user, **validated_data)
        for ingredient_data in ingredients_data:
            Ingredient.objects.create(recipe=recipe, **ingredient_data)
        return recipe
    
    
class RecipesRelationshipSerializer(serializers.ModelSerializer):
    rating = RatingSerializer(read_only=True, many=True)

    class Meta:
        model = Recipe
        fields = "__all__"


class RecipesUpdateSerializer(serializers.ModelSerializer):
    rating = RatingSerializer(read_only=True, many=True)
    ingredients = IngredientSerializer(many=True)


    class Meta:
        model = Recipe
        fields = "__all__"
        read_only_fields = [
            "id",
            "created_at",
            "user",
            "rating",
        ]

    def update(self, instance, validated_data):
        ingredients_data = validated_data.pop("ingredients")
        instance = super().update(instance, validated_data)
        instance.ingredients.all().delete()
        for ingredient_data in ingredients_data:
            Ingredient.objects.create(recipe=instance, **ingredient_data)
        return instance