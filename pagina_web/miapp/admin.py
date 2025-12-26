from django.contrib import admin
from .models import Empleado, Producto, Cliente, Avatar # Eliminamos Mascota

admin.site.register(Empleado)
admin.site.register(Producto)
admin.site.register(Cliente)
admin.site.register(Avatar)