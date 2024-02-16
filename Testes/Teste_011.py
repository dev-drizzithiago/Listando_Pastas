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
