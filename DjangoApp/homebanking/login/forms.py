from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    password1: forms.Field = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2: forms.Field = forms.CharField(label='Confirmar contraseña', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        help_texts = {k:"" for k in fields}

# class UserLoginForm(AuthenticationForm):
#     username = forms.CharField()
#     password: forms.Field = forms.CharField(label='Contraseña', widget=forms.PasswordInput)

#     class Meta:
#         model = User
#         fields = ['username', 'password']
#         help_texts = {k:"" for k in fields}