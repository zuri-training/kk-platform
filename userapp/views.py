from django. views. decorators. csrf import csrf_exempt
from django.shortcuts import render
from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from .models import *
from django.http import JsonResponse
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from .forms import NewUserForm, CommentForm, LoginForm
# Create your views here.
from django.contrib.auth.forms import UserCreationForm
# from djangoUpload.forms import UploadForm
from django.contrib.auth.decorators import login_required
from django. views. decorators. csrf import csrf_exempt


def Home(request):
    return render(request, "home.html")

 # EMAIL CONFIRMATION FUNCTION


# def ActivateEmail(request, user, to_email):
#     messages.success(request, f'Dear {user}, please go to you email {to_email} inbox and click on \
#     received activation link to confirm and complete the registration. Note: Check your spam folder.')

# SIGNUP FUNCTION


def SignUpView(request):
    form = NewUserForm(request.POST)
    if request.method == "POST":
        print('This is a POST document')
    if form.is_valid():
        pwd = request.POST.get('Password', 'None')
        pwd2 = request.POST.get('Password2', 'None')
        if pwd != pwd2:
            messages.error(request, 'PASSWORDS ENTERED ARE NOT SAME')
            return redirect("Signup")
        else:
            form.save()
            User.is_active = False
            # login(request, User)
            # return redirect("Validate")
            # ActivateEmail(request, User, form.cleaned_data.get('email'))
            return redirect('EmailPage')  # enter link to validate email
    else:
        # return render(request, "signup.html")
        return render(request=request, template_name="signup.html", context={"signup_form": form})


# COMMENT FUNCTION
@login_required(login_url='Login')
def Comment(request):

    if request.method == "POST":
        print('This is a POST document')

    form = CommentForm(request.POST or None)
    if form.is_valid():
        Comment = form.save()
        messages.success(request, "Comment successful.")
        return redirect("Home")
        messages.error(
            request, "Unsuccessful Commenting.")
    return render(request=request, template_name="comment.html", context={"comment_form": form})


# EMAIL REDIRECTION FUNCTON PAGE
@csrf_exempt
def emailPage(request):
    return render(request, "email.html")


@login_required(login_url='Login')
def Video(request):
    if request.method == "POST":
        print('This is a POST document')
    form = VideoForm(request.POST or None)
    if form.is_valid():
        Video = form.save()
        messages.success(request, "Upload successful.")
        return redirect("Home")

    return render(request=request, template_name="video.html", context={"video_form": form})


@csrf_exempt
def Login_page(request):
    form = LoginForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            Username = request.POST.get('User_name')
            Password = request.POST.get('Password')
            user = authenticate(
                request, username=Username, password=Password)
            if request.user.is_authenticated:
                Login = form.save()
                login(request, user)
                return redirect("Membersarea")
            else:
                messages.error(
                    request, "Login Unsuccessful: Enter Correct Details.")
                return redirect("Login")
        else:
            messages.error(
                request, "Login Unsuccessful: Form Is Invalid. [Try Confirming Your Email Address")
            return redirect("Login")
    return render(request=request, template_name="login.html", context={"login_form": form})


# MEMBERS AREA FUNCTION
@login_required(login_url='Login')
def Memberarea(request):
    return render(request, "membersarea.html")

# LOGOUT FUNCTION


def Logout_user(request):
    logout(request)
    messages.success(request, "LOGOUT successful.")
    return redirect('Login')
