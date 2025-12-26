from django.db import models

class Empleado(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    puesto = models.CharField(max_length=50)
    sueldo = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class Producto(models.Model):
    nombre = models.CharField(max_length=50)
    categoria = models.CharField(max_length=50)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()

    def __str__(self):
        return self.nombre

class Cliente(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField(unique=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"
    
class Avatar(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to="avatares", null=True, blank=True)

    def __str__(self):
        return f"Avatar de {self.user.username}"
