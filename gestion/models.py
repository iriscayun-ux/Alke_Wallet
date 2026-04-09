from django.db import models
from django.contrib.auth.models import User

# CLIENTE
class Cliente(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    telefono = models.CharField(max_length=15)
    direccion = models.CharField(max_length=255)

    def __str__(self):
        return self.usuario.username


# CUENTA
class Cuenta(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    saldo = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Cuenta {self.id}"


# TRANSACCION
class Transaccion(models.Model):
    TIPO = [
        ('deposito', 'Depósito'),
        ('retiro', 'Retiro'),
    ]

    ESTADO = [
        ('exito', 'Realizada con éxito'),
        ('fallo', 'Fallida'),
    ]

    cuenta = models.ForeignKey(Cuenta, on_delete=models.CASCADE)
    tipo = models.CharField(max_length=10, choices=TIPO)
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    fecha = models.DateTimeField(auto_now_add=True)
    estado = models.CharField(max_length=10, choices=ESTADO, default='exito')

    def __str__(self):
        return f"{self.tipo} - {self.monto} - {self.estado}"