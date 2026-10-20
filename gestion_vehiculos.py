from validaciones import (
    validar_entero,
    validar_texto,
    validar_opcion
)
from gestion_json import cargar, reemplazar, generar_id


NOMBRE_ARCHIVO = "vehiculos.json"


def buscar_vehiculo(id_vehiculo):
    datos = cargar(NOMBRE_ARCHIVO)

    for item in datos:
        if item.get("id") == id_vehiculo:
            return item

    return None


def buscar_por_placa(placa):
    datos = cargar(NOMBRE_ARCHIVO)

    for item in datos:
        if item.get("placa", "").upper() == placa.upper():
            return item

    return None


def agregar():
    registros = cargar(NOMBRE_ARCHIVO)

    placa_ingresada = validar_texto(
        "Ingrese la placa del vehículo: "
    ).upper()

    if buscar_por_placa(placa_ingresada) is not None:
        print("Ya existe un vehículo con esa placa.")
        return

    nuevo_vehiculo = {
        "id": generar_id(registros),
        "placa": placa_ingresada
    }

    seleccion_tipo = validar_opcion(
        """
Seleccione el tipo de vehículo:
1. Moto
2. Carro
Opción: """,
        ["1", "2"]
    )

    nuevo_vehiculo["tipo"] = "moto" if seleccion_tipo == "1" else "carro"
    nuevo_vehiculo["disponible"] = True

    registros.append(nuevo_vehiculo)
    reemplazar(NOMBRE_ARCHIVO, registros)

    print("Vehículo registrado correctamente.")


def imprimir(vehiculo):
    estado_actual = "Disponible" if vehiculo.get("disponible") else "No disponible"

    print(f"""
        ******************************
        ID:         {vehiculo.get("id")}
        Placa:      {vehiculo.get("placa")}
        Tipo:       {vehiculo.get("tipo")}
        Estado:     {estado_actual}
    """)


def listar_vehiculo():
    registros = cargar(NOMBRE_ARCHIVO)

    if not registros:
        print("No existen vehículos registrados.")
        return

    for item in registros:
        imprimir(item)


def cambiar_disponibilidad(id_vehiculo):
    registros = cargar(NOMBRE_ARCHIVO)

    for item in registros:
        if item.get("id") == id_vehiculo:
            item["disponible"] = not item.get("disponible", False)

            reemplazar(
                NOMBRE_ARCHIVO,
                registros
            )

            print("Disponibilidad actualizada correctamente.")
            return

    print("El vehículo no existe.")


def menu_vehiculitos():
    while True:
        opcion_menu = validar_entero("""
            _________________________________
                                
            BIENVENIDO AL MÓDULO DE VEHÍCULOS
            _________________________________
                                
            1. Registrar vehículo
            2. Listar vehículos
            3. Cambiar disponibilidad
            4. Regresar

            Opción: """)

        match opcion_menu:
            case 1:
                agregar()

            case 2:
                listar_vehiculo()

            case 3:
                listar_vehiculo()

                id_auto = validar_entero(
                    "Ingrese el ID del vehículo: "
                )

                cambiar_disponibilidad(id_auto)

            case 4:
                break

            case _:
                print("Opción no encontrada.")