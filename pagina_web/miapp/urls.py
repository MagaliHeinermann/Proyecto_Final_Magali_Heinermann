from django.urls import path
from . import views

urlpatterns = [
    # Empleados
    path("empleados/crear/", views.crear_empleado, name="crear_empleado"),
    path("empleados/lista/", views.lista_empleados, name="lista_empleados"),

    # Productos
    path("productos/crear/", views.crear_producto, name="crear_producto"),
    path("productos/lista/", views.lista_productos, name="lista_productos"),

    # Clientes
    path("clientes/crear/", views.crear_cliente, name="crear_cliente"),
    path("clientes/lista/", views.lista_clientes, name="lista_clientes"),

    # Búsqueda
    path("buscar/", views.buscar, name="buscar"),
]
