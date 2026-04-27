from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model


class User(AbstractUser):
    is_buyer = models.BooleanField(default=False)
    is_supplier = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)

User = get_user_model()   # now User is your custom model
