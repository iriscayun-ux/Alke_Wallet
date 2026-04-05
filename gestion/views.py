from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Cuenta, Cliente, Transaccion
from .forms import CuentaForm, TransaccionForm

#  LISTAR CUENTAS (SOLO DEL USUARIO)
@login_required
def lista_cuentas(request):
    cuentas = Cuenta.objects.filter(cliente__usuario=request.user)
    return render(request, 'cuentas/lista.html', {'cuentas': cuentas})

#  CREAR CUENTA (ASIGNADA AL CLIENTE DEL USUARIO)
@login_required
def crear_cuenta(request):
    cliente, created = Cliente.objects.get_or_create(usuario=request.user)

    if request.method == 'POST':
        form = CuentaForm(request.POST)
        if form.is_valid():
            cuenta = form.save(commit=False)
            cuenta.cliente = cliente  # asigna la cuenta al cliente actual
            cuenta.save()
            return redirect('lista_cuentas')
    else:
        form = CuentaForm()

    return render(request, 'cuentas/crear.html', {'form': form})

#  EDITAR CUENTA (SOLO SI ES DEL USUARIO)
@login_required
def editar_cuenta(request, id):
    cuenta = get_object_or_404(
        Cuenta,
        id=id,
        cliente__usuario=request.user
    )

    if request.method == 'POST':
        form = CuentaForm(request.POST, instance=cuenta)
        if form.is_valid():
            form.save()
            return redirect('lista_cuentas')
    else:
        form = CuentaForm(instance=cuenta)

    return render(request, 'cuentas/editar.html', {'form': form})

#  ELIMINAR CUENTA (SOLO SI ES DEL USUARIO)
@login_required
def eliminar_cuenta(request, id):
    cuenta = get_object_or_404(
        Cuenta,
        id=id,
        cliente__usuario=request.user
    )
    cuenta.delete()
    return redirect('lista_cuentas')

#  TRANSACCIONES (DEPÓSITO / RETIRO) 
@login_required
def crear_transaccion(request):
    if request.method == 'POST':
        form = TransaccionForm(request.POST, user=request.user)
        if form.is_valid():
            transaccion = form.save(commit=False)
            cuenta = transaccion.cuenta

            #  Validación: solo el dueño de la cuenta puede operar
            if cuenta.cliente.usuario != request.user:
                transaccion.estado = 'fallo'
                transaccion.save()
                return render(request, 'cuentas/error.html', {
                    'mensaje': 'No tienes permiso para esta cuenta'
                })

            #  Aplicar transacción y asignar estado
            if transaccion.tipo == 'deposito':
                cuenta.saldo += transaccion.monto
                transaccion.estado = 'exito'

            elif transaccion.tipo == 'retiro':
                if cuenta.saldo >= transaccion.monto:
                    cuenta.saldo -= transaccion.monto
                    transaccion.estado = 'exito'
                else:
                    transaccion.estado = 'fallo'
                    transaccion.save()
                    return render(request, 'cuentas/error.html', {
                        'mensaje': 'Saldo insuficiente'
                    })

            cuenta.save()
            transaccion.save()
            return redirect('lista_cuentas')
    else:
        form = TransaccionForm(user=request.user)

    return render(request, 'cuentas/transaccion.html', {'form': form})

#  REPORTE DE TRANSACCIONES (SOLO DEL USUARIO)
@login_required
def reporte_transacciones(request):
    transacciones = Transaccion.objects.filter(
        cuenta__cliente__usuario=request.user
    ).order_by('-fecha')

    return render(request, 'cuentas/reporte.html', {
        'transacciones': transacciones
    })