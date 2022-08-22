from django.urls import path
from django.contrib.auth.views import logout_then_login
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('logout/', logout_then_login, name='logout'),
]