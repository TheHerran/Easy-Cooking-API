from rest_framework import serializers

from .models import Recipe


class RecipesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Recipe
        fields = "__all__"
        read_only_fields = [
            "id",
            "created_at",
        ]

    def create(self, validated_data):
        recipe = Recipe.objects.create(user=self.context["request"].user, **validated_data)
        return recipe


class RecipesUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Recipe
        fields = "__all__"
        read_only_fields = [
            "id",
            "created_at",
            "user",
            "rating",
        ]
