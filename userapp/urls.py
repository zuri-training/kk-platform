from django.urls import path
from . import views

# importing views from views..py

urlpatterns = [
    path('', views.Home, name='Home'),
    path("Signup/", views.SignUpView, name='Signup'),
    path("Login/", views.Login, name='Login'),
    path("WatchMovie/", views.Watch, name='WatchMovie')
]   
