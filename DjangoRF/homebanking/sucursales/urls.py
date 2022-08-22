from nturl2path import url2pathname
from django.contrib import admin
from django.urls import path, include
from .views import SucursalesList

urlpatterns = [
    path('all', SucursalesList.as_view(), name="sucursales"),
]
