from django.shortcuts import render, redirect
from .models import Empleado, Producto, Cliente
from .forms import EmpleadoForm, ProductoForm, ClienteForm

# ───────── EMPLEADOS ─────────

def crear_empleado(request):
    if request.method == "POST":
        form = EmpleadoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("lista_empleados")
    else:
        form = EmpleadoForm()
    return render(request, "empleados/crear_empleado.html", {"form": form})

def lista_empleados(request):
    empleados = Empleado.objects.all()
    return render(request, "empleados/lista_empleados.html", {"empleados": empleados})

# ───────── PRODUCTOS ─────────

def crear_producto(request):
    if request.method == "POST":
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("lista_productos")
    else:
        form = ProductoForm()
    return render(request, "productos/crear_producto.html", {"form": form})

def lista_productos(request):
    productos = Producto.objects.all()
    return render(request, "productos/lista_productos.html", {"productos": productos})

# ───────── CLIENTES ─────────

def crear_cliente(request):
    if request.method == "POST":
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("lista_clientes")
    else:
        form = ClienteForm()
    return render(request, "clientes/crear_cliente.html", {"form": form})

def lista_clientes(request):
    clientes = Cliente.objects.all()
    return render(request, "clientes/lista_clientes.html", {"clientes": clientes})

# ───────── BÚSQUEDA ─────────

def buscar(request):
    query = request.GET.get("q", "")
    productos = Producto.objects.filter(nombre__icontains=query) if query else []
    return render(request, "buscar.html", {"productos": productos, "query": query})
