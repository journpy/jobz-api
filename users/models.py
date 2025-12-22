from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from .managers import CustomUserManager
import uuid


class CustomUser(AbstractBaseUser, PermissionsMixin):
    """A custom user."""
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, unique=True)
    email = models.EmailField(_("email address"), unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)
    email_verified = models.BooleanField(default=False)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    class Meta:
        ordering = ['-date_joined']

    def __str__(self):
        """String representation of Custom User object."""
        return self.email
