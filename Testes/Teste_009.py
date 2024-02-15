from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from datetime import datetime
from pathlib import Path

categorias_busca = ('Arquivo Imagem', 'Arquivos de Vídeos/Audios', 'Arquivos de Leitura', 'Arquivos execução',
                    'Arquivos compreesão')

valor_pasta_destino = Path().home()
pasta_arq_registro_extensao = str(Path(valor_pasta_destino, 'AppData', 'LocalLow', 'extensoes'))
valor_datatime = datetime.now()
data_atual = valor_datatime.strftime('%d/%m/%Y')
hora_atual = valor_datatime.strftime('%H:%M')


# Declaração de variaveis
data = data_atual.replace('/', '')
hora = hora_atual.replace(':', '')
contador = 1
w, h = A4

# Declaração de linha
x_linha = 50
y_linha = h - 50

# DECLARAÇÃO TEXTO
x_txt = 50
y_txt = h - 70

# CORPO RELATORIO
arquivo_pdf = str('Relatorio_' + data + '_' + hora + '.pdf')

relatorio_pdf = canvas.Canvas('arquivo_pdf.pdf', pagesize=A4)
relatorio_pdf.drawCentredString(300, 800, f"Relatorio {data_atual}")
relatorio_pdf.line(x_linha, y_linha, x_linha + 500, y_linha)  # Primeira linha
relatorio_pdf.line(x_linha, y_linha - 730, x_linha + 500, y_linha - 730)  # Última linha

texto_indice = relatorio_pdf.beginText(x_txt, y_txt)
texto_string = relatorio_pdf.beginText(x_txt + 15, y_txt)

for cont in range(1, 70):
    texto_indice.textLines(f'{cont}')
    contador += 1

    if contador == 50:
        relatorio_pdf.showPage()

for cont in categorias_busca:
    texto_string.textLines(cont)

relatorio_pdf.drawText(texto_indice)
relatorio_pdf.drawText(texto_string)

relatorio_pdf.save()
