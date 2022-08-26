from re import M
from django.urls import path
from django.contrib.auth.views import logout_then_login
from .views import index, DatosCliente, DireccionDetail

urlpatterns = [
    path('', index, name='index'),
    path('logout/', logout_then_login, name='logout'),
    path('datos', DatosCliente.as_view()),
    path('direcciones', DireccionDetail.as_view()),
    path('direcciones/<int:pk>', DireccionDetail.as_view()),

]