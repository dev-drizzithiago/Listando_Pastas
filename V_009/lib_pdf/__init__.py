from reportlab.lib.enums import TA_JUSTIFY
from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import mm
from pathlib import Path
from tkinter.messagebox import showinfo, showerror

import matplotlib.pyplot

home = Path.home()
diretorio_arquivo_save = str(Path(home, 'Downloads'))


"""# Grafico"""
# _+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+


# ----------------------------------------------------------------------
def numero_paginas(janela, documento):
    """Adicionao número de paginas"""
    num_pag = janela.getPageNumber()
    pagina = f'Pagina {num_pag}'
    janela.drawRightString(200 * mm, 20 * mm, pagina)


# ----------------------------------------------------------------------
def documento_PDF(valor_dados_coletados='<Sem dados coletados>', valor_nome_documento='nome desconhecido',
                  valor_qtd_extensao='Sem dados coletados', valor_qtd_arq_pasta='Sem dados coletados'):
    print(f'teste {valor_qtd_extensao}')
    """Criando parametros para savar o arquivo no diretorio 'DOWNLOADS' do windows. """
    nome_arquivo_pdf = str(valor_nome_documento)
    pdf_diretorio_save = diretorio_arquivo_save + "\\" + nome_arquivo_pdf + '.pdf'
    print(f'Diretorio de SAVE - [{pdf_diretorio_save}]')
    print('Aguarde! Documento esta sendo criado!')
    try:
        """Salvando as informações no documento"""
        doc = SimpleDocTemplate(pdf_diretorio_save, pagezsize=A4, rightMargin=72, leftMargin=72,
                                topMargin=72, bottomMargin=18)
        estilo = getSampleStyleSheet()
        estilo.add(ParagraphStyle(name='Justify', alignment=TA_JUSTIFY))

        separado = '-=-' * 35
        dados_save = []

        """# Separação"""
        texto = f'<font size="16">%s</font>' % 'ARQUIVOS ENCONTRADOS'
        dados_save.append(Spacer(1, 20))
        dados_save.append(Paragraph(texto, estilo['Justify']))
        dados_save.append(Spacer(1, 5))
        dados_save.append(Paragraph(separado, estilo['Normal']))
        dados_save.append(Spacer(1, 5))

        """# Abaixo são contabilizados a quantidade de EXTENSÕES encontradas"""
        for dados_extensao in valor_qtd_extensao:
            texto = f'<font size="12">%s</font>' % dados_extensao
            dados_save.append(Paragraph(texto, estilo["Normal"]))
            dados_save.append(Spacer(1, 10))

        """# Separação"""
        texto = f'<font size="16">%s</font>' % 'Quantidade de Extenções encontradas'
        dados_save.append(Spacer(1, 30))
        dados_save.append(Paragraph(texto, estilo['Justify']))
        dados_save.append(Spacer(1, 5))
        dados_save.append(Paragraph(separado, estilo['Normal']))
        dados_save.append(Spacer(1, 5))

        """# Abaixo são contabilizados a quantidade de arquivos encontrado em cada pasta"""
        for dados_qtd_ext in valor_qtd_arq_pasta:
            texto = f'<font size="12">%s</font>' % dados_qtd_ext
            dados_save.append(Paragraph(texto, estilo["Normal"]))
            dados_save.append(Spacer(1, 10))

        """# Separaãção"""
        texto = f'<font size="16">%s</font>' % 'Quantidade de arquivos por PASTAS'
        dados_save.append(Spacer(1, 30))
        dados_save.append(Paragraph(texto, estilo['Justify']))
        dados_save.append(Spacer(1, 5))
        dados_save.append(Paragraph(separado, estilo['Normal']))
        dados_save.append(Spacer(1, 5))

        """# Abaixo, são adicionado os dados da busca no documento"""
        for dados_busca in valor_dados_coletados:
            texto = f'<font size="12">%s</font>' % dados_busca
            dados_save.append(Paragraph(texto, estilo["Justify"]))
            dados_save.append(Spacer(1, 10))

        """# Linhas responsavel por adicionar mais paginas, conforme for adicionando os textos"""
        doc.build(dados_save, onFirstPage=numero_paginas, onLaterPages=numero_paginas)

        print('\nFinalizado! \nArquivos criado com sucesso!')
        showinfo('Parabens!', f'O documento foi salvo com sucesso na pasta [{"Downloads"}]')
    except:
        print(f'ERROR: Não foi possível gravar o documento {pdf_diretorio_save}')
        showerror("ERROR", f'Não foi possível gravar o documento {pdf_diretorio_save}')


if __name__ == '__main__':
    documento_PDF()
