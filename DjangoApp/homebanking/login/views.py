from typing import List
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from django.contrib import messages
from .forms import UserRegisterForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from login.models import Cliente, UserCliente

from django.contrib.auth.models import User

def recuperarClave(request):
  template = loader.get_template('login/forgot.html')
  return HttpResponse(template.render({}, request))

def registrarse(request):
  if request.method == 'POST':
    form = UserRegisterForm(request.POST)
    if form.is_valid():
      dni = form.cleaned_data.get('dni')
      cliente = Cliente.objects.filter(customer_dni = dni)
      for x in cliente:
        idCliente = x.customer_id
      if len(cliente) != 0:
        user : User = form.save()
        login(request, user)
        userCliente = UserCliente(id_user = user.pk , id_cliente = idCliente)
        userCliente.save()
        return redirect('index')
      else:
        messages.error(request, "No encontamos su DNI en la lista de clientes.")
        messages.error(request, "Debe ser cliente del banco para poder registrarse.")

  else:
    form = UserRegisterForm()
  
  context = {'form' : form}
  template = loader.get_template('login/register-page.html')
  return HttpResponse(template.render(context, request))

def iniciarSesion(request):
  if request.method == 'POST':
    form = AuthenticationForm(request, data=request.POST)
    if form.is_valid():
      username = form.cleaned_data.get('username')
      password = form.cleaned_data.get('password')
      user = authenticate(username=username, password=password)
      if user is not None:
          login(request, user)
          messages.info(request, f"You are now logged in as {username}.")
          return redirect('/homebanking')
      else:
        messages.error(request,"Invalid username or password.")
    else:
      messages.error(request,"Invalid username or password.")
  else:
    form  = AuthenticationForm()
  context = {'form' : form}
  template = loader.get_template('login/login-page.html')
  return HttpResponse(template.render(context, request))
