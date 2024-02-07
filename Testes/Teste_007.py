from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4

c = canvas.Canvas('ola mundo.pdf', pagesize=A4)
c.drawString(10, 800, 'ola mundo!')
c.save()
