from ast import Return
from django.shortcuts import render
from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from .models import User
from django.http import JsonResponse
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from .forms import NewUserForm, LoginForm
# Create your views here.
from django.contrib.auth.forms import UserCreationForm
# from djangoUpload.forms import UploadForm


class UserList(ListView):
    # specify the model for list view
    model = User

# HOME FUNCTION


def Home(request):
    return render(request, "home.html")

# SIGN UP FUNCTION


def SignUpView(request):
    if request.method == "POST":
        print('This is a POST document')
    form = NewUserForm(request.POST)
    if form.is_valid():
        User = form.save()
        messages.success(request, "Registration successful.")
        return redirect("Home")
    messages.error(
        request, "Unsuccessful registration. Invalid information.")
    return render(request=request, template_name="signup.html", context={"signup_form": form})

# LOGIN FUNCTION


def Login(request):
    if request.method == "POST":
        print('This is a POST document')
    form = LoginForm(request.POST or None)
    if form.is_valid():
        Login = form.save()
        messages.success(request, "Login successful.")
        return redirect("Home")
    messages.error(
        request, "Login Failed")
    return render(request=request, template_name="login.html", context={"login_form": form})

#WATCH MOVIES FUNCTION

def Watch(request):
    return render(request=request, template_name="watchpage.html")