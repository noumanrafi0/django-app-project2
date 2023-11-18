from django.contrib.auth.models import AbstractUser
from django.db import models

from .manager import UserManager


class CustomUser(AbstractUser):
    username = None
    phone_number = models.CharField(max_length=100, unique=True)
    email = None
    user_bio = models.CharField(max_length=50, blank=True)
    # user_profile_image = models.ImageField(upload_to="profile")

    USERNAME_FIELD = "phone_number"
    REQUIRED_FIELDS = []
    objects = UserManager()

    def save(self, *args, **kwargs):
        self.user_bio = "This is a custom user"

        super().save(*args, **kwargs)
