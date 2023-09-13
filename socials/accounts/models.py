from django.db import models
from django.contrib import auth
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User

UserModel = get_user_model()


class Followers(models.Model):
    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
        related_name="followers"
    )
    follower = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
        related_name="following"
    )

    class Meta:
        verbose_name_plural = 'Followers'