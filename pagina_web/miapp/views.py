from django.shortcuts import render, redirect
from .models import Empleado, Producto, Cliente
from .forms import EmpleadoForm, ProductoForm, ClienteForm

# --- Vista de Inicio ---
def inicio(request):
    return render(request, 'inicio.html', {})

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

from django.contrib.auth.decorators import login_required

@login_required
def crear_cliente(request):
    ...


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

from django.contrib.auth.decorators import login_required

@login_required
def crear_cliente(request):
    ...


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

from django.contrib.auth.decorators import login_required

@login_required
def crear_cliente(request):
    ...


# ───────── BÚSQUEDA ─────────

def buscar(request):
    query = request.GET.get("q", "")
    productos = Producto.objects.filter(nombre__icontains=query) if query else []
    return render(request, "buscar.html", {"productos": productos, "query": query})

from django.contrib.auth.decorators import login_required

@login_required
def crear_cliente(request):
    ...


# ───────── REGISTRO ─────────

from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from .forms import RegistroUsuarioForm, AvatarForm
from .models import Avatar

def registro(request):
    if request.method == "POST":
        form = RegistroUsuarioForm(request.POST)
        if form.is_valid():
            usuario = form.save()
            login(request, usuario)
            return redirect("inicio")
    else:
        form = RegistroUsuarioForm()
    return render(request, "registro.html", {"form": form})


def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            usuario = form.get_user()
            login(request, usuario)
            return redirect("inicio")
    else:
        form = AuthenticationForm()
    return render(request, "login.html", {"form": form})


def logout_view(request):
    logout(request)
    return redirect("inicio")


@login_required
def agregar_avatar(request):
    avatar = Avatar.objects.filter(user=request.user).first()

    if request.method == "POST":
        form = AvatarForm(request.POST, request.FILES, instance=avatar)
        if form.is_valid():
            avatar = form.save(commit=False)
            avatar.user = request.user
            avatar.save()
            return redirect("inicio")
    else:
        form = AvatarForm(instance=avatar)

    return render(request, "avatar.html", {"form": form})

# Pagina "Acerca de mi"
def acerca_de_mi(request):
    return render(request, "acerca_de_mi.html")
