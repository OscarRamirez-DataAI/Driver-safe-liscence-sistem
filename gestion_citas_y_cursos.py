from datetime import datetime, timedelta

from validaciones import (
    validar_entero,
    validar_fecha,
    validar_hora,
    validar_si_no,
    validar_texto_opcional
)
from gestion_json import cargar, cargar_json, reemplazar, generar_id
from gestion_clientes import (
    buscar_cliente,
    listar_cliente
)
from gestion_instructores import (
    buscar_instructor,
    listar_instructor
)
from gestion_vehiculos import (
    buscar_vehiculo,
    listar_vehiculo
)


NOMBRE_ARCHIVO = "cita.json"


def buscar_cita(id_cita):
    datos = cargar(NOMBRE_ARCHIVO)

    for item in datos:
        if item.get("id") == id_cita:
            return item

    return None


def obtener_intervalo(fecha, hora, duracion):
    fecha_hora = datetime.strptime(
        f"{fecha} {hora}",
        "%Y-%m-%d %H:%M"
    )

    fecha_hora_final = fecha_hora + timedelta(
        minutes=duracion
    )

    return fecha_hora, fecha_hora_final


def existe_conflicto(
    registros_citas,
    campo,
    id_elemento,
    fecha,
    hora,
    duracion
):
    nuevo_inicio, nuevo_final = obtener_intervalo(
        fecha,
        hora,
        duracion
    )

    for item in registros_citas:
        if item.get(campo) == id_elemento:
            inicio_existente, final_existente = obtener_intervalo(
                item.get("fecha"),
                item.get("hora"),
                item.get("duracion", 0)
            )

            if (
                nuevo_inicio < final_existente
                and inicio_existente < nuevo_final
            ):
                return True

    return False


def agregar():
    registros = cargar(NOMBRE_ARCHIVO)

    datos_clientes = cargar("cliente.json")
    datos_instructores = cargar("instructores.json")
    datos_vehiculos = cargar("vehiculos.json")

    if not datos_clientes:
        print("Debe registrar al menos un cliente.")
        return

    if not datos_instructores:
        print("Debe registrar al menos un instructor.")
        return

    if not datos_vehiculos:
        print("Debe registrar al menos un vehículo.")
        return

    listar_cliente()

    id_cliente = validar_entero(
        "Ingrese el ID del cliente: "
    )

    cliente_hallado = buscar_cliente(id_cliente)

    if cliente_hallado is None:
        print("El cliente no existe.")
        return

    listar_instructor()

    id_instructor = validar_entero(
        "Ingrese el ID del instructor: "
    )

    instructor_hallado = buscar_instructor(id_instructor)

    if instructor_hallado is None:
        print("El instructor no existe.")
        return

    if not instructor_hallado.get("disponible"):
        print("El instructor está marcado como no disponible.")
        return

    if instructor_hallado.get("especialidad") != cliente_hallado.get("tipo_vehiculo"):
        print(
            "La especialidad del instructor no coincide "
            "con el tipo de vehículo del cliente."
        )
        return

    listar_vehiculo()

    id_vehiculo = validar_entero(
        "Ingrese el ID del vehículo: "
    )

    vehiculo_hallado = buscar_vehiculo(id_vehiculo)

    if vehiculo_hallado is None:
        print("El vehículo no existe.")
        return

    if not vehiculo_hallado.get("disponible"):
        print("El vehículo está marcado como no disponible.")
        return

    if vehiculo_hallado.get("tipo") != cliente_hallado.get("tipo_vehiculo"):
        print(
            "El tipo del vehículo no coincide "
            "con el solicitado por el cliente."
        )
        return

    fecha = validar_fecha(
        "Ingrese la fecha de la cita (AAAA-MM-DD): "
    )

    hora = validar_hora(
        "Ingrese la hora de la cita (HH:MM): "
    )

    duracion = validar_entero(
        "Ingrese la duración en minutos: ",
        minimo=30
    )

    inicio_cita, _ = obtener_intervalo(
        fecha,
        hora,
        duracion
    )

    if inicio_cita <= datetime.now():
        print("La cita debe programarse para una fecha futura.")
        return

    if existe_conflicto(
        registros,
        "id_cliente",
        id_cliente,
        fecha,
        hora,
        duracion
    ):
        print("El cliente ya tiene una cita en ese horario.")
        return

    if existe_conflicto(
        registros,
        "id_instructor",
        id_instructor,
        fecha,
        hora,
        duracion
    ):
        print("El instructor ya tiene una cita en ese horario.")
        return

    if existe_conflicto(
        registros,
        "id_vehiculo",
        id_vehiculo,
        fecha,
        hora,
        duracion
    ):
        print("El vehículo ya está reservado en ese horario.")
        return

    nueva_cita = {
        "id": generar_id(registros),
        "id_cliente": id_cliente,
        "id_instructor": id_instructor,
        "id_vehiculo": id_vehiculo,
        "fecha": fecha,
        "hora": hora,
        "duracion": duracion,
        "asistencia": None,
        "observaciones": "",
        "estado": "programada"
    }

    registros.append(nueva_cita)
    reemplazar(NOMBRE_ARCHIVO, registros)

    print("Cita programada correctamente.")


def imprimir(cita):
    cliente_hallado = buscar_cliente(cita.get("id_cliente"))
    instructor_hallado = buscar_instructor(cita.get("id_instructor"))
    vehiculo_hallado = buscar_vehiculo(cita.get("id_vehiculo"))

    nombre_cliente = cliente_hallado.get("nombre") if cliente_hallado else "Cliente no encontrado"
    nombre_instructor = instructor_hallado.get("nombre") if instructor_hallado else "Instructor no encontrado"
    placa_vehiculo = vehiculo_hallado.get("placa") if vehiculo_hallado else "Vehículo no encontrado"

    asistencia_valor = cita.get("asistencia")
    if asistencia_valor is None:
        asistencia_texto = "Pendiente"
    elif asistencia_valor:
        asistencia_texto = "Sí asistió"
    else:
        asistencia_texto = "No asistió"

    print(f"""
        *************************************
        ID de cita:   {cita.get("id")}
        Cliente:      {nombre_cliente}
        Instructor:   {nombre_instructor}
        Vehículo:     {placa_vehiculo}
        Fecha:        {cita.get("fecha")}
        Hora:         {cita.get("hora")}
        Duración:     {cita.get("duracion")} minutos
        Estado:       {cita.get("estado")}
        Asistencia:   {asistencia_texto}
        Observaciones:{cita.get("observaciones")}
    """)


def listar():
    registros = cargar(NOMBRE_ARCHIVO)

    if not registros:
        print("No existen citas registradas.")
        return

    for item in registros:
        imprimir(item)


def buscar_por_cliente(id_cliente):
    datos = cargar(NOMBRE_ARCHIVO)
    resultados = []

    for item in datos:
        if item.get("id_cliente") == id_cliente:
            resultados.append(item)

    return resultados


def consultar_por_cliente():
    listar_cliente()

    id_cliente = validar_entero(
        "Ingrese el ID del cliente: "
    )

    cliente_hallado = buscar_cliente(id_cliente)

    if cliente_hallado is None:
        print("El cliente no existe.")
        return

    resultados = buscar_por_cliente(id_cliente)

    if not resultados:
        print("El cliente no tiene citas registradas.")
        return

    for item in resultados:
        imprimir(item)


def buscar_por_fecha(fecha):
    datos = cargar(NOMBRE_ARCHIVO)
    resultados = []

    for item in datos:
        if item.get("fecha") == fecha:
            resultados.append(item)

    return resultados


def consultar_por_fecha():
    fecha_ingresada = validar_fecha(
        "Ingrese la fecha (AAAA-MM-DD): ",
        permitir_pasado=True
    )

    resultados = buscar_por_fecha(fecha_ingresada)

    if not resultados:
        print("No existen citas para esa fecha.")
        return

    for item in resultados:
        imprimir(item)


def registrar_asistencia():
    registros = cargar(NOMBRE_ARCHIVO)

    if not registros:
        print("No existen citas registradas.")
        return

    listar()

    id_cita = validar_entero(
        "Ingrese el ID de la cita: "
    )

    for item in registros:
        if item.get("id") == id_cita:
            if item.get("estado") != "programada":
                print(
                    "La asistencia de esta cita ya fue registrada."
                )
                return

            asistencia_confirmada = validar_si_no(
                "¿El cliente asistió? (S/N): "
            )

            observaciones_texto = validar_texto_opcional(
                "Ingrese las observaciones: "
            )

            item["asistencia"] = asistencia_confirmada
            item["observaciones"] = observaciones_texto
            item["estado"] = "realizada" if asistencia_confirmada else "inasistencia"

            reemplazar(NOMBRE_ARCHIVO, registros)

            print("Asistencia registrada correctamente.")
            return

    print("La cita no existe.")


def historial_cliente():
    listar_cliente()

    id_cliente = validar_entero(
        "Ingrese el ID del cliente: "
    )

    cliente_hallado = buscar_cliente(id_cliente)

    if cliente_hallado is None:
        print("El cliente no existe.")
        return

    lista_citas = buscar_por_cliente(id_cliente)
    historial = [
        item for item in lista_citas 
        if item.get("estado") in ["realizada", "inasistencia"]
    ]

    if not historial:
        print("El cliente no tiene prácticas realizadas.")
        return

    print(f"""
        HISTORIAL DE PRÁCTICAS
        Cliente: {cliente_hallado.get("nombre")}
        Documento: {cliente_hallado.get("documento")}
    """)

    for item in historial:
        imprimir(item)


from gestion_json import cargar_json, guardar_json


def cancelar_cita():
    registros = cargar(NOMBRE_ARCHIVO)
    if not registros:
        print("No existen citas registradas.")
        return

    listar()  # Muestra todas las citas para ver su ID
    id_cita = validar_entero("Ingrese el ID de la cita a cancelar: ")

    for item in registros:
        if item.get("id") == id_cita:
            if item.get("estado") == "cancelada":
                print("La cita ya se encuentra cancelada.")
                return

            # Se actualiza el estado utilizando tus llaves
            item["estado"] = "cancelada"
            reemplazar(NOMBRE_ARCHIVO, registros)
            print("Cita cancelada correctamente.")
            return

    print("La cita no existe.")

def menu_citicas():
    while True:
        opcion_menu = validar_entero("""
            BIENVENIDO AL MÓDULO DE CITAS

            1. Programar cita
            2. Cancelar cita
            3. Listar todas las citas
            4. Consultar citas por cliente
            5. Consultar citas por fecha
            6. Registrar asistencia y observaciones
            7. Consultar historial de un cliente
            8. Cancelar cita
            9. Regresar

            Opción: """)

        match opcion_menu:
            case 1:
                agregar()

            case 2:
                cancelar_cita()
            case 3:
                listar()

            case 4:
                consultar_por_cliente()

            case 5:
                consultar_por_fecha()

            case 6:
                registrar_asistencia()

            case 7:
                historial_cliente()

            case 8:
                cancelar_cita()

            case 9: 
                break

            case _:
                print("Opción no encontrada.")