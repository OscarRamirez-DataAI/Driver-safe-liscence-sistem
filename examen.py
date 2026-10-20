#Contexto
#La academia de conducción DriveSafe necesita organizar la disponibilidad de sus instructores para asignar clases de práctica a los estudiantes.

#Cada instructor tiene un nombre, una categoría de licencia (A, B o C) y un conjunto de días disponibles para dictar clases.

#El objetivo del examen es desarrollar un programa en Python que permita registrar instructores, consultar sus disponibilidades

# y actualizar los días en los que pueden dictar clases.


#Objetivo del examen
#Implementar un programa que:

#Permita registrar nuevos instructores con sus datos.
#Liste todos los instructores con sus días disponibles.
#Permita modificar la disponibilidad de un instructor existente.
#Guarde y cargue la información desde un archivo instructores.json.

#Requerimientos funcionales
#Registro de instructores
#Solicitar: nombre, categoría de licencia (A, B o C) y días disponibles (lista de días).
#Validar que la categoría esté dentro de A, B o C.
#Guardar los datos en instructores.json.
#Consulta de instructores
#Mostrar todos los instructores con formato:
#Nombre: Carlos López | Licencia: B | Días: Lunes, Miércoles, Viernes
#Si no hay registros, mostrar un mensaje adecuado.
#Actualización de disponibilidad
#Permitir seleccionar un instructor por nombre.
#Pedir nuevos días disponibles y actualizar su registro.
#Persistencia
#Cargar automáticamente la información desde instructores.json al iniciar.
#Crear el archivo si no existe.
#Menú principal
#=== GESTIÓN DE INSTRUCTORES DRIVESAFE ===
#1. Registrar nuevo instructor
#2. Listar instructores
#3. Actualizar disponibilidad
#4. Salir
#Ejemplo de ejecución esperada
#=== GESTIÓN DE INSTRUCTORES DRIVESAFE ===
#1. Registrar nuevo instructor
#2. Listar instructores
#3. Actualizar disponibilidad
#4. Salir
#Seleccione una opción: 1
#Nombre: María Gómez
#Categoría de licencia (A/B/C): B
#Días disponibles (separados por comas): Lunes, Miércoles, Viernes
#Instructor registrado correctamente.

#Seleccione una opción: 2
#--- Lista de Instructores ---
#Nombre: María Gómez | Licencia: B | Días: Lunes, Miércoles, Viernes

#Seleccione una opción: 3
#Ingrese el nombre del instructor: María Gómez
#Nuevos días disponibles: Martes, Jueves
#Disponibilidad actualizada correctamente.

from validaciones import validar_entero, validar_texto, validar_opcion
from gestion_json import cargar, reemplazar

def menu_instructores():
    while True:
        opcion_menu = validar_entero("""
            BIENVENIDO AL MÓDULO DE INSTRUCTORES

            1. Registrar instructor
            2. Listar instructores
            3. Actualizar disponibilidad
            4. Regresar

            Opción: """)

        match opcion_menu:
            case 1:
                agregar_instructor()

            case 2:
                listar_instructor()

            case 3:
                cambiar_disponibilidad()
                
                nombre = validar_texto(
                    "Ingrese el nombre del instructor: "
                )

                cambiar_disponibilidad(nombre)

            case 4:
                print("Saliendo del modulo...")
                break

            case _:
                print("Opción no encontrada.")


def agregar_instructor():
    registros = cargar("instructores.json")

    nombre = validar_texto(
        "Ingrese el nombre del instructor: "
    )
    categoria = validar_opcion(
            """
    Seleccione la categoría de licencia:
    1. A
    2. B
    3. C
    Opción: """,
            ["1", "2", "3"]
        )

    dias_disponibles = validar_texto(
        "Ingrese los días disponibles (separados por comas): "
    )
    nuevo_instructor = {
        "nombre": nombre,
        "Categoría de licencia (A/B/C): ": categoria,
        "dias_disponibles": dias_disponibles
    }
    registros.append(nuevo_instructor)
    reemplazar("instructores.json", registros)
    print("Instructor registrado correctamente.")


def listar_instructor():
    registros = cargar("instructores.json")

    if not registros:
        print("No existen instructores registrados.")
        return

    for item in registros:
        imprimir(item)


def cambiar_disponibilidad(nombre_instructor):
    registros = cargar("instructores.json")

    for item in registros:
        if item.get("nombre") == nombre_instructor:
            item["dias_disponibles"] = validar_texto(
                "Ingrese los nuevos días disponibles (separados por comas): "
            )

            reemplazar(
                "instructores.json",
                registros
            )

            print("Disponibilidad actualizada correctamente.")
            return

    print("El instructor no existe.")

def imprimir(instructor):
    estado_actual = "Disponible" if instructor.get("disponible") else "No disponible"

    print(f"""
        ******************************
        Nombre:       {instructor.get("nombre")}
        Categoría:    {instructor.get("categoria")}
        Días Disponibles: {instructor.get("dias_disponibles")}
        Estado:       {estado_actual}
    """)

  