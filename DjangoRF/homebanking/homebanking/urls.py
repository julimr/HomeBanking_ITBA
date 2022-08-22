from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('login.urls')),
    path('clientes/', include('clientes.urls')),
    path('prestamos/', include('prestamos.urls')),
    path('cuentas/', include('cuentas.urls')),
    path('tarjetas/', include('tarjetas.urls')),
    path('homebanking/', include('principal.urls')),
    path('sucursales/', include('sucursales.urls')),
]
