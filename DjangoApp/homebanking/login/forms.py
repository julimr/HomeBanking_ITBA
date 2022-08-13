from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import User

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    password1: forms.Field = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2: forms.Field = forms.CharField(label='Confirmar contraseña', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        help_texts = {k:"" for k in fields}

class UserLoginForm(UserCreationForm):
    email = forms.EmailField()
    password1: forms.Field = forms.CharField(label='Contraseña', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1']
        help_texts = {k:"" for k in fields}