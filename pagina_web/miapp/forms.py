from django import forms
from .models import Empleado, Producto, Cliente

class EmpleadoForm(forms.ModelForm):
    class Meta:
        model = Empleado
        fields = "__all__"

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = "__all__"

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = "__all__"

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Avatar

class RegistroUsuarioForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]


class AvatarForm(forms.ModelForm):
    class Meta:
        model = Avatar
        fields = ["imagen"]