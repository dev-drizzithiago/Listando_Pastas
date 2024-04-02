"""# Modulos para PDF"""
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_JUSTIFY
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from pathlib import Path

"""# Modulo PANDAS"""
import pandas as pd

"""# Modulos GERAL"""
from tkinter.messagebox import showinfo, showerror


home = Path.home()
diretorio_arquivo_save = str(Path(home, 'Downloads'))

"""# Modulo Grafico"""
import matplotlib.pyplot as plt

# _+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+


# ----------------------------------------------------------------------
def numero_paginas(janela, documento):
    """Adicionao número de paginas"""
    num_pag = janela.getPageNumber()
    pagina = f'Pagina {num_pag}'
    janela.drawRightString(200 * mm, 20 * mm, pagina)


# ----------------------------------------------------------------------
def documento_PDF(valor_dados_coletados=None, valor_nome_documento=None, valor_qtd_extensao=None,
                  valor_qtd_arq_pasta=None, valor_ext_grafico=None):

    """# Análise dos valores que chagaram até a funnção"""
    print(f'\nAnalise "valor_dados_coletados" \n>{valor_dados_coletados}<')
    print(f'\nAnalise "valor_nome_documento" \n>{valor_nome_documento}<')
    print(f'\nAnalise "valor_qtd_extensao" \n>{valor_qtd_extensao}<')
    print(f'\nAnalise "valor_qtd_arq_pasta" \n>{valor_qtd_arq_pasta}<')
    print(f'\nAnalise "valor_ext_grafico" \n.{valor_ext_grafico}<')

    """# As condições abaixo, são responsável para que, caso execulte o programa nessa parte, não ocorra erros"""
    if valor_qtd_extensao is None:
        valor_qtd_extensao = ['Sem', 'dados', 'para', 'analisar']

    if valor_qtd_arq_pasta is None:
        valor_qtd_arq_pasta = ['Sem', 'dados', 'para', 'analisar']

    if valor_nome_documento is None:
        valor_nome_documento = 'nome desconhecido'

    if valor_dados_coletados is None:
        valor_dados_coletados = ['Sem', 'dados', 'para', 'analisar']

    if valor_ext_grafico is None:
        valor_ext_grafico = ['jpg=3927', 'txt=113', 'conf=2', 'rdp=29', 'pdf=235', 'jpeg=16', 'png=77', 'xlsx=29',
                             'docx=6', 'p7s=1', 'pptx=6', 'xps=2', 'zip=3', 'rar=10', 'kdbx=2', 'html=10', 'exe=2',
                             'msi=3', 'evtx=2', 'msg=2', 'gif=5', 'xls=1', 'mov=1', 'mp4=2']

    """# Declaração Variaveis"""
    extensao = list()
    quantidade = list()

    dict_valores_graficos = {'Extensao': None, 'Quantidade': None}

    """# Lendos arquivo 'valor_ext_grafico"""
    for dividindo_valores in valor_ext_grafico:
        extensao.append(dividindo_valores.split('=')[0])
        quantidade.append(dividindo_valores.split('=')[1])
        dict_valores_graficos['Extensao'] = extensao
        dict_valores_graficos['Quantidade'] = quantidade

    """# Teste de Grafico"""
    grafico_pizza = 'Maça', 'Banana', 'uva', 'Goiaba'
    valores_pizza = [3, 5, 10, 9]
    teste_1, teste_2 = plt.subplots()
    teste_2.pie(valores_pizza, labels=grafico_pizza)

    """# Apenas testes com pandas"""
    df_1 = pd.Series(quantidade, index=extensao)
    df_2 = pd.DataFrame(dict_valores_graficos)

    print(f'\n{df_1}\n')
    print(f'\n{df_2}\n')

    """Criando parametros para savar o arquivo no diretorio 'DOWNLOADS' do windows. """
    nome_arquivo_pdf = str(valor_nome_documento)
    pdf_diretorio_save = diretorio_arquivo_save + "\\" + nome_arquivo_pdf + '.pdf'

    print(f'Arquivos vai ser criado no diretório - [{pdf_diretorio_save}]')
    print('Aguarde! Documento esta sendo criado!')

    """#### Criando documento PDF principal"""
    try:
        """Salvando as informações no documento"""
        doc = SimpleDocTemplate(pdf_diretorio_save, pagezsize=A4, rightMargin=72, leftMargin=72, topMargin=72,
                                bottomMargin=18)
        estilo = getSampleStyleSheet()
        estilo.add(ParagraphStyle(name='Justify', alignment=TA_JUSTIFY))

        separado = '-=-' * 35
        dados_save = []

        """# Separação"""
        texto = f'<font size="16">%s</font>' % 'Quantidade de Extenções encontradas'
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
        texto = f'<font size="16">%s</font>' % 'Quantidade de arquivos por PASTAS'
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

        """# Separação"""
        texto = f'<font size="16">%s</font>' % 'ARQUIVOS ENCONTRADOS'
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
