from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    avatar = models.ImageField(blank=True)
    bio = models.TextField(blank=True, max_length=255)