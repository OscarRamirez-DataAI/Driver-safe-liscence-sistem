from validaciones import (
    validar_entero,
    validar_fecha,
    validar_hora,
    validar_texto,
    validar_documento,
    validar_opcion
)
from gestion_json import cargar, reemplazar, generar_id


NOMBRE_ARCHIVO = "instructores.json"


def buscar_instructor(id_instructor):
    datos = cargar(NOMBRE_ARCHIVO)

    for item in datos:
        if item.get("id") == id_instructor:
            return item

    return None


def buscar_por_documento(documento):
    datos = cargar(NOMBRE_ARCHIVO)

    for item in datos:
        if item.get("documento") == documento:
            return item

    return None


def agregar():
    registros = cargar(NOMBRE_ARCHIVO)

    num_documento = validar_documento(
        "Ingrese el documento del instructor: "
    )

    if buscar_por_documento(num_documento) is not None:
        print("Ya existe un instructor con ese documento.")
        return

    nuevo_instructor = {
        "id": generar_id(registros),
        "nombre": validar_texto("Ingrese el nombre del instructor: "),
        "documento": num_documento
    }

    seleccion_esp = validar_opcion(
        """
Seleccione la especialidad:
1. Moto
2. Carro
Opción: """,
        ["1", "2"]
    )

    nuevo_instructor["especialidad"] = "moto" if seleccion_esp == "1" else "carro"
    nuevo_instructor["disponible"] = True

    registros.append(nuevo_instructor)
    reemplazar(NOMBRE_ARCHIVO, registros)

    print("Instructor registrado correctamente.")


def imprimir(instructor):
    estado_actual = "Disponible" if instructor.get("disponible") else "No disponible"

    print(f"""
        ******************************
        ID:           {instructor.get("id")}
        Nombre:       {instructor.get("nombre")}
        Documento:    {instructor.get("documento")}
        Especialidad: {instructor.get("especialidad")}
        Estado:       {estado_actual}
    """)


def listar_instructor():
    registros = cargar(NOMBRE_ARCHIVO)

    if not registros:
        print("No existen instructores registrados.")
        return

    for item in registros:
        imprimir(item)


def cambiar_disponibilidad(id_instructor):
    registros = cargar(NOMBRE_ARCHIVO)

    for item in registros:
        if item.get("id") == id_instructor:
            item["disponible"] = not item.get("disponible", False)

            reemplazar(
                NOMBRE_ARCHIVO,
                registros
            )

            print("Disponibilidad actualizada correctamente.")
            return

    print("El instructor no existe.")


def menu_instructores():
    while True:
        opcion_menu = validar_entero("""
            BIENVENIDO AL MÓDULO DE INSTRUCTORES

            1. Registrar instructor
            2. Listar instructores
            3. Cambiar disponibilidad
            4. Regresar

            Opción: """)

        match opcion_menu:
            case 1:
                agregar()

            case 2:
                listar_instructor()

            case 3:
                listar_instructor()

                id_docente = validar_entero(
                    "Ingrese el ID del instructor: "
                )

                cambiar_disponibilidad(id_docente)

            case 4:
                break

            case _:
                print("Opción no encontrada.")






                #  def validar_disponibilidad_instructor(citas, instructor, fecha, hora):
                #"""Devuelve True si el instructor está disponible, False si ya tiene cita."""
                #for c in citas:
                 # Se verifica que coincidan instructor, fecha y hora
                #mismo_instructor = (
                #c.get("instructor", "").strip().lower()
                #== instructor.strip().lower()
                        
                #misma_fecha = c.get("fecha") == fecha
                #misma_hora = c.get("hora") == hora

                #if mismo_instructor and misma_fecha and misma_hora:
                 #return False  # Hay conflicto, el instructor está ocupado

                #return True  # Está libre

                #def registrar_nueva_cita():
                #citas = cargar(NOMBRE_ARCHIVO)

                #cliente = validar_texto("Ingrese cliente: ")
                #instructor = validar_texto("Ingrese instructor: ")
                #vehiculo = validar_texto("Ingrese vehículo: ")
                #fecha = validar_fecha("Ingrese fecha (YYYY-MM-DD): ")
                #hora = validar_hora("Ingrese hora (HH:MM): ")

                ## VALIDACIÓN: Verificar si el instructor ya tiene cita en esa fecha y hora
                #if not validar_disponibilidad_instructor(citas, instructor, fecha, hora):
                #print(
                # f"\n❌ Error: El instructor '{instructor}' ya tiene una cita programada el {fecha} a las {hora} con otro cliente.")
                #return  # Interrumpe el registro para que no se guarde la cita repetida

                # Si pasa la validación, se guarda la cita normalmente
                # nueva_cita = {
        #"id": generar_id(citas),
        # "cliente": cliente,
        #"instructor": instructor,
        #"vehiculo": vehiculo,
        #"fecha": fecha,
        #"hora": hora,
   # }

    #citas.append(nueva_cita)
    #reemplazar(NOMBRE_ARCHIVO, citas)
    #print("\n Cita registrada con éxito.")