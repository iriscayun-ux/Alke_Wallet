from django import forms
from .models import Cuenta, Transaccion


# 🔹 FORMULARIO CUENTA
class CuentaForm(forms.ModelForm):
    class Meta:
        model = Cuenta
        fields = ['saldo']  # NO incluir cliente


# 🔹 FORMULARIO TRANSACCIÓN
class TransaccionForm(forms.ModelForm):
    class Meta:
        model = Transaccion
        fields = ['cuenta', 'tipo', 'monto']

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)

        if user:
            self.fields['cuenta'].queryset = Cuenta.objects.filter(
                cliente__usuario=user
            )