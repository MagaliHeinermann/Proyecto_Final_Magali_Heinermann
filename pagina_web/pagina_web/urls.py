"""
URL configuration for pagina_web project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# pagina_web/urls.py

from django.contrib import admin
from django.urls import path, include

# --- ÚNICA IMPORTACIÓN DE VISTAS REQUERIDA ---
# Importamos las vistas desde el módulo de tu aplicación 'MiApp'
from miapp import views as MiApp_views 

urlpatterns = [
    # Ruta de Inicio (Solución 404)
    path('', MiApp_views.inicio, name='inicio'), 

    # Admin
    path('admin/', admin.site.urls),
    
    # Rutas de tu aplicación MiApp
    path('empleados/crear/', MiApp_views.crear_empleado, name='crear_empleado'),
    path('empleados/lista/', MiApp_views.lista_empleados, name='lista_empleados'),
    path('productos/crear/', MiApp_views.crear_producto, name='crear_producto'),
    path('productos/lista/', MiApp_views.lista_productos, name='lista_productos'),
    path('clientes/crear/', MiApp_views.crear_cliente, name='crear_cliente'),
    path('clientes/lista/', MiApp_views.lista_clientes, name='lista_clientes'),
    path('buscar/', MiApp_views.buscar, name='buscar'),
]