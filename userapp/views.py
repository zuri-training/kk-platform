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
from .forms import *
# Create your views here.
from django.contrib.auth.forms import UserCreationForm
# from djangoUpload.forms import UploadForm
from django.contrib.auth.decorators import login_required
from django. views. decorators. csrf import csrf_exempt


class UserList(ListView):
    # specify the model for list view
    model = User

# HOME FUNCTION


@login_required(login_url='Login')
def Home(request):
    return render(request, "home.html")

# SIGN UP FUNCTION


def SignUpView(request):
    if request.method == "POST":
        login(request, user)
        Full_Name = request.POST['userfullname']
        Email = request.POST['emailaddress']
        Password = request.POST['password']
        new_user = User_Main(Full_Name=Full_Name,
                             Email=Email, Password=Password)
        new_user.save()
        return redirect("Home")
    return render(request=request, template_name="signup2.html")


# LOGIN FUNCTION
@csrf_exempt
def Login_page(request):
    form = LoginForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            Email = request.POST.get('Email')
            Password = request.POST.get('Password')
            user = authenticate(
                request, email=Email, password=Password)
            if request.user.is_authenticated:
                form.save()
                login(request, user)
                return redirect("Home")
            else:
                messages.error(
                    request, "Login Unsuccessful: Enter Correct Details.")
                return redirect("Login")
        else:
            messages.error(
                request, "Login Unsuccessful: Form Is Invalid. [Try Confirming Your Email Address")
            return redirect("Login")
    return render(request=request, template_name="login.html", context={"login_form": form})


# def Login_user(request):
#     if request.method == "POST":
#         print('This is a POST document')
#     form = LoginForm(request.POST or None)
#     if form.is_valid():
#         form.save()
#         messages.success(request, "Login successful.")
#         return redirect("Home")
#     messages.error(
#         request, "Login Failed")
#     return render(request=request, template_name="login.html", context={"login_form": form})


def Watch(request):
    return render(request=request, template_name="watchpage.html")


# def New_Signup(request):
#     return render(request=request, template_name="signup2.html")
