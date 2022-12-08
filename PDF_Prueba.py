# Cargando librerias
import os
import base64
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

PAGE_HEIGHT = defaultPageSize[1];
PAGE_WIDTH = defaultPageSize[0]
estilo = getSampleStyleSheet()
Imagen = Image('miku.png', width=100, height=100)
doc = SimpleDocTemplate("test.pdf", pagesize=A4)
story = []

P1 = Paragraph('''SI VALE''', estilo["BodyText"])
P2 = Paragraph('''MONEDERO SI VALE''', estilo["BodyText"])

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

#  Creando archivo de texto en base64
archivo_b64 = open("Prueba.txt", "w")

with open("test.pdf", "rb") as pdf_file:
    encoded_string = base64.b64encode(pdf_file.read())

archivo_b64.write(str(encoded_string))
archivo_b64.close()
