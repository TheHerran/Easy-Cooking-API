from rest_framework import serializers
from .models import Comment

class CommentReplySerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = "__all__"
        read_only_fields = ["id", "created_at", "user"]


class CommentSerializer(serializers.ModelSerializer):
    replies = CommentReplySerializer(many=True, read_only=True)
    
    class Meta:
        model = Comment
        fields = "__all__"
        read_only_fields = ["id", "created_at", "user"]


