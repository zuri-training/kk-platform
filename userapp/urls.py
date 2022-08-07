from django.contrib import admin
from django.urls import path,include


# importing views from views..py
from .views import UserList
urlpatterns = [
    path('', UserList.as_view()),
]
