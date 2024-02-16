from reportlab.lib.enums import TA_JUSTIFY
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image, PageBreak
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import mm


# ----------------------------------------------------------------------------------------------------------------------
class PageNumCanvas(canvas.Canvas):
    """
    http://code.activestate.com/recipes/546511-page-x-of-y-with-reportlab/
    http://code.activestate.com/recipes/576832/
    """

    # ------------------------------------------------------------------------------------------------------------------
    def __init__(self, *args, **kwargs):
        """Construção"""
        canvas.Canvas.__init__(self, *args, **kwargs)
        self.paginas = []

    # ------------------------------------------------------------------------------------------------------------------
    def showPagina(self):
        """ Em uma quebra de página, adicione informações à lista """
        self.paginas.append(dict(self.__dict__))
        self._startPage()

    # ------------------------------------------------------------------------------------------------------------------
    def save(self):
        """ Adicione o número da página a cada página (página x de y) """
        contagem_paginas = len(self.paginas)
        for pagina in self.paginas:
            self.__dict__.update(pagina)
            self.draw_page_number(contagem_paginas)
            canvas.Canvas.showPage()
        canvas.Canvas.save()

    # ------------------------------------------------------------------------------------------------------------------
    def draw_page_number(self, contagem_paginas):
        """Adicione o número da página"""
        pagina = f'Pagina {self._pageNumber, contagem_paginas}'
        self.setFont("Helvetica", 9)
        self.drawRightString(195 * mm, 272 * mm, pagina)


# ----------------------------------------------------------------------------------------------------------------------
def criandoMultiPaginas():
    """Criando diversas paginas"""
    documento = SimpleDocTemplate("documento_v2.pdf", pagesize=A4,
                                  rightMargin=50, leftMargin=50, topMargin=50, bottomMargin=15)
    Estilo = getSampleStyleSheet()
    Estilo.add(ParagraphStyle(name='Justify', alignment=TA_JUSTIFY))

    Story = list()

    margem_nome = 'Teste'
    emitir_numero = 12
    preco = '12.00'
    data_limite = '03/05/2024'
    presente = 'Chapeu de palha'
    nome_completo = "Drizz't Do'Urden"
    endereco = ['Mg Pinheiros', 'São Paulo']

    for pagina in range(5):
        # Criar endereço de retorno
        p_texto = '<font size="12">%s</font>' % nome_completo
        Story.append(Paragraph(p_texto, Estilo['Normal']))
        for end in endereco:
            p_texto = '<font size="12">%s</font>' % end.strip()
            Story.append(Paragraph(p_texto, Estilo['Normal']))

        Story.append(Spacer(1, 12))
