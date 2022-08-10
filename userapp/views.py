from ast import Return
from django.shortcuts import render
from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from .models import *
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
        print('The form is POST')
        Full_Name = request.POST['userfullname']
        Email = request.POST['emailaddress']
        Password = request.POST['password']
        new_user = User_Main(Full_Name=Full_Name,
                             Email=Email, Password=Password)
        new_user.save()
        return redirect("Home")
    return render(request=request, template_name="signup2.html")


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


def Watch(request):
    return render(request=request, template_name="watchpage.html")


# def New_Signup(request):
#     return render(request=request, template_name="signup2.html")
