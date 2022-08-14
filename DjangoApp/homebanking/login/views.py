from typing import List
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from django.contrib import messages
from .forms import UserRegisterForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from login.models import Cliente, UserCliente

def recuperarClave(request):
  template = loader.get_template('login/forgot.html')
  return HttpResponse(template.render({}, request))

def registrarse(request):
  if request.method == 'POST':
    form = UserRegisterForm(request.POST)
    if form.is_valid():
      # username = form.cleaned_data['username']
      #messages.success(request, f'Usuario {username} creado')
      user = form.save()
      login(request, user)
      messages.success(request, "Registration successful." )
      return redirect('index')  #Acá iria la direccion del HB
    messages.error(request, "Unsuccessful registration. Invalid information.")

  else:
    form = UserRegisterForm()
  
  context = {'form' : form}
  template = loader.get_template('login/register-page.html')
  return HttpResponse(template.render(context, request))

# def registrarse(request):
#   if request.method == 'POST':
#     form = UserRegisterForm(request.POST)
#     if form.is_valid():
#       dni = form.cleaned_data.get('dni')
#       clientes = Cliente.objects.all().values().filter(customer_dni = dni)
#       cliente = clientes.filter(customer_dni = dni)
#       clienteid = cliente.first()['customer_id']
#       # clienteid = 1
#       # if len(clientes) != 0:
#         # user = form.save(commit=False)
#         # userCliente = UserCliente(id_user = 1, id_cliente = 1)
#         # userCliente.save()
#         # user = form.save()
#         # login(request, user)
#         # messages.success(request, "Registration successful." )
#       user = form.save()
#       login(request, user)
#       messages.success(request, "Registration successful." )
#       return redirect('index')  #Acá iria la direccion del HB
#     messages.error(request, "Unsuccessful registration. Invalid information.")

#   else:
#     form = UserRegisterForm()
  
#   context = {'form' : form}
#   template = loader.get_template('login/register-page.html')
#   return HttpResponse(template.render(context, request))
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
