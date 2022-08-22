from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views

urlpatterns = [
    #path('', views.index, name='index'),
    path('recuperarClave/', views.recuperarClave, name='recuperarClave'),
    path('registrarse/', views.registrarse, name='registrarse'),
    # path('login/', LoginView.as_view(template_name="login/login-page.html"), name="login"),
    path('',views.iniciarSesion, name="login"),
]