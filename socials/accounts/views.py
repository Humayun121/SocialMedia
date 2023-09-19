from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth import get_user_model
from . import forms
from django.shortcuts import render

from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Followers


class SignUp(CreateView):
    form_class = forms.UserCreateForm
    success_url = reverse_lazy("login")
    template_name = "accounts/signup.html"


UserModel = get_user_model()


# Follow
@login_required
def follow_user(request, user_id):

    person_to_follow = get_object_or_404(UserModel, id=user_id)
    print(person_to_follow)
    follower_instance, created = Followers.objects.get_or_create(
        user=person_to_follow,
        follower=request.user
    )
    print(follower_instance)
    print(created)  

    return redirect("posts:allPost")


# Unfollow
@login_required
def unfollow_user(request, user_id):
    person_to_unfollow = get_object_or_404(UserModel, id=user_id)
    request.user.followers.delete(person_to_unfollow)
    return redirect("posts:allPost")
