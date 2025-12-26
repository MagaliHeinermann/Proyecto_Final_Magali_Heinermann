from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout as django_logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm

# Importaciones locales
from .models import Empleado, Producto, Cliente, Avatar
from .forms import EmpleadoForm, ProductoForm, ClienteForm, AvatarForm, RegistroForm

# ───────── INICIO Y GENERAL ─────────

def inicio(request):
    return render(request, 'inicio.html', {})

def acerca(request):
    return render(request, "acerca.html")

# ───────── EMPLEADOS ─────────

@login_required
def lista_empleados(request):
    empleados = Empleado.objects.filter(usuario=request.user)
    return render(request, "empleados/lista_empleados.html", {"empleados": empleados})

@login_required
def crear_empleado(request):
    if request.method == "POST":
        form = EmpleadoForm(request.POST)
        if form.is_valid():
            empleado = form.save(commit=False)
            empleado.usuario = request.user
            empleado.save()
            return redirect("lista_empleados")
    else:
        form = EmpleadoForm()
    return render(request, "empleados/crear_empleado.html", {"form": form})

# ───────── PRODUCTOS ─────────

@login_required
def lista_productos(request):
    productos = Producto.objects.filter(usuario=request.user)
    return render(request, "productos/lista_productos.html", {"productos": productos})

@login_required
def crear_producto(request):
    if request.method == "POST":
        form = ProductoForm(request.POST)
        if form.is_valid():
            producto = form.save(commit=False)
            producto.usuario = request.user 
            producto.save()
            return redirect("lista_productos")
    else:
        form = ProductoForm()
    return render(request, "productos/crear_producto.html", {"form": form})

# ───────── CLIENTES ─────────

@login_required
def lista_clientes(request):
    clientes = Cliente.objects.filter(usuario=request.user)
    return render(request, "clientes/lista_clientes.html", {"clientes": clientes})

@login_required
def crear_cliente(request):
    if request.method == "POST":
        form = ClienteForm(request.POST)
        if form.is_valid():
            cliente = form.save(commit=False)
            cliente.usuario = request.user 
            cliente.save()
            return redirect("lista_clientes")
    else:
        form = ClienteForm()
    return render(request, "clientes/crear_cliente.html", {"form": form})

# ───────── BÚSQUEDA ─────────

@login_required
def buscar(request):
    query = request.GET.get("q", "")
    if query:
        # Filtramos productos que contengan el texto Y que pertenezcan al usuario actual
        productos = Producto.objects.filter(nombre__icontains=query, usuario=request.user)
    else:
        productos = []
    return render(request, "buscar.html", {"productos": productos, "query": query})

# ───────── AUTENTICACIÓN Y PERFIL ─────────

def registro(request):
    if request.method == "POST":
        form = RegistroForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Guardamos datos adicionales del formulario personalizado
            user.first_name = form.cleaned_data.get('first_name')
            user.last_name = form.cleaned_data.get('last_name')
            user.email = form.cleaned_data.get('email')
            user.save()
            login(request, user)
            return redirect("inicio")
    else:
        form = RegistroForm()
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
    return render(request, "registration/login.html", {"form": form})

def logout_manual(request):
    django_logout(request)
    return redirect('inicio')

@login_required
def agregar_avatar(request):
    if request.method == "POST":
        form = AvatarForm(request.POST, request.FILES)
        if form.is_valid():
            # Borramos avatar anterior para que no se acumulen
            Avatar.objects.filter(user=request.user).delete()
            avatar = form.save(commit=False)
            avatar.user = request.user
            avatar.save()
            return redirect("inicio")
    else:
        form = AvatarForm()
    return render(request, "agregar_avatar.html", {"form": form})

def acerca(request):
    return render(request, "acerca.html")