from reportlab.pdfgen import canvas


def criando_relatorio_pdf(relatorio, data, hora):
    relatorio_pdf = canvas.Canvas(f'Relatorio')
