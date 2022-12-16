# Cargando librerias
# Librerias reportlab a usar:
from reportlab.platypus import (SimpleDocTemplate, PageBreak, Image, Spacer, Paragraph, Table, TableStyle)
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import A4, letter
from reportlab.rl_config import defaultPageSize
from reportlab.lib.units import inch
from reportlab.lib import colors
from reportlab.pdfgen import canvas
# Libreria para importar a base64
from io import open
import base64

PAGE_HEIGHT = defaultPageSize[1]
PAGE_WIDTH = defaultPageSize[0]
estilo = getSampleStyleSheet()
doc = SimpleDocTemplate("test_nuevo.pdf", pagesize=A4)
story = []

contador = 1
# Pidiendo cantidad de datos al usuario
cantidad = input("Introduzca el primer dato de la fila 1: ")
story.append(cantidad)
deci = input("Agregas otro dato? S/N ")
while deci == "s" or deci == "S":
    cantidad = input("Introduzca otro dato a la fila 1: ")
    story.append(cantidad)
    deci = input("Agregas otro dato?: ")
    t = Table(story)
    story.append(t)
doc.build(story)
print(f"Los numeros introducidos son: {story}")
print(len(story))


"""

t = Table(
    data=[
        ['SKU', 'Nombre', 'Imagen', 'Precio Unitario', 'Impresión', 'FEE', 'Cantidad', 'Total'],
        [[P1], [P2], [Imagen], '$1,000.00', '$10.00', '$0.08', '3', '$3,272.40'],
        ['000', '000', '000', '000', '000', '000', '000', '000']
    ],
    style=[
        ('BACKGROUND', (0, 0), (8, 0), colors.aquamarine),
        ('BACKGROUND', (0, 1), (8, 2), colors.lightslategrey),
        ('BOX', (0, 0), (-1, -1), 1, colors.black),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ('ALIGN', (0, 0), (8, 2), 'CENTER'),
    ]
)
story.append(t)
doc.build(story)
"""


"""
def mostrar_menu(nombre, opciones):
    print(f'# {nombre}. Seleccione una opción:')
    for clave in sorted(opciones):
        print(f' {clave}) {opciones[clave][0]}')


def leer_opcion(opciones):
    while (a := input('Opción: ')) not in opciones:
        print('Opción incorrecta, vuelva a intentarlo.')
    return a


def ejecutar_opcion(opcion, opciones):
    opciones[opcion][1]()


def generar_menu(nombre, opciones, opcion_salida):  # incorporamos el parámetro para mostrar el nombre del menú
    opcion = None
    while opcion != opcion_salida:
        mostrar_menu(nombre, opciones)
        opcion = leer_opcion(opciones)
        ejecutar_opcion(opcion, opciones)
        print()


def menu_principal():
    opciones = {
        '1': ('Opción 1', funcion1),
        '2': ('Opción 2 >', submenu),  # la acción es una llamada a submenu que genera un nuevo menú
        '3': ('Opción 3', funcion3),
        '4': ('Salir', salir)
    }
    generar_menu('Menú principal', opciones, '4')  # indicamos el nombre del menú


def submenu():
    opciones = {
        'a': ('Opción a', funcionA),
        'b': ('Opción b', funcionB),
        'c': ('Volver al menú principal', salir)
    }

    generar_menu('Submenú', opciones, 'c')  # indicamos el nombre del submenú


# A partir de aquí creamos las funciones que ejecutan las acciones de los menús
def funcion1():
    print('Has elegido la opción 1')


def funcion2():
    print('Has elegido la opción 2')


def funcion3():
    print('Has elegido la opción 3')


def funcionA():
    print('Has elegido la opción A')


def funcionB():
    print('Has elegido la opción B')


def salir():
    print('Saliendo')


if __name__ == '__main__':
    menu_principal() # iniciamos el programa mostrando el menú principal
"""
