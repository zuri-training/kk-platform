<<<<<<< HEAD
from django.contrib import admin
from django.urls import path,include

=======
from django.urls import path
from . import views
>>>>>>> e9306fbc86f310673ece35d1667501e9647e4afd

# importing views from views..py

urlpatterns = [
    path('', views.Home, name='Home'),
    path("Signup/", views.SignUpView, name='Signup'),
    path("Login/", views.Login, name='Login'),
]
