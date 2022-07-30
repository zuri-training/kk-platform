from django.shortcuts import render
from django.views.generic.list import ListView
from .models import User

# Create your views here.


class UserList(ListView):

    # specify the model for list view
    model = User
