from rest_framework import serializers

from accounts.models import Account
from .models import Recipe


class CreateRecipesSerializer(serializers.ModelSerializer):
    # def create(self, validated_data: dict):
    #     return super().create(validated_data)

    class Meta:
        model = Recipe
        fields = '__all__'
        read_only_fields = [
            "id",
            "created_at",
            # "comments"
        ]
