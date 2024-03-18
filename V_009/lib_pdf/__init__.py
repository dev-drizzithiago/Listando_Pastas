from reportlab.lib.enums import TA_JUSTIFY
from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image, PageBreak
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import mm
from pathlib import Path

home = Path.home()
diretorio_arquivo_save = str(Path(home, 'Downloads'))


def descompactado_dados(dados_1, nome_pdf):
    criando_documento_pdf(dados_1, nome_pdf)


def criando_documento_pdf(busca_caletada, nome_arquivo_PDF):
    """Escolhendo as informações para salvar o arquivo"""
    nome_arquivo_pdf = nome_arquivo_PDF

    pdf_diretorio_save = diretorio_arquivo_save + "\\" + nome_arquivo_pdf + '.pdf'

    for valor in busca_caletada:
        print(valor)

    """ Criando o Arquivos PDF"""
    documento_PDF(busca_caletada, pdf_diretorio_save)


# ----------------------------------------------------------------------
def numero_paginas(janela, documento):
    """Adicionao número de paginas"""
    num_pag = janela.getPageNumber()
    pagina = f'Pagina {num_pag}'
    janela.drawRightString(200 * mm, 20 * mm, pagina)


# ----------------------------------------------------------------------
def documento_PDF(valor_dados_coletados, diretorio_save):
    print(valor_dados_coletados)
    print(diretorio_save)
    """Salvando as informações no documento"""
    doc = SimpleDocTemplate(diretorio_save, pagezsize=A4, rightMargin=72, leftMargin=72,
                            topMargin=72, bottomMargin=18)
    estilo = getSampleStyleSheet()
    estilo.add(ParagraphStyle(name='Justify', alignment=TA_JUSTIFY))

    dados_save = []

    for dados in valor_dados_coletados:
        texto = f'<font size="8">%s</font>' % dados
        dados_save.append(Paragraph(texto, estilo["Justify"]))
        dados_save.append(Spacer(1, 10))

    doc.build(dados_save, onFirstPage=numero_paginas, onLaterPages=numero_paginas)

    print('Finalizado!')


'''if __name__ == '__main__':
    documento_PDF()'''

# criando_documento_pdf(['Thiago', 'alves'])
