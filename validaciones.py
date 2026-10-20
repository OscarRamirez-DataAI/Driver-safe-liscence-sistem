from datetime import datetime, date


def validar_entero(mensaje, minimo=None):
    while True:
        dato = input(mensaje).strip()

        if dato.isdigit():
            numero = int(dato)

            if minimo is not None and numero < minimo:
                print(f"El número debe ser mayor o igual a {minimo}.")
            else:
                return numero
        else:
            print("Dato incorrecto. Ingrese un número entero.")


def validar_texto(mensaje):
    dato = input(mensaje).strip()

    while len(dato) < 2:
        dato = input(
            "El texto debe tener al menos 2 caracteres: "
        ).strip()

    return dato


def validar_texto_opcional(mensaje):
    return input(mensaje).strip()


def validar_documento(mensaje):
    documento = input(mensaje).strip()

    while not documento.isdigit() or len(documento) < 5:
        documento = input(
            "Documento incorrecto. Ingrese únicamente números: "
        ).strip()

    return documento


def validar_opcion(mensaje, opciones):
    opcion = input(mensaje).strip()

    while opcion not in opciones:
        opcion = input("Opción incorrecta. Intente nuevamente: ").strip()

    return opcion


def validar_fecha(mensaje, permitir_pasado=False):
    while True:
        fecha_texto = input(mensaje).strip()

        try:
            fecha = datetime.strptime(
                fecha_texto,
                "%Y-%m-%d"
            ).date()

            if not permitir_pasado and fecha < date.today():
                print("La fecha no puede estar en el pasado.")
            else:
                return fecha.strftime("%Y-%m-%d")

        except ValueError:
            print("Fecha incorrecta. Utilice AAAA-MM-DD.")


def validar_hora(mensaje):
    while True:
        hora_texto = input(mensaje).strip()

        try:
            hora = datetime.strptime(
                hora_texto,
                "%H:%M"
            )

            return hora.strftime("%H:%M")

        except ValueError:
            print("Hora incorrecta. Utilice HH:MM.")


def validar_si_no(mensaje):
    respuesta = input(mensaje).strip().lower()

    while respuesta not in ["s", "si", "sí", "n", "no"]:
        respuesta = input(
            "Respuesta incorrecta. Escriba S o N: "
        ).strip().lower()

    return respuesta in ["s", "si", "sí"]