from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4

"""Uma folha A4 é composta por 595,2 pontos de largura ( largura ) e 841,8 pontos de altura ( altura )."""

w, h = A4
c = canvas.Canvas('ola mundo.pdf', pagesize=A4)
c.drawString(10, 800, 'ola mundo!')

# linha
x = 10
y = h - 50  # O 'H' inverte o valor
c.line(x, y, x + 580, y)  # linha reta horizontal

# retangulo
x = 50
y = h - 50
c.rect(100, 300, 300, 300)

# Retangulos com curvas nas pontas
x = 10
y = 50
c.roundRect(x, 300, 300, 200, 10)

# Este método informa ao ReportLab que terminamos de trabalhar na planilha atual e queremos passar para a próxima.
c.showPage()

# salvar o documento
c.save()
