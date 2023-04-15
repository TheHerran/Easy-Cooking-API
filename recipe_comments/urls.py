from django.urls import path

from . import views

urlpatterns = [
    path("<uuid:recipe_id>/comments/", views.CommentListCreateView.as_view()),
    path("<uuid:recipe_id>/comments/<pk>/", views.CommentRetrieveDestroyView.as_view()),
    path("<uuid:recipe_id>/comments/<uuid:comment_id>/reply/", views.CommentReplyCreateView.as_view()),
    path("<uuid:recipe_id>/comments/<uuid:comment_id>/reply/<pk>", views.CommentReplyRetrieveDestroyView.as_view()),
]
