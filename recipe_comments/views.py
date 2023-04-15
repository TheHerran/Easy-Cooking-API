from rest_framework import generics
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from recipes.models import Recipe
from utils.permissions import IsOwner

from .models import Comment
from .serializers import CommentSerializer, CommentReplySerializer


class CommentListCreateView(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        recipe = self.kwargs.get("recipe_id")
        recipe = get_object_or_404(Recipe, id=recipe)
        serializer.save(recipe=recipe, user=self.request.user)


class CommentRetrieveDestroyView(generics.RetrieveDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwner]


class CommentReplyCreateView(generics.CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentReplySerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        parent_comment = get_object_or_404(Comment, pk=self.kwargs["comment_id"])
        serializer.save(user=self.request.user, parent=parent_comment)


class CommentReplyRetrieveDestroyView(generics.RetrieveDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentReplySerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwner]
