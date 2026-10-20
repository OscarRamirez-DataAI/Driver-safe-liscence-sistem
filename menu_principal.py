from validaciones import validar_entero
from gestion_instructores import menu_instructores
from gestion_clientes import menu_clientico
from gestion_vehiculos import menu_vehiculitos
from gestion_citas_y_cursos import menu_citicas

def menu():
    while True:
        opcion_general = validar_entero('''
            BIENVENIDO A DRIVERSAFE
                1. Gestion de Instructores
                2. Gestion de clientes
                3. Gestionn de vehiculos
                4. Gestion de agengamiento de citas y cursos
                5. Salir

                opcion: ''')

        match opcion_general:
            case 1:
                menu_instructores()
            case 2:
                menu_clientico()
            case 3:
                menu_vehiculitos()
            case 4:
                menu_citicas()
            case 5:
                print("Saliendo...")
                break