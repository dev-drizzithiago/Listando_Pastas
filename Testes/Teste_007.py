from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4

"""Uma folha A4 é composta por 595,2 pontos de largura ( largura ) e 841,8 pontos de altura ( altura )."""

w, h = A4
c = canvas.Canvas('ola mundo.pdf', pagesize=A4)
c.drawString(10, 800, 'ola mundo!')

# linha
x = 10
y = 50  # O 'H' inverte o valor
c.line(x, y, x + 580, y)  # linha reta horizontal


# retangulo
x = 20
y = h - 50
c.rect(100, 300, 300, 300)


# Retangulos com curvas nas pontas
x = 30  # Horizontal
y = 50  # Vertical
# opera de forma semelhante, mas um quinto argumento indica o raio pelo qual as extremidades são curvadas.
c.roundRect(x, 300, 300, 200, 50)

# No caso de círculos, a posição do centro é indicada seguida do raio.
y = 100
x = 100
raio = 100
c.circle(y, x, raio)

# Este método informa ao ReportLab que terminamos de trabalhar na planilha atual e queremos passar para a próxima.
c.showPage()

# salvar o documento
c.save()
