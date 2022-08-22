from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='prestamos'),
    path('nuevo_prestamo/', views.prestamos, name='nuevo_prestamo'),
]