from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    avatar = models.ImageField(blank=True, upload_to="accounts/%Y/%m")
    nickname = models.CharField(unique=True, max_length=10)
    bio = models.TextField(blank=True, max_length=255)