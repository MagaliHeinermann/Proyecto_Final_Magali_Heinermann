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
