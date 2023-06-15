import uuid
from django.db import models
from django.contrib.auth import get_user_model


class Comment(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    recipe = models.ForeignKey("recipes.Recipe", on_delete=models.CASCADE)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='replies')
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    # def __str__(self):
    #     return self.text