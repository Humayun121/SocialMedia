from django.db import models
from django.contrib import auth
from django.contrib.auth import get_user_model

UserModel = get_user_model()


# Create your models here.
class User(auth.models.User, auth.models.PermissionsMixin):
    user_profile = models.OneToOneField(
        UserModel,
        related_name='profile',
        on_delete=models.CASCADE,
        default=None
    )
    followers = models.ManyToManyField(
        UserModel,
        related_name="following",
        blank=True)


    def __str__(self):
        return f"@{self.username}"
