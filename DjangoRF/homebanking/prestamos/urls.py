from django.urls import path
from . import views
from .views import EliminarPrestamo, PrestamosCliente

urlpatterns = [
    path('', views.index, name='prestamos'),
    path('nuevo_prestamo/', views.prestamos, name='nuevo_prestamo'),
    path('cliente/<int:pk>', PrestamosCliente.as_view()),
    path('anular_prestamo/<int:pk>', EliminarPrestamo.as_view()),
]
