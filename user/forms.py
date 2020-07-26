from django.contrib.auth.forms import UserCreationForm
from django.forms import forms
from .models import User


class SignupForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['username', 'password', 'email']
