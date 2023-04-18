from rest_framework import serializers

from recipes.serializers import RecipesSerializer

from .models import Favorite


class FavoriteSerializer(serializers.ModelSerializer):
    # recipe = RecipesSerializer(read_only=True)

    class Meta:
        model = Favorite
        fields = "__all__"

    def create(self, validated_data):
        validated_data['user'] = self.context['request'].user
        return super().create(validated_data)
    
