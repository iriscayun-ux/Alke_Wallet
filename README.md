 Proyecto Alke Wallet

Descripción del Proyecto
Alke Wallet es una aplicación web desarrollada con Django que simula una billetera digital. Permite a los usuarios autenticados crear y gestionar sus propias cuentas, realizar transacciones (depósitos y retiros) y consultar sus saldos de forma segura.

El sistema implementa control de acceso por usuario, asegurando que cada persona solo pueda ver y operar sobre sus propios datos.

Objetivo
Desarrollar una aplicación web funcional que permita:
•	Gestionar cuentas digitales
•	Realizar transacciones
•	Mantener la seguridad de los datos por usuario
•	Aplicar buenas prácticas con Django (ORM, migraciones, autenticación)

 Tecnologías 
•	Python 3
•	Django
•	SQLite (base de datos)
•	Bootstrap 5 (interfaz gráfica)
•	HTML
•	Git & GitHub

 ¿Cómo funciona el sistema?
La aplicación está basada en tres modelos principales:

 Usuario (User)
Sistema de autenticación de Django.
•	Permite iniciar sesión (login)
•	Permite cerrar sesión (logout)

Cliente
Representa la información adicional del usuario.
•	Relación: 1 a 1 con User
•	Contiene datos como teléfono y dirección

Cuenta
Representa una billetera digital.
•	Cada cuenta pertenece a un cliente
•	Un cliente puede tener varias cuentas
•	Contiene saldo y fecha de creación

Transacción
Representa movimientos de dinero.
•	Depósito → suma saldo
•	Retiro → resta saldo (con validación)
•	Cada transacción está asociada a una cuenta

 Seguridad Implementada
El sistema cuenta con control de acceso por usuario:
•	Cada usuario solo puede ver sus propias cuentas
•	No puede editar ni eliminar cuentas de otros
•	No puede realizar transacciones en cuentas ajenas
•	Los formularios están filtrados por usuario autenticado

Ejemplo de implementación:
Cuenta.objects.filter(cliente__usuario=request.user)
Esto garantiza la privacidad y seguridad de los datos.

Funcionalidades (CRUD)
Listar cuentas
Muestra únicamente las cuentas del usuario logueado.

Crear cuenta
Permite crear una nueva cuenta asociada automáticamente al usuario. El sistema asigna un identificador único, vincula la cuenta al cliente correspondiente y registra el saldo inicial ingresado, junto con la fecha de creación, sin requerir intervención manual del usuario.”

Editar cuenta
Permite modificar una cuenta existente (solo si pertenece al usuario).

Eliminar cuenta
Permite eliminar cuentas propias.

Realizar transacciones
Permite:
•	Depositar dinero
•	Retirar dinero (validando saldo suficiente)
 	
Reporte de transacciones
Muestra todas las transacciones del usuario en orden descendente por fecha, para llevar un control de los movimientos.


Base de Datos
Se utilizó SQLite como base de datos.
Se gestionó mediante el ORM de Django:
•	Creación de modelos
•	Migraciones
•	Relaciones entre tablas

Migraciones
Se utilizaron los siguientes comandos:
python manage.py makemigrations
python manage.py migrate
Esto permitió sincronizar los modelos con la base de datos.

Interfaz de Usuario
Se utilizó Bootstrap para mejorar la experiencia:
•	Navbar con logo
•	Botones estilizados
•	Formularios centrados

Ejecución del Proyecto
1.	Activar entorno virtual:
venv\Scripts\activate
2.	Ejecutar migraciones:
python manage.py migrate
3.	Crear superusuario:
python manage.py createsuperuser
4.	Ejecutar servidor:
python manage.py runserver
5.	Acceder:
http://127.0.0.1:8000/

Pruebas realizadas
•	Creación de múltiples usuarios
•	Creación de cuentas por usuario
•	Validación de acceso restringido
•	Pruebas de depósitos y retiros
•	Verificación de seguridad entre usuarios

Conclusión
El proyecto Alke Wallet permite aplicar:
•	ORM de Django
•	Relaciones entre modelos
•	Operaciones CRUD
•	Seguridad y control de acceso
•	Integración de frontend con Bootstrap
Se logró construir una aplicación funcional, segura y escalable.




