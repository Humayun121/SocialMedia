from django.db import models
from django.contrib import auth
from django.contrib.auth import get_user_model

UserModel = get_user_model()


# Create your models here.
class User(auth.models.User, auth.models.PermissionsMixin):
    def __str__(self):
        return f"@{self.username}"


# Following
class UserFollowing(models.Model):
    user_id = models.ForeignKey(
        UserModel, related_name="following", on_delete=models.CASCADE
    )
    following_user_id = models.ForeignKey(
        UserModel,
        related_name="follwoing",
        on_delete=models.CASCADE,
    )
    created = models.DateTimeField(
        auto_now_add=True,
        db_index=True
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["user_id", "following_user_id"], name="unique_followers"
            )
        ]

        ordering = ["-created"]

    def __str__(self):
        f"{self.user_id} follows {self.following_user_id}"
