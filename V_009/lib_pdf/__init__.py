from reportlab.lib.enums import TA_JUSTIFY
from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image, PageBreak
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import mm
from tkinter.filedialog import askdirectory
from tkinter.simpledialog import askstring
from tkinter.messagebox import showinfo
from pathlib import Path

home = Path.home()
diretorio_arquivo_save = Path(home, 'Downloads')


def descompactado_dados(dados_1):
    print('ºººº' * 20)
    for valor in dados_1:
        print('teste', valor)
    input('digite')
    criando_documento_pdf(dados_1)


def criando_documento_pdf(busca_caletada):
    """Escolhendo as informações para salvar o arquivo"""
    showinfo('AVISA!', 'Escolha o direto para salvar o documento')
    nome_arquivo_pdf = askstring('Imprestante!', 'Digite o nome do arquivo')
    pdf_diretorio_save = str(diretorio_arquivo_save + nome_arquivo_pdf + '.pdf')
    print(pdf_diretorio_save)

    print(busca_caletada)

    """ Criando o Arquivos PDF"""
    lista_teste = [busca_caletada]

    # ----------------------------------------------------------------------
    def numero_paginas(janela, documento):
        """Adicionao número de paginas"""
        num_pag = janela.getPageNumber()
        pagina = f'Pagina {num_pag}'
        janela.drawRightString(200 * mm, 20 * mm, pagina)

    # ----------------------------------------------------------------------
    def documento_PDF():
        """Salvando as informações no documento"""
        doc = SimpleDocTemplate(pdf_diretorio_save, pagezsize=A4, rightMargin=72, leftMargin=72,
                                topMargin=72, bottomMargin=18)
        estilo = getSampleStyleSheet()
        estilo.add(ParagraphStyle(name='Justify', alignment=TA_JUSTIFY))

        dados_save = []

        for dados in lista_teste:
            texto = f'<font size="12">%s</font>' % dados
            dados_save.append(Paragraph(texto, estilo["Justify"]))
            dados_save.append(Spacer(1, 10))

        doc.build(dados_save, onFirstPage=numero_paginas, onLaterPages=numero_paginas)
        print('Finalizado!')

    if __name__ == '__main__':
        documento_PDF()

# criando_documento_pdf(['Thiago', 'alves'], 'Zenny', 'Enzo')
