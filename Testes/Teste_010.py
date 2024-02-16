from reportlab.pdfgen import canvas


# ----------------------------------------------------------------------------------------------------------------------
def criandoMultiPaginas():
    documento_pdf = canvas.Canvas('documento_teste.pdf')

    for i in range(3):
        num_pagina = documento_pdf.getPageNumber()
        texto_pg = 'Está é a pagina %s' % num_pagina
        documento_pdf.drawString(100, 750, texto_pg)
        documento_pdf.showPage()
    documento_pdf.save()


# ----------------------------------------------------------------------------------------------------------------------
if __name__ == '__main__':
    criandoMultiPaginas()
