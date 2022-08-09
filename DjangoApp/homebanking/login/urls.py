from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('recuperarClave/', views.recuperarClave, name='recuperarClave'),
    path('registrarse/', views.registrarse, name='registrarse'),
]