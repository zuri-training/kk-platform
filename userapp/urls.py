from django.contrib import admin
from django.urls import path

# importing views from views..py

from . import views
from .views import UserList

urlpatterns = [
    # path('', UserList.as_view()),
    path('', views.home, name="home"),
    path('login/', views.login, name="login"),
    path('signup', views.signup, name="signup")
]
