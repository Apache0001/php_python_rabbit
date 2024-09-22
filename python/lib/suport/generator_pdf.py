from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
PATH_ROOT_FILES = '/storage/pdf/teste.pdf'

# Fill the writer with the pages you want
pdf = canvas.Canvas('./teste.pdf', pagesize=A4)
pdf.drawString(0, 0, '<h1>Olá, mundo1</h1>')
pdf.save()
