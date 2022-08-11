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
    videoall = Video_Files.objects.all()
    return render(request, "home.html", context={"videoall": videoall})


# SIGN UP FUNCTION


def SignUpView(request):
    if request.method == "POST":
        Full_Name = request.POST['userfullname']
        Email = request.POST['emailaddress']
        Password = request.POST['password']
        new_user = User_Main(Full_Name=Full_Name,
                             Email=Email, Password=Password)
        new_user.save()
        return redirect("Validation")
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


# LOGOUT FUNCTION


def Logout_user(request):
    logout(request)
    messages.success(request, "LOGOUT successful.")
    return redirect('Login')

# WATCH FUNCTION


def Watch(request):
    return render(request=request, template_name="watchpage.html")


# def New_Signup(request):
#     return render(request=request, template_name="signup2.html")


# VALIDATION IMAGES FUNCTION

def Validate_id(request):
    data = Validation.objects.all()
    form = ValidateForm(request.POST, request.FILES)
    if form.is_valid():
        form.save()
        return redirect('Login')
        messages.success(
            request, "ID pictures Uploaded, Proceed to Login Now")
    else:
        form = ValidateForm()
    return render(request, "validateid.html", context={"ValidateForm": form})


# VALIDATION 2 SCHOOL ID AND EMAIL
def Validation2(request):
    form = ValidateForm2(request.POST, request.FILES)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            messages.success(request, "School Email Submitted.")
            return redirect("Validate")

    return render(request=request, template_name="validation2.html", context={"validation2_form": form})
    # return render(request, "validation2.html")

# VIDEO UPLOAD FUNCTION


@csrf_exempt
@login_required(login_url='Login')
def Video_Upload(request):
    form = VideoForm(request.POST, request.FILES)
    videoall = Video_Files.objects.all()
    if request.method == "POST":
        if form.is_valid():
            form.save()
            messages.success(request, "Upload successful.")
            return redirect("Home")
    else:
        # form = VideoForm()
        print("done")
    return render(request=request, template_name=("video.html"), context={"video_form": form})

    # def _upload_file_view(request):


# Library function below

def Library(request):
    videoall = Video_Files.objects.all()
    return render(request, "library.html", context={"videoall": videoall})
