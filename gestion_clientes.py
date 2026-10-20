from validaciones import (
    validar_entero,
    validar_texto,
    validar_documento,
    validar_opcion
)
from gestion_json import cargar, reemplazar, generar_id


NOMBRE_ARCHIVO = "cliente.json"


def buscar_cliente(id_cliente):
    datos = cargar(NOMBRE_ARCHIVO)

    for item in datos:
        if item.get("id") == id_cliente:
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
        "Ingrese el documento del cliente: "
    )

    if buscar_por_documento(num_documento) is not None:
        print("Ya existe un cliente con ese documento.")
        return

    nuevo_cliente = {
        "id": generar_id(registros),
        "nombre": validar_texto("Ingrese el nombre del cliente: "),
        "documento": num_documento
    }

    seleccion_tipo = validar_opcion(
        """
Seleccione el tipo de vehículo:
1. Moto
2. Carro
Opción: """,
        ["1", "2"]
    )

    nuevo_cliente["tipo_vehiculo"] = "moto" if seleccion_tipo == "1" else "carro"

    registros.append(nuevo_cliente)
    reemplazar(NOMBRE_ARCHIVO, registros)

    print("Cliente registrado correctamente.")


def imprimir(cliente):
    print(f"""
        ******************************
        ID:               {cliente.get("id")}
        Nombre:           {cliente.get("nombre")}
        Documento:        {cliente.get("documento")}
        Tipo de vehículo: {cliente.get("tipo_vehiculo")}
    """)


def listar_cliente():
    registros = cargar(NOMBRE_ARCHIVO)

    if not registros:
        print("No existen clientes registrados.")
        return

    for item in registros:
        imprimir(item)


def consultar():
    id_usuario = validar_entero(
        "Ingrese el ID del cliente: "
    )

    cliente_hallado = buscar_cliente(id_usuario)

    if cliente_hallado is None:
        print("El cliente no existe.")
    else:
        imprimir(cliente_hallado)


def menu_clientico():
    while True:
        opcion_menu = validar_entero("""
            BIENVENIDO AL MÓDULO DE CLIENTES

            1. Registrar cliente
            2. Listar clientes
            3. Buscar cliente
            4. Regresar

            Opción: """)

        match opcion_menu:
            case 1:
                agregar()

            case 2:
                listar_cliente()

            case 3:
                consultar()

            case 4:
                break

            case _:
                print("Opción no encontrada.")