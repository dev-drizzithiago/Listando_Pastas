from reportlab.lib.enums import TA_JUSTIFY
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image, PageBreak
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import mm


class PageNumCanvas(canvas.Canvas):
    """
    http://code.activestate.com/recipes/546511-page-x-of-y-with-reportlab/
    http://code.activestate.com/recipes/576832/
    """

    def __init__(self, *args, **kwargs):
        """Construção"""
        canvas.Canvas.__init__(self, *args, **kwargs)
        self.paginas = []

    def showPagina(self):
        """ Em uma quebra de página, adicione informações à lista """
        self.paginas.append(dict(self.__dict__))
        self._startPagina()
        