from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from django.contrib import messages
from .forms import UserRegisterForm

def index(request):
  template = loader.get_template('login/login-page.html')
  return HttpResponse(template.render())

def recuperarClave(request):
  template = loader.get_template('login/forgot.html')
  return HttpResponse(template.render({}, request))

def registrarse(request):
  if request.method == 'POST':
    form = UserRegisterForm(request.POST)
    if form.is_valid():
      username = form.cleaned_data['username']
      #messages.success(request, f'Usuario {username} creado')
      return redirect('')  #Acá iria la direccion del HB

  else:
    form = UserRegisterForm()
  
  context = {'form' : form}
  template = loader.get_template('login/register-page.html')
  return HttpResponse(template.render(context, request))
