import uuid

from django.db import models


class Category(models.TextChoices):
    MAIN = "Prato Principal"
    DESSERT = "Sobremesas"
    SNACKS = "Lanches"
    DRINKS = "Bebidas"
    DEFAULT = "Não informado"


class Recipe(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    title = models.CharField(max_length=50)
    img = models.CharField(max_length=512)
    ingredients = models.TextField()
    preparation = models.TextField()
    rating = models.IntegerField(null=True)
    category = models.CharField(
        max_length=20,
        choices=Category.choices,
        default=Category.DEFAULT,
    )
    user = models.ForeignKey(
        "accounts.Account",
        on_delete=models.CASCADE,
        related_name="recipes",
        null=True
    )
    # comments = models.ForeignKey()
    created_at = models.DateTimeField(auto_now_add=True)
