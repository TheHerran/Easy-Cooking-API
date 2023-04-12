# Generated by Django 4.1.5 on 2023-04-12 03:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("recipes", "0005_alter_recipe_user"),
    ]

    operations = [
        migrations.AlterField(
            model_name="recipe",
            name="user",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="recipes",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
