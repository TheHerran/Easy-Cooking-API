from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from recipes.serializers import RecipesSerializer, RecipesRelationshipSerializer
from favorites.serializers import FavoriteSerializer, FavoriteRelationshipSerializer

from .models import Account


class LoginJWTSerializer(TokenObtainPairSerializer):
    def get_token(cls, user):
        token = super().get_token(user)
        token["username"] = user.username
        return token


class AccountSerializer(serializers.ModelSerializer):
    # recipes = RecipesRelationshipSerializer(read_only=True, many=True)
    # favorites = FavoriteRelationshipSerializer(read_only=True, many= True)

    class Meta:
        model = Account
        fields = "__all__"
        read_only_fields = ["created_at", "updated_at", "recipes"]
        extra_kwargs = {
            "password": {"write_only": True},
            "last_login": {"write_only": True},
        }

    def create(self, validated_data):
        return Account.objects.create_user(**validated_data)
    

class AccountDetailsSerializer(serializers.ModelSerializer):
    recipes = RecipesSerializer(read_only=True, many=True)
    favorites = FavoriteSerializer(read_only=True, many= True)

    class Meta:
        model = Account
        fields = "__all__"
        read_only_fields = ["created_at", "updated_at", "recipes"]
        extra_kwargs = {
            "password": {"write_only": True},
            "last_login": {"write_only": True},
        }


class UpdateAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = "__all__"
        read_only_fields = ["id", "created_at", "updated_at", "is_active"]
        extra_kwargs = {
            "password": {"write_only": True},
            "last_login": {"write_only": True},
        }
