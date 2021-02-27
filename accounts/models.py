from django.contrib.auth.models import AbstractUser
from django.urls import reverse
from django.db import models


class User(AbstractUser):
    avatar = models.ImageField(blank=True, upload_to="accounts/%Y/%m")
    nickname = models.CharField(unique=True, max_length=10)
    bio = models.TextField(blank=True, max_length=255)

    def get_absolute_url(self):
        return reverse("accounts:profile", kwargs={"pk": self.pk})