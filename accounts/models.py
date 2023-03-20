import uuid

from django.contrib.auth.models import AbstractUser
from django.db import models

class Account(AbstractUser):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    username = models.CharField(max_length=25, unique=True)
    email = models.EmailField(max_length=255, unique=True)
    password = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)