from django.urls import path, include
from miapp import views as MiApp_views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('acerca/', views.acerca, name='acerca'), # Cambiado de 'acerca_de_mi' a 'acerca'
    path('empleados/lista/', views.lista_empleados, name='lista_empleados'),
    path('empleados/crear/', views.crear_empleado, name='crear_empleado'),
    path('productos/lista/', views.lista_productos, name='lista_productos'),
    path('productos/crear/', views.crear_producto, name='crear_producto'),
    path('clientes/lista/', views.lista_clientes, name='lista_clientes'),
    path('clientes/crear/', views.crear_cliente, name='crear_cliente'),
    path('buscar/', views.buscar, name='buscar'),
    path('registro/', views.registro, name='registro'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_manual, name='logout'),
    path('agregar-avatar/', views.agregar_avatar, name='agregar_avatar'),
]