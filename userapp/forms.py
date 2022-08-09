from django import forms
from django.contrib.auth.models import User
from django.db import models
from django.forms import ModelForm
from .models import *

# SIGNUP FORM


class NewUserForm(forms.ModelForm):
    class Meta:
        model = User_Main
        fields = ("First_name", "Last_name", "User_name",
                  "Email", "College_name", "Department",
                  "Year_of_admission", "Year_of_graduation",
                  "Account_verification", "Password", "Password2")
        # "__all__"
        widgets = {
            'First_name': forms.TextInput(attrs={'class': 'form-control'}),
            'Last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'User_name': forms.TextInput(attrs={'class': 'form-control'}),
            'Email': forms.EmailInput(attrs={'class': 'form-control'}),
            'College_name': forms.TextInput(attrs={'class': 'form-control'}),
            'Department': forms.TextInput(attrs={'class': 'form-control'}),
            'Year_of_admission': forms.TextInput(attrs={'class': 'form-control'}),
            'Year_of_graduation': forms.TextInput(attrs={'class': 'form-control'}),
            'Account_verification': forms.TextInput(attrs={'class': 'form-control'}),
            'Account_suspension_status': forms.TextInput(attrs={'class': 'form-control'}),
            'User_tag': forms.TextInput(attrs={'class': 'form-control'}),
            'User_ID': forms.TextInput(attrs={'class': 'form-control'}),
            'Password': forms.PasswordInput(attrs={'class': 'form-control'}),
            'Password2': forms.PasswordInput(attrs={'class': 'form-control'}),

        }


# LOGIN FORM
class LoginForm(forms.ModelForm):
    class Meta:
        model = Login_page
        fields = widgets = {
            'User_name': forms.TextInput(attrs={'class': 'form-control'}),
            'Email': forms.TextInput(attrs={'class': 'form-control'}),
            'Password': forms.PasswordInput(attrs={'class': 'form-control'}),
        }
        # "__all__"


# COMMENT FORM


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ("Comments", "User_ID")
        # "__all__"
        widgets = {
            'Comments_ID': forms.TextInput(attrs={'class': 'form-control'}),
            'Comments': forms.TextInput(attrs={'class': 'form-control'}),
            'User_ID': forms.TextInput(attrs={'class': 'form-control'}),

        }
