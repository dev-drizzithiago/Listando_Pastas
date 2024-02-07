from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4

"""Uma folha A4 é composta por 595,2 pontos de largura ( largura ) e 841,8 pontos de altura ( altura )."""

w, h = A4
c = canvas.Canvas('ola mundo.pdf', pagesize=A4)
c.drawString(10, 800, 'ola mundo!')

# linha
x = 10
y = h - 50
c.line(x, y, x + 580, y)  # linha reta horizontal

# retangulo
x = 50
y = h - 50
c.line(50, h - 300, 300, 300)

# Este método informa ao ReportLab que terminamos de trabalhar na planilha atual e queremos passar para a próxima.
c.showPage()

# salvar o documento
c.save()
