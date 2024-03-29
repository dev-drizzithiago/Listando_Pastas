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
    canvas.drawRightString(200 * mm, 208 * mm, texto)


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
    presente = 'Chapeu de palha'
    nome_completo = "Drizz't Do'Urden"
    endereco = ['Mg Pinheiros', 'São Paulo']

    for pagina in range(5):
        ptexto = nome_completo
        Story.append(Paragraph(ptexto, estilo["Normal"]))
        for parte in endereco:
            ptexto = parte.strip()
            Story.append(Paragraph(ptexto, estilo["Normal"]))
        Story.append(Spacer(1, 12))

        ptexto = f'     Sr. {nome_completo.split()[0].strip()}'
        Story.append(Paragraph(ptexto, estilo['Normal']))
        Story.append(Spacer(1, 1))

        ptexto = """<font size="12">Gostaríamos de lhe dar as boas-vindas à nossa base de assinantes para a revista %s! 
        Você receberá %s edições na excelente introdução preço de $%s. Por favor, 
        responda até %s para começar a receber sua assinatura e ganhe o seguinte presente grátis: %s.</font>"""
        ptexto = ptexto % (margem_nome, emitir_numero, preco, data_limite, presente)
        Story.append(Paragraph(ptexto, estilo["Normal"]))
        Story.append(Spacer(1, 12))

        ptexto = '<font size="12">Muito obrigado e estamos ansiosos para atendê-lo.</font>'
        Story.append(Paragraph(ptexto, estilo['Justify']))
        Story.append(Spacer(1, 12))

        ptexto = '<font size="12">Atenciosamente,</font>'
        Story.append(Paragraph(ptexto, estilo['Normal']))
        Story.append(Spacer(1, 12))

        ptexto = '<font size="12"> Seu otário </font>'
        Story.append(Paragraph(ptexto, estilo['Normal']))
        Story.append(Spacer(1, 12))
        Story.append(PageBreak())

    doc.build(Story, onFirstPage=addNumeroPaginas, onLaterPages=addNumeroPaginas)


# ----------------------------------------------------------------------------------------------------------------------
if __name__ == "__main__":
    criando_multi_paginas()
