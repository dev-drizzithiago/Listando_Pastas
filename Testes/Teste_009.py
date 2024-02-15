from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from datetime import datetime
from pathlib import Path


valor_pasta_destino = Path().home()
pasta_arq_registro_extensao = str(Path(valor_pasta_destino, 'AppData', 'LocalLow', 'extensoes'))
valor_datatime = datetime.now()
data_atual = valor_datatime.strftime('%d/%m/%Y')
hora_atual = valor_datatime.strftime('%H:%M')


# Declaração de variaveis
data = data_atual.replace('/', '')
hora = hora_atual.replace(':', '')

# Declaração de linha
w, h = A4
x = 50
y = h - 50

# CORPO RELATORIO
arquivo_pdf = str('Relatorio_' + data + '_' + hora + '.pdf')
relatorio_pdf = canvas.Canvas('arquivo_pdf.pdf', pagesize=A4)
relatorio_pdf.line(x, y, x + 500, y)
relatorio_pdf.drawString(x + 450, 800, "Relatorios")
relatorio_pdf.save()
