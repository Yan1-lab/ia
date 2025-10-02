from io import BytesIO
from datetime import datetime
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def generar_pdf(nombre, edad, sintomas, resultado):
    buffer = BytesIO()
    c = canvas.Canvas(buffer, pagesize=letter)
    c.setFont("Helvetica-Bold", 16)
    c.drawString(200, 750, "Reporte Médico IA")
    c.setFont("Helvetica", 12)
    c.drawString(50, 700, f"Nombre: {nombre}")
    c.drawString(50, 680, f"Edad: {edad}")
    c.drawString(50, 660, f"Fecha: {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    c.drawString(50, 630, "Síntomas:")
    text_obj = c.beginText(50, 610)
    text_obj.setFont("Helvetica", 11)
    for line in sintomas.split("\n"):
        text_obj.textLine(line)
    c.drawText(text_obj)
    c.drawString(50, 560, "Análisis IA:")
    text_obj2 = c.beginText(50, 540)
    text_obj2.setFont("Helvetica", 11)
    for line in resultado.split("\n"):
        text_obj2.textLine(line)
    c.drawText(text_obj2)
    c.showPage()
    c.save()
    buffer.seek(0)
    return buffer
