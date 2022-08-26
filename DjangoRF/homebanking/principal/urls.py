from re import M
from django.urls import path
from django.contrib.auth.views import logout_then_login
from .views import index, DatosCliente, DireccionCliente

urlpatterns = [
    path('', index, name='index'),
    path('logout/', logout_then_login, name='logout'),
    path('datos', DatosCliente.as_view()),
    path('editarDireccion/<int:pk>', DireccionCliente.as_view()),

]