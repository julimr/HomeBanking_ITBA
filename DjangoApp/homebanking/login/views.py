from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def index(request):
  template = loader.get_template('login/login-page.html')
  return HttpResponse(template.render())

def recuperarClave(request):
  template = loader.get_template('login/forgot.html')
  return HttpResponse(template.render({}, request))

def registrarse(request):
  template = loader.get_template('login/register-page.html')
  return HttpResponse(template.render({}, request))
