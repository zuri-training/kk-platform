from django.shortcuts import render
from django.views.generic.list import ListView
from .models import User

# Create your views here.


class UserList(ListView):

    # specify the model for list view
    model = User

def home(request):
    return render(request, 'userapp/home.html')

def login(request):
    return render(request, 'authentication/login.html')

def signup(request):
    return render(request, 'authentication/signup.html')