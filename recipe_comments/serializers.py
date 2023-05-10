from rest_framework import serializers
from .models import Comment


class CommentReplySerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = "__all__"
        read_only_fields = ["id", "created_at", "user", "recipe"]


class CommentDetailReplySerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = [
            "id",
        ]


class CommentSerializer(serializers.ModelSerializer):
    replies = CommentDetailReplySerializer(many=True, read_only=True)

    class Meta:
        model = Comment
        fields = "__all__"
        read_only_fields = ["id", "created_at", "user", "recipe"]
