import os

# Variables goblales
CARPETA = 'contactos/'
EXTENSION = '.txt'

# Contactos
class Contacto:
    def __init__(self, nombre, telefono, categoria):
        self.nombre = nombre
        self.telefono = telefono
        self.categoria = categoria


def app():
    # Revisa si la carpeta existe, sino la crea
    crear_directorio()
    # Muestra el menu de opciones
    mostrar_menu()
    # Preguntar al usuario
    preguntar = True
    while preguntar:
        opt = input('Seleccione una opcion: \r\n')
        opt = int(opt)

        if opt == 1:
            print('Agregar contacto')
            agregar_contacto()
            mostrar_menu()
        elif opt == 2:
            print('Modifica contacto')
            editar_contacto()
            mostrar_menu()
        elif opt == 3:
            print('Ver contacto')
            mostrar_contacto()
            mostrar_menu()
        elif opt == 4:
            print('Buscar contacto')
            buscar_contacto()
            mostrar_menu()
        elif opt == 5:
            print('Borrar contacto')
            eliminar_contacto()
            mostrar_menu()
        elif opt == 6:
            print('Cerraste la aplicacion, escribe en la consola "python proyecto.py" si quieres reiniciarla')
            preguntar = False
        else:
            print('Esa opcion no existe')
    


def eliminar_contacto():
    nombre = input('Escriba el nombre del contacto que desea eliminar: \r\n')
    try:
        os.remove(CARPETA + nombre + EXTENSION)
        print('El archivo eliminado correctamente')
    except IOError:
        print('El contacto no existe')
        # print(IOError)
        app()


def buscar_contacto():
    nombre = input('Escriba el nombre del contacto que desea buscar: \r\n')


def mostrar_contacto():
    archivos = os.listdir(CARPETA)


def editar_contacto():
    print('Escribe el nombre del contacto')


def agregar_contacto():
    print('Escribe los datos para agregar el nuevo contacto:')
    nombre_contacto = input('Nombre del contacto: \r\n')

    ruta_file = CARPETA + nombre_contacto + EXTENSION
    # Revisar si el archivo ya existe
    existe = existe_contacto(ruta_file)

    if not existe:
        with open(ruta_file, 'w') as archivo:
            telefono_contacto = input('Agrega el telefono: \r\n')
            categoria_contacto = input(
                'Agrega una categoria del contacto: \r\n')

            # instanciar la clase
            contacto = Contacto(
                nombre_contacto, telefono_contacto, categoria_contacto)

            # Escribir en el contacto
            archivo.write('Nombre: '+contacto.nombre+'\r\n')
            archivo.write('Telefono: '+contacto.telefono+'\r\n')
            archivo.write('Categoria: '+contacto.categoria+'\r\n')

            # Msg de exito
            print('\r\n Contacto creado correctamente \r\n')
    else:
        print('Ese contacto ya existe')
        # reiniciar App
        app()


def existe_contacto(ruta_file):
    return os.path.isfile(ruta_file)


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