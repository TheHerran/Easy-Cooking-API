# Generated by Django 4.1.5 on 2023-04-12 01:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Recipe",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("title", models.CharField(max_length=50)),
                ("img", models.CharField(max_length=512)),
                ("ingredients", models.TextField()),
                ("preparation", models.TextField()),
                ("rating", models.IntegerField()),
                (
                    "category",
                    models.CharField(
                        choices=[
                            ("Prato Principal", "Main"),
                            ("Sobremesas", "Dessert"),
                            ("Lanches", "Snacks"),
                            ("Bebidas", "Drinks"),
                            ("Não informado", "Default"),
                        ],
                        default="Não informado",
                        max_length=20,
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                (
                    "user",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="recipes",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]