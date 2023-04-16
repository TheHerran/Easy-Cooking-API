import uuid

from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class Rating(models.Model):
    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["post", "user"], name="unique_recipe_user_rating"
            )
        ]

    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    user = models.ForeignKey("accounts.Account", on_delete=models.CASCADE)
    recipe = models.ForeignKey(
        "recipes.Recipe",
        on_delete=models.CASCADE,
        related_name="rating",
    )
    rating = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )
