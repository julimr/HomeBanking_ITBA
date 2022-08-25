from django.urls import path
from . import views
from .views import TarjetasClienteDetail

urlpatterns = [
    path('', views.index, name='index'),
    path('cliente/<int:pk>', TarjetasClienteDetail.as_view() ),
]