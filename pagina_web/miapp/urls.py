from django.urls import path
from miapp import views as MiApp_views

urlpatterns = [
    # Inicio
    path("", MiApp_views.inicio, name="inicio"),

    # Empleados
    path("empleados/crear/", MiApp_views.crear_empleado, name="crear_empleado"),
    path("empleados/lista/", MiApp_views.lista_empleados, name="lista_empleados"),

    # Productos
    path("productos/crear/", MiApp_views.crear_producto, name="crear_producto"),
    path("productos/lista/", MiApp_views.lista_productos, name="lista_productos"),

    # Clientes
    path("clientes/crear/", MiApp_views.crear_cliente, name="crear_cliente"),
    path("clientes/lista/", MiApp_views.lista_clientes, name="lista_clientes"),

    # Búsqueda
    path("buscar/", MiApp_views.buscar, name="buscar"),
]
