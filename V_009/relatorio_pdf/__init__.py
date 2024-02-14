from reportlab.pdfgen import canvas


def criando_relatorio_pdf(relatorio, pasta_destino, data, hora):
    print(relatorio, pasta_destino, data, hora)
    relatorio_pdf = canvas.Canvas(f'Relatorio-{data}-{hora}.pdf')
    relatorio_pdf.drawString(10, 200, "Relatorios")
    relatorio_pdf.save()
