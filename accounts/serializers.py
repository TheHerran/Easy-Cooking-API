from rest_framework import serializers

from .models import Account


class AccountSeriazlizer(serializers.ModelSerializer):
    def create(self, validated_data):
        return Account.objects.create_user(**validated_data)

    class Meta:
        model = Account
        fields = [
            "id",
            "username",
            "email",
            "password",
            "created_at",
            "updated_at",
            "is_active"
        ]
        read_only_fields = ["created_at", "updated_at", "is_active"]
        extra_kwargs = {"password": {"write_only": True}}

class LoginAccountSerializer(serializers.Serializer):
    username = serializers.CharField(write_only=True)
    password = serializers.CharField(write_only=True)

class UpdateAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = [
            "id",
            "username",
            "email",
            "password",
            "created_at",
            "updated_at"
        ]
        read_only_fields = [
            "id",
            "created_at",
            "updated_at",
            "is_active",
        ]
        extra_kwargs = {"password": {"write_only": True}}