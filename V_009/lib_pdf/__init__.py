from reportlab.lib.enums import TA_JUSTIFY
from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image, PageBreak
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import mm
from pathlib import Path

home = Path.home()
diretorio_arquivo_save = str(Path(home, 'Downloads'))


# ----------------------------------------------------------------------
def numero_paginas(janela, documento):
    """Adicionao número de paginas"""
    num_pag = janela.getPageNumber()
    pagina = f'Pagina {num_pag}'
    janela.drawRightString(200 * mm, 20 * mm, pagina)


# ----------------------------------------------------------------------
def documento_PDF(valor_dados_coletados='<desconhecido>', nome_documento='desconhecido'):
    """Criando parametros para savar o arquivo no diretorio 'DOWNLOADS' do windows. """
    nome_arquivo_pdf = str(nome_documento)
    pdf_diretorio_save = diretorio_arquivo_save + "\\" + nome_arquivo_pdf + '.pdf'
    print(f'Diretorio de SAVE - [{pdf_diretorio_save}]')

    """Nas duas linhas abaixo, vai mostrar os testes estão tudo correto"""
    for valor in valor_dados_coletados:
        print(valor)

    """Salvando as informações no documento"""
    doc = SimpleDocTemplate(pdf_diretorio_save, pagezsize=A4, rightMargin=72, leftMargin=72,
                            topMargin=72, bottomMargin=18)
    estilo = getSampleStyleSheet()
    estilo.add(ParagraphStyle(name='Justify', alignment=TA_JUSTIFY))

    dados_save = []

    for dados in valor_dados_coletados:
        texto = f'<font size="12">%s</font>' % dados
        dados_save.append(Paragraph(texto, estilo["Justify"]))
        dados_save.append(Spacer(1, 10))

    doc.build(dados_save, onFirstPage=numero_paginas, onLaterPages=numero_paginas)

    print('Finalizado!')


if __name__ == '__main__':
    documento_PDF()
