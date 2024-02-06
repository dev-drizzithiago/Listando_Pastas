from reportlab.pdfgen import canvas

c = canvas.Canvas('ola mundo.pdf')
c.save()
