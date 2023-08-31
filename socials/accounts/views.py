from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth import login, logout
from django.views.generic import CreateView

from . import forms


