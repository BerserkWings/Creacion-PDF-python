# Cargando librerias
import itertools
from random import randint
from statistics import mean
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4, letter


# función grouper
def grouper(iterable, n):
    # Crea a partir de ciertos datos iterables (en este caso los datos)
    # una variable para manejarlos
    args = [iter(iterable)] * n
    # Aquí entonces regresa los datos "encapsulados" de manera apuntador
    # Es por ello que se envían así a la función
    return itertools.zip_longest(*args)


# Función para exportar al PDF
def export_to_pdf(data):
    # Primero se crea el archivo PDF con su nombre y tamaño de hoja
    c = canvas.Canvas("alumnos.pdf", pagesize=A4)
    # Se saca el tamaño de la hoja A4
    w, h = A4
    # con esto se establece el número máximo de registros por página
    max_rows_per_page = 5
    # Márgenes en pixeles
    x_offset = 60
    y_offset = 60
    # Se coloca un espacio entre cada una de las filas
    padding = 15

    # Aquí se genera las listas para cada una de las líneas que comprenderán
    # a la rejilla de la tabla
    xlist = [x + x_offset for x in [0, 200, 250, 300, 350, 400, 480]]
    # Observar como se generan las líneas horizontales en el eje Y
    ylist = [h - y_offset - i * padding for i in range(max_rows_per_page + 1)]

    # Pasar por todos los datos
    for rows in grouper(data, max_rows_per_page):
        # acomodar las fils
        rows = tuple(filter(bool, rows))
        # Crear las líneas de la rejillas de la tabla
        c.grid(xlist, ylist[:len(rows) + 1])
        # en este doble for se va iterando sobre los datos para irlos
        # "pintando" dentro de 1 sola página
        for y, row in zip(ylist[:-1], rows):
            for x, cell in zip(xlist, row):
                c.drawString(x + 2, y - padding + 3, str(cell))
        # Showpage termina la página
        c.showPage()
    # Aquí termina de crear cada página y salva el archivo
    c.save()


# Se genera una lista con los datos del encabezado de la tabla
data = [("SKU", "Nombre", "Imagen", "Precio Unitario", "Impresión.", "FEE", "Cantidad", "Total")]
# Ahora recorrer de 1 a 100 elementos (que serán como simular 100 alumnos)
for i in range(1, 7):
    # Los exámenes se crea una lista de 3 elementos aleatorios
    exams = [randint(0, 10) for _ in range(3)]
    # Se obtiene el promedio de las calificaciones generadas
    avg = round(mean(exams), 2)
    # Aquí se decide si su estado es Aprobado o Reprobado
    state = "Aprobado" if avg >= 6 else "Reprobado"
    # Se añaden a la lista losa valores, observar que exams se trata como una
    # especie de apuntador
    data.append((f"Alumno {i}", *exams, avg, state))
# Una vez que se generaron las 100 calificaciones, se crear el PDF
export_to_pdf(data)