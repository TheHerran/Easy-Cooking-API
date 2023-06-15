import uuid
from django.db import models

from recipes.models import Recipe


class Ingredient(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    item = models.CharField(max_length=255)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name="ingredients")