from nturl2path import url2pathname
from django.contrib import admin
from django.urls import path, include
from .views import SucursalDetail, SucursalesList

urlpatterns = [
    path('all', SucursalesList.as_view(template_name="sucursales/index.html"), name="sucursales"),
    path('prestamos/<int:pk>', SucursalDetail.as_view()),

]
