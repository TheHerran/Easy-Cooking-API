from rest_framework import serializers

from recipes.serializers import RecipesRelationshipSerializer

from .models import Favorite


class FavoriteSerializer(serializers.ModelSerializer):
    recipe = RecipesRelationshipSerializer(read_only=True)

    class Meta:
        model = Favorite
        fields = "__all__"
        read_only_fields = ["user", "recipe"]
    def create(self, validated_data):
        validated_data["user"] = self.context["request"].user
        return super().create(validated_data)


class FavoriteRelationshipSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favorite
        fields = [
            "id",
        ]
