from reportlab.pdfgen import canvas


def criando_relatorio_pdf():
    relatorio_pdf = canvas.Canvas(f'Relatorio')
