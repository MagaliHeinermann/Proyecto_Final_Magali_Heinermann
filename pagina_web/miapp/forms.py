from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Avatar, Empleado, Producto, Cliente # <--- ASEGÚRATE DE ESTA LÍNEA

class RegistroForm(UserCreationForm):
    first_name = forms.CharField(label="Nombre", max_length=30)
    last_name = forms.CharField(label="Apellido", max_length=30)
    email = forms.EmailField(label="Correo electrónico")

    class Meta:
        model = User
        fields = ["username", "first_name", "last_name", "email"]

# Si tienes un AvatarForm abajo, ahora sí reconocerá 'Avatar'
class AvatarForm(forms.ModelForm):
    class Meta:
        model = Avatar
        fields = ['imagen']


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

class EmpleadoForm(forms.ModelForm):
    class Meta:
        model = Empleado
        fields = '__all__'

# modificacion de avatar

from django import forms
from .models import Avatar

class AvatarForm(forms.ModelForm):
    class Meta:
        model = Avatar
        fields = ['imagen']