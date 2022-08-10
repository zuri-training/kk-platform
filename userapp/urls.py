from django.urls import path
from . import views

# importing views from views..py

urlpatterns = [
    path('', views.Home, name='Home'),
    path("Signup/", views.SignUpView, name='Signup'),
    path("Login/", views.Login_page, name='Login'),
    path("WatchPage/", views.Watch, name='Watch-Page'),
    path("new_signup/", views.SignUpView, name='New-Signup-Page')
]
