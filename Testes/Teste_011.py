from reportlab.lib.enums import TA_JUSTIFY
from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image, PageBreak
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import mm


# from reportlab.pdfgen import canvas

# ----------------------------------------------------------------------------------------------------------------------
def addNumeroPaginas(canvas, doc):
    """ Adicionando número de páginas """
    num_pag = canvas.getPageNumber()
    texto = "Pagina #%s" % num_pag
    canvas.drawRightString(200*mm, 208*mm, texto)


# ----------------------------------------------------------------------------------------------------------------------
def criando_multi_paginas():
    """Criando diversas paginas"""
    doc = SimpleDocTemplate('doc_pag_num.pdf', pagesize=A4,
                            rightMargin=72, leftMargin=72,
                            topMargin=72, bottomMargin=18)
    estilo = getSampleStyleSheet()
    estilo.add(ParagraphStyle(name='Justify', alignment=TA_JUSTIFY))

    Story = []

    margem_nome = 'Teste'
    emitir_numero = 12
    preco = '12.00'
    data_limite = '03/05/2024'
    presente = 'Chave de palha'
    nome_completo = "Drizz't Do'Urden"
    endereco = ['Mg Pinheiros', 'São Paulo']

    for pagina in range(5):
        ptexto = '<font size="12">%s</font>' % nome_completo
        Story.append(Paragraph(ptexto, estilo["Normal"]))
        for parte in endereco:
            ptexto = '<font size="12">%s</font>' % parte.strip()
            Story.append(Paragraph(ptexto, estilo["Normal"]))
