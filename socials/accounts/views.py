from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth import login, logout
from django.views.generic import CreateView

from . import forms

class SignUp(CreateView):
    formClass = forms.UserCreateForm
    success_url = reverse_lazy("login")
    template_name = "accounts/signup.html"
