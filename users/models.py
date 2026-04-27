from django.db import models
from django.contrib.auth.models import AbstractUser
<<<<<<< HEAD
from django.contrib.auth import get_user_model
=======
>>>>>>> 1074f0aa0d82a4919a3df8e7085d78470368cdc7


class User(AbstractUser):
    is_buyer = models.BooleanField(default=False)
    is_supplier = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
<<<<<<< HEAD

User = get_user_model()   # now User is your custom model
=======
>>>>>>> 1074f0aa0d82a4919a3df8e7085d78470368cdc7
