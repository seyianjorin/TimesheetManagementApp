from django import forms
from .models import Doctor
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class CreateUserForm(UserCreationForm):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    email = forms.CharField(required=True)

    class Meta:
        model = User
        fields = ['username','first_name', 'last_name', 'email', 'password1', 'password2']


class DoctorForm(forms.ModelForm):

    class Meta:

        model = Doctor

        fields = [
            "specialization",
            "departmentId",
            "is_Admin"
        ]
