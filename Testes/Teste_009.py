from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from datetime import datetime
from pathlib import Path

categorias_busca = ('1 - G:\Meu Drive\Fotos\Fotos Penso Day Parte II 2-2023.pdf',
                    '2 - G:\Meu Drive\Fotos\\teste.txt',
                    '3 - G:\Meu Drive\Fotos\\teste.log',
                    '4 - G:\Meu Drive\Fotos\desktop.ini',
                    '5 - G:\Meu Drive\Fotos\Screenshots\Screenshot_20220725-085708.png',
                    '6 - G:\Meu Drive\Fotos\Screenshots\Screenshot_20220725-224021.png',
                    '7 - G:\Meu Drive\Fotos\Screenshots\Screenshot_20220727-080238.png',
                    '8 - G:\Meu Drive\Fotos\Screenshots\Screenshot_20220728-120141.png',
                    '9 - G:\Meu Drive\Fotos\Screenshots\Screenshot_20220729-123824.png',
                    '10 - G:\Meu Drive\Fotos\Screenshots\Screenshot_20220731-111027.png',
                    '11 - G:\Meu Drive\Fotos\Screenshots\Screenshot_20220809-120443.png',
                    '12 - G:\Meu Drive\Fotos\Screenshots\Screenshot_20220820-172710.png',
                    '13 - G:\Meu Drive\Fotos\Screenshots\Screenshot_20220820-205321.png',
                    '14 - G:\Meu Drive\Fotos\Screenshots\Screenshot_20220821-071518.png',
                    '15 - G:\Meu Drive\Fotos\Screenshots\Screenshot_20220821-072505.png',
                    '16 - G:\Meu Drive\Fotos\Screenshots\Screenshot_20220822-141901.png',
                    '17 - G:\Meu Drive\Fotos\Screenshots\Screenshot_20220824-105802.png',
                    '18 - G:\Meu Drive\Fotos\Screenshots\Screenshot_20220824-134047.png',
                    '19 - G:\Meu Drive\Fotos\Screenshots\Screenshot_20220826-120550.png',
                    '20 - G:\Meu Drive\Fotos\Screenshots\Screenshot_20220826-132340.png',
                    '21 - G:\Meu Drive\Fotos\Screenshots\Screenshot_20220827-160146.png',
                    '22 - G:\Meu Drive\Fotos\Screenshots\Screenshot_20220827-182258.png',
                    '23 - G:\Meu Drive\Fotos\Screenshots\Screenshot_20220828-211806.png',
                    '24 - G:\Meu Drive\Fotos\Screenshots\Screenshot_20220828-212030.png',
                    '25 - G:\Meu Drive\Fotos\Screenshots\Screenshot_20220828-212256.png',
                    '26 - G:\Meu Drive\Fotos\Screenshots\Screenshot_20220828-212329.png',
                    '27 - G:\Meu Drive\Fotos\Screenshots\Screenshot_20220828-212348.png',
                    '28 - G:\Meu Drive\Fotos\Screenshots\Screenshot_20220828-212440.png',
                    '29 - G:\Meu Drive\Fotos\Screenshots\Screenshot_20220901-083634.png',
                    '30 - G:\Meu Drive\Fotos\Screenshots\Screenshot_20220902-073242.png',
                    '31 - G:\Meu Drive\Fotos\Screenshots\Screenshot_20220902-073247.png',
                    '32 - G:\Meu Drive\Fotos\Screenshots\Screenshot_20220905-230413.png',
                    '33 - G:\Meu Drive\Fotos\Screenshots\Screenshot_20220905-230421.png',
                    '34 - G:\Meu Drive\Fotos\Screenshots\Screenshot_20220905-230429.png',
                    '35 - G:\Meu Drive\Fotos\Screenshots\Screenshot_20220905-230438.png',
                    '36 - G:\Meu Drive\Fotos\Screenshots\Screenshot_20220905-230447.png',
                    '37 - G:\Meu Drive\Fotos\Screenshots\Screenshot_20220906-084506.png',
                    '38 - G:\Meu Drive\Fotos\Screenshots\Screenshot_20220906-084514.png',
                    '39 - G:\Meu Drive\Fotos\Screenshots\Screenshot_20220906-084528.png',
                    '40 - G:\Meu Drive\Fotos\Screenshots\Screenshot_20220906-085620.png',
                    '41 - G:\Meu Drive\Fotos\Screenshots\Screenshot_20220906-085629.png',
                    '42 - G:\Meu Drive\Fotos\Screenshots\Screenshot_20220906-085652.png',
                    '43 - G:\Meu Drive\Fotos\Screenshots\Screenshot_20220906-120235.png',
                    '44 - G:\Meu Drive\Fotos\Screenshots\Screenshot_20220906-120242.png',
                    '45 - G:\Meu Drive\Fotos\Screenshots\Screenshot_20220907-152348.png',
                    '46 - G:\Meu Drive\Fotos\Screenshots\Screenshot_20220907-205301.png',
                    '47 - G:\Meu Drive\Fotos\Screenshots\Screenshot_20220908-121826.png',
                    '48 - G:\Meu Drive\Fotos\Screenshots\Screenshot_20220912-184236.png',
                    '49 - G:\Meu Drive\Fotos\Screenshots\Screenshot_20220913-152835.png',
                    '50 - G:\Meu Drive\Fotos\Screenshots\Screenshot_20220913-230819.png',
                    '51 - G:\Meu Drive\Fotos\Screenshots\Screenshot_20220913-230828.png',
                    '52 - G:\Meu Drive\Fotos\Screenshots\Screenshot_20220913-230835.png',
                    '53 - G:\Meu Drive\Fotos\Screenshots\Screenshot_20220913-233007.png',
                    '54 - G:\Meu Drive\Fotos\Screenshots\Screenshot_20220913-233415.png')

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
class DocumentoPDF:
    def __init__(self):
        self.arquivo_pdf = str('Relatorio_' + data + '_' + hora + '.pdf')
        self.relatorio_pdf = canvas.Canvas('arquivo_pdf.pdf', pagesize=A4)

    def criando_documento(self):
        self.relatorio_pdf.drawCentredString(300, 800, f"Relatorio {data_atual}")
        self.relatorio_pdf.line(x_linha, y_linha, x_linha + 500, y_linha)  # Primeira linha
        self.relatorio_pdf.line(x_linha, y_linha - 730, x_linha + 500, y_linha - 730)  # Última linha
        self.relatorio_pdf.getPageNumber()
        self.texto_indice = self.relatorio_pdf.beginText(x_txt, y_txt)
        self.texto_string = self.relatorio_pdf.beginText(x_txt + 15, y_txt)
        self.relatorio_pdf.drawText(self.texto_string)
        self.relatorio_pdf.showPage()

    def add_dados(self):
        for valor in categorias_busca:
            self.texto_string.textLine(valor)


obj_inicio = DocumentoPDF()
obj_inicio.relatorio_pdf.save()
