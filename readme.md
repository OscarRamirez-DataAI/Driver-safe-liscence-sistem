
DriveSafe
Sistema de gestión de prácticas de conducción
README del proyecto
Aplicación en Python · Consola · Persistencia local JSON/TXT


Academia DriveSafe

 1. Descripción del proyecto
DriveSafe es una aplicación desarrollada en Python para apoyar la administración de una academia de conducción que ofrece cursos prácticos y teóricos para motocicletas y automóviles. El proyecto busca reemplazar la asignación manual de citas por un sistema organizado desde consola.
La aplicación permite registrar clientes, instructores y vehículos, programar citas, controlar asistencia y guardar observaciones de cada práctica. La información se conserva en archivos locales, por ejemplo JSON o TXT, por lo que los datos pueden recuperarse después de cerrar y volver a ejecutar el programa.
2. Objetivo general
Desarrollar un sistema de gestión sencillo y modular para organizar las prácticas de conducción de la academia DriveSafe, evitando cruces de horarios y mejorando el control de clientes, instructores, vehículos y citas.
3. Objetivos específicos
1. Registrar y consultar clientes con nombre, documento y tipo de vehículo.
2. Administrar instructores y vehículos disponibles.
3. Programar citas asociando cliente, instructor, vehículo, fecha, hora y duración.
4. Controlar asistencia y observaciones de cada práctica.
5. Consultar el historial de prácticas de un cliente.
6. Guardar y cargar la información mediante archivos locales.
4. Funcionalidades principales
•	Registrar clientes y validar que el documento no esté repetido.
•	Registrar instructores con especialidad en moto o carro.
•	Registrar vehículos con tipo, placa y estado de disponibilidad.
•	Programar citas de práctica.
•	Consultar citas y filtrarlas por cliente o fecha.
•	Registrar asistencia y observaciones de una cita existente.
•	Consultar el historial de prácticas de cada cliente.
•	Guardar y recuperar datos desde archivos JSON o TXT.
5. Gestión de clientes
Cada cliente debe contar, como mínimo, con los siguientes datos:
•	Nombre completo.
•	Número de documento.
•	Tipo de vehículo: moto o carro.
El documento funciona como identificador único. Por esta razón, el sistema debe comprobar que no exista otro cliente con el mismo documento antes de guardar el registro.
Nombre: Juan Pérez
Documento: 1020304050
Tipo de vehículo: carro
6. Gestión de instructores
Los instructores se registran indicando su información básica y su especialidad. La especialidad define qué tipo de práctica puede dirigir cada instructor.
•	moto
•	carro
Al programar una cita, la especialidad del instructor debe ser compatible con el tipo de vehículo solicitado por el cliente.
7. Gestión de vehículos
Cada vehículo puede manejar los siguientes campos:
•	Tipo de vehículo.
•	Placa.
•	Disponibilidad.
Tipo: carro
Placa: ABC123
Disponible: Sí
La placa debe ser única y la disponibilidad ayuda a impedir que el mismo vehículo sea utilizado en dos prácticas que se crucen en el horario.
8. Programación de citas
Una cita representa una práctica de conducción. Cada cita debe relacionar:
•	Cliente.
•	Instructor.
•	Vehículo.
•	Fecha.
•	Hora.
•	Duración.
Antes de guardar una cita, el sistema debe realizar validaciones como:
•	Verificar que el cliente, instructor y vehículo existan.
•	Validar el formato y la lógica de la fecha y la hora.
•	Comprobar que instructor y vehículo estén disponibles.
•	Comprobar que la especialidad del instructor coincida con el tipo de práctica.
•	Evitar duplicados o cruces de horario.
9. Asistencia y observaciones
Después de realizar una práctica, una cita puede actualizarse para indicar si el cliente asistió y para guardar observaciones del instructor. Esto permite conservar información útil sobre el avance del estudiante.
Asistencia: Sí
Observaciones: Buen control del vehículo. Debe mejorar el estacionamiento.
10. Historial de prácticas
El sistema permite buscar un cliente por su documento y consultar las prácticas asociadas a ese registro. El historial puede incluir fecha, hora, instructor, vehículo, asistencia y observaciones.
Cliente: Juan Pérez
Fecha: 15/09/2026
Hora: 10:00
Instructor: Carlos Gómez
Vehículo: ABC123
Asistencia: Sí
Observaciones: Buen manejo general.
11. Persistencia de datos
La persistencia significa que la información permanece almacenada aunque el programa se cierre. DriveSafe utiliza archivos locales en lugar de una base de datos.
Una organización posible de los archivos es:
datos/
├── clientes.json
├── instructores.json
├── vehiculos.json
└── citas.json
Ejemplo de un cliente almacenado en JSON:
{
    "nombre": "Juan Pérez",
    "documento": "1020304050",
    "tipo_vehiculo": "carro"
}
12. Estructura modular del proyecto
El programa se divide en varios módulos. La modularización separa responsabilidades y facilita leer, probar y mantener el código.
DriveSafe/
├── main.py
├── menu_principal.py
├── clientes.py
├── instructores.py
├── vehiculos.py
├── citas.py
└── datos/
    ├── clientes.json
    ├── instructores.json
    ├── vehiculos.json
    └── citas.json
