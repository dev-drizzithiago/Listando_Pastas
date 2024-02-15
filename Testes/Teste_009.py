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
w, h = A4

# Declaração de linha
x_linha = 50
y_linha = h - 50

# DECLARAÇÃO TEXTO
x_txt = 52
y_txt = h - 50

# CORPO RELATORIO
arquivo_pdf = str('Relatorio_' + data + '_' + hora + '.pdf')

relatorio_pdf = canvas.Canvas('arquivo_pdf.pdf', pagesize=A4)
relatorio_pdf.line(x_linha, y_linha, x_linha + 500, y_linha)

texto = relatorio_pdf.beginText(x_txt, y_txt + 500)
texto.setFont('Helvetica', 12)
texto.textLine('Testando')
relatorio_pdf.drawText(texto)

relatorio_pdf.drawString(420, 800, f"Relatorio {data_atual}")
relatorio_pdf.save()
