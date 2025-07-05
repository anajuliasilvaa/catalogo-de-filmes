from django.shortcuts import render,redirect
from .admin import CustomUserCreationForm
from django.contrib import messages

def registro(request):
    form = CustomUserCreationForm

    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