Archivo	Responsabilidad
main.py	Punto de entrada del programa. Inicia el menú principal.
menu_principal.py	Muestra las opciones al usuario y dirige la ejecución.
clientes.py	Registro, consulta y validación de clientes.
instructores.py	Registro y consulta de instructores y especialidades.
vehiculos.py	Registro y control de vehículos y disponibilidad.
citas.py	Programación, consulta, asistencia, observaciones e historial.
13. Archivo principal
En la versión actual compartida, el archivo principal importa la función menu desde el módulo menu_principal y luego la ejecuta. Esto indica que el menú está separado del punto de entrada del programa.
from menu_principal import menu

menu()
14. Menú por consola
Un menú posible para la aplicación puede verse así:
=================================
       DRIVESAFE - ACADEMIA
=================================

1. Registrar cliente
2. Consultar clientes
3. Registrar instructor
4. Registrar vehículo
5. Programar cita
6. Consultar citas
7. Registrar asistencia
8. Consultar historial
9. Salir

Seleccione una opción:
15. Requisitos técnicos
•	Python 3.
•	Aplicación ejecutada desde consola o terminal.
•	Estructura modular con mínimo tres archivos.
•	Persistencia mediante JSON o TXT.
•	Validaciones básicas de datos y disponibilidad.
•	No se requiere una base de datos.
Se pueden utilizar módulos de la biblioteca estándar de Python, por ejemplo:
import json
from datetime import datetime
16. Ejecución del programa
1. Ubicar todos los archivos del proyecto en una misma carpeta, respetando la estructura de módulos.
2. Abrir una terminal dentro de la carpeta del proyecto.
3. Ejecutar el archivo principal.
4. Usar el menú mostrado en consola para seleccionar las opciones.
python main.py
En algunos sistemas también puede utilizarse:
python3 main.py
17. Validaciones importantes
•	Documento de cliente único.
•	Placa de vehículo única.
•	Fecha y hora válidas.
•	Existencia del cliente, instructor y vehículo antes de crear la cita.
•	Compatibilidad entre especialidad del instructor y tipo de vehículo.
•	Disponibilidad del instructor y del vehículo.
•	Validación de las opciones del menú y manejo de entradas incorrectas.
Estas validaciones ayudan a mantener la integridad de los datos, es decir, evitan información duplicada, incoherente o imposible de procesar correctamente.
18. Conceptos técnicos utilizados
Modularización: Separación del programa en archivos con responsabilidades específicas.
Funciones: Bloques reutilizables que realizan operaciones concretas.
Persistencia: Almacenamiento de datos para conservarlos entre ejecuciones.
Validación: Comprobación de que los datos ingresados cumplen ciertas reglas.
Manejo de archivos: Lectura y escritura de información en JSON o TXT.
Manejo de excepciones: Uso de try y except para evitar cierres inesperados por entradas inválidas.
Ejemplo de manejo de excepciones:
try:
    opcion = int(input("Seleccione una opción: "))
except ValueError:
    print("Debe ingresar un número.")
19. Flujo general del sistema
Usuario
   ↓
Menú principal
   ↓
Selecciona una opción
   ↓
El programa solicita información
   ↓
Se realizan validaciones
   ↓
Se procesa la operación
   ↓
Se actualizan los archivos
   ↓
Se muestra el resultado al usuario
20. Posibles mejoras futuras
•	Interfaz gráfica.
•	Base de datos.
•	Inicio de sesión para administradores.
•	Control de pagos.
•	Reportes y estadísticas.
•	Calendario visual.
•	Recordatorios de citas.
•	Versión web del sistema.
21. Conclusión
DriveSafe es una solución sencilla para organizar prácticas de conducción utilizando Python. El sistema centraliza el registro de clientes, instructores, vehículos y citas, y permite realizar seguimiento mediante asistencia, observaciones e historial. La combinación de modularización, validaciones y persistencia en archivos locales permite construir una aplicación clara, funcional y apropiada para un proyecto academico
