from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4

"""Uma folha A4 é composta por 595,2 pontos de largura ( largura ) e 841,8 pontos de altura ( altura )."""

w, h = A4
c = canvas.Canvas('ola mundo.pdf', pagesize=A4)
c.drawString(10, 800, 'ola mundo!')

# linha
x = 10
y = h - 50
c.line(x, y, x + 590, y)  # linha reta horizontal

# mostra pagina
c.showPage()

# salvar o documento
c.save()
