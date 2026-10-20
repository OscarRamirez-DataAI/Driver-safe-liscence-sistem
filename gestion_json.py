import os
import json


DIRECTORIO_BASE = os.path.dirname(os.path.abspath(__file__))


def obtener_ruta(nombre_archivo):
    return os.path.join(DIRECTORIO_BASE, nombre_archivo)


def cargar(nombre_archivo):
    ubicacion = obtener_ruta(nombre_archivo)

    try:
        if os.path.exists(ubicacion):
            with open(ubicacion, "r", encoding="utf-8") as recurso:
                return json.load(recurso)
        else:
            return []

    except json.JSONDecodeError:
        print(f"El archivo {nombre_archivo} contiene un JSON inválido.")
        return []


def reemplazar(nombre_archivo, lista_datos):
    ubicacion = obtener_ruta(nombre_archivo)

    with open(ubicacion, "w", encoding="utf-8") as recurso:
        json.dump(
            lista_datos,
            recurso,
            indent=4,
            ensure_ascii=False
        )


def generar_id(lista):
    if not lista:
        return 1

    return max(registro.get("id", 0) for registro in lista) + 1


def cargar_json(ruta_archivo):
    """Carga los datos de un archivo JSON con validación de existencia y formato."""
    # 1. Verificar si el archivo existe
    if not os.path.exists(ruta_archivo):
        print(
            f"⚠️ El archivo '{ruta_archivo}' no existe. Creando uno nuevo..."
        )
        guardar_json(ruta_archivo, [])
        return []

    # 2. Intentar leer y decodificar el JSON
    try:
        with open(ruta_archivo, "r", encoding="utf-8") as archivo:
            datos = json.load(archivo)

            # Validar que sea una lista (para evitar errores al iterar)
            if isinstance(datos, list):
                return datos
            else:
                print(
                    f"⚠️ El contenido de '{ruta_archivo}' no es una lista válida."
                )
                return []

    except json.JSONDecodeError:
        print(f"❌ Error: El archivo '{ruta_archivo}' está dañado o vacío.")
        return []
    except Exception as e:
        print(f"❌ Error inesperado al leer '{ruta_archivo}': {e}")
        return []


def guardar_json(ruta_archivo, datos):
    """Guarda una lista de datos en el archivo JSON."""
    try:
        with open(ruta_archivo, "w", encoding="utf-8") as archivo:
            json.dump(datos, archivo, indent=4, ensure_ascii=False)
        return True
    except Exception as e:
        print(f"❌ Error al guardar en '{ruta_archivo}': {e}")
        return False