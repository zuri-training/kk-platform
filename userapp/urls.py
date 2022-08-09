from django.urls import path
from . import views

# importing views from views..py

urlpatterns = [
    # path('About/', views.About, name='About'),
    path('', views.Home, name='Home'),
    path("Signup/", views.SignUpView, name='Signup'),
    path("Comment/", views.Comment, name='Comment'),
    path("Video/", views.Video, name='Video'),
    path("Login/", views.Login_page, name='Login'),
    path("membersarea/", views.Memberarea, name='Membersarea'),
    path("logout/", views.Logout_user, name='Logout'),

]
