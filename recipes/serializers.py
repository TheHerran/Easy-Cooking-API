from rest_framework import serializers

from accounts.models import Account
from .models import Recipe


class CreateRecipesSerializer(serializers.ModelSerializer):
    # def create(self, validated_data: dict):
    #     return super().create(validated_data)

    class Meta:
        model = Recipe
        fields = [
            "id",
            "title",
            "img",
            "rating",
            "category",
            "preparation",
            "ingredients",
            "user",
            "created_at",
            # "comments"
        ]
        read_only_fields = [
            "id",
            "created_at",
            # "comments"
        ]
