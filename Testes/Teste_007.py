from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4

w, h = A4
c = canvas.Canvas('ola mundo.pdf', pagesize=A4)
c.drawString(10, 800, 'ola mundo!')
c.showPage()
c.save()
