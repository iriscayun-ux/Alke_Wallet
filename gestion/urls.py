from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_cuentas, name='lista_cuentas'),
]
urlpatterns = [
    path('', views.lista_cuentas, name='lista_cuentas'),
    path('crear/', views.crear_cuenta, name='crear_cuenta'),
    path('editar/<int:id>/', views.editar_cuenta, name='editar_cuenta'),
    path('eliminar/<int:id>/', views.eliminar_cuenta, name='eliminar_cuenta'),
    path('transaccion/', views.crear_transaccion, name='crear_transaccion'),
    path('reporte/', views.reporte_transacciones, name='reporte'),
]