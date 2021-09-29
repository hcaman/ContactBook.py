import os

# Variables goblales
CARPETA = 'contactos/'

def app():
    # Revisa si la carpeta existe, sino la crea
    crear_directorio()
    # Muestra el menu de opciones
    mostrar_menu()

def crear_directorio():
    if not os.path.exists(CARPETA):
        os.makedirs(CARPETA)


def mostrar_menu():
    print('Selecciones del menu:')
    print('1 - Agregar contacto')
    print('2 - Modifica contacto')
    print('3 - Ver contacto')
    print('4 - Buscar contacto')
    print('5 - Borrar contacto')
    print('6 - Salir')


app()