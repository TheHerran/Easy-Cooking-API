# Generated by Django 4.1.5 on 2023-07-21 23:14

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("accounts", "0002_alter_account_password"),
    ]

    operations = [
        migrations.AlterField(
            model_name="account",
            name="username",
            field=models.CharField(max_length=500, unique=True),
        ),
    ]
