"""# Modulo tkinter"""
from tkinter.messagebox import showinfo

"""# Modulo Grafico"""
import matplotlib.pyplot as plt
import numpy as np

"""# Modulo PANDAS"""
import pandas as pd

"""# Modulo Geral"""
from threading import Thread
from time import sleep
from winsound import PlaySound, SND_ASYNC

"""#### Declaração de variaveis"""
dict_valores_graficos = dict()


def arquivos_em_pandas(valor_extensao=None):
    print(f'Iniciando salvamento em EXCEL')
    print(f'Dados entrandono no função "arquivos_em_pastas: {valor_extensao}')
    if valor_extensao is None:
        valor_extensao = ['dados=1']

    """# Apenas testes com pandas"""
    for dividinho_ext_qtd in valor_extensao:
        print(f"Dados no loop 'dividindo_ext_qtd': {str(dividinho_ext_qtd)}")
        extensao = str(dividinho_ext_qtd).split('=')[0].strip()
        quantidade = str(dividinho_ext_qtd).split('=')[1].strip()
        dict_valores_graficos['Extensão'] = extensao
        dict_valores_graficos['Quantidade'] = quantidade

    df_1 = pd.Series(quantidade, index=extensao)
    df_2 = pd.DataFrame(dict_valores_graficos)
    print(f'\n{df_1}\n')
    print(f'\n{df_2}\n')


def grafico_pizza(valor_extensao=None):
    print(f'Iniciando grafico de pizza')
    print(f'Valores dos dados: {valor_extensao}')
    if valor_extensao is None:
        valor_extensao = ['dados=1']

    """# Encaminhando dados para pandas; Salvando em EXCEL"""
    print(f'Dados sendo encaminhados para salvar em planilha')
    sleep(1)
    Thread(target=arquivos_em_pandas(valor_extensao)).start()

    """# Declaração de lista"""
    extensao = list()
    quantidade = list()
    valor_qtd_int = list()

    """# Divide os valores que vão chegar da busca"""
    for valor_divisao_extensao in valor_extensao:
        print(f'Extensao: {valor_divisao_extensao.split("=")[0]}')
        print(f'Quantidade: {valor_divisao_extensao.split("=")[1]}')

        extensao.append(str(valor_divisao_extensao).split('=')[0])
        quantidade.append(str(valor_divisao_extensao).split('=')[1])

    """# Analise dos valores do arquivo; server para o desenvolvedor analisar como os dados estão chegando"""
    print(extensao)
    print(quantidade)

    """# Transforma os dados números que chegam como string em inteiros(int)"""
    for valor_inteiro in quantidade:
        valor_qtd_int.append(int(valor_inteiro))

    """#### Teste grafico pizza"""
    """# Criando a representação, plotagem"""
    fig, ax = plt.subplots(figsize=(10, 5), subplot_kw=dict(aspect='equal'))

    """# Abaixo a função vai ser responsavel ela porcentagem dos valores"""

    def func(pct, allvals):
        # Calc %
        absoluto = int(pct / 100. * np.sum(allvals))
        # Legendao do grafico com %
        return "{:.1f}%\n({:d})".format(pct, absoluto)

    """# Criando o grafico e colocand as legendas"""
    wedges, textos, texto_auto = ax.pie(valor_qtd_int, textprops=dict(color="w"),
                                        autopct=lambda pct: func(pct, valor_qtd_int))

    """# Define a caixa de legenda externa, titulos, localização e onde vai ancorar o box"""
    ax.legend(wedges, extensao, title='Valores da busca', loc="center left", bbox_to_anchor=(1, 0, 0.5, 1))

    """# Define o tamanho do texto dentro do grafico """
    plt.setp(texto_auto, size=6, weight='bold')

    """# Titulo do grafico"""
    ax.set_title('Extensões encontradas')

    """# Rodando o grafico"""
    plt.show()


def grafico_barras(valor_extensao=None):
    print(f'Iniciando grafico de Barras')
    print(f'Valores dos dados: {valor_extensao}')
    if valor_extensao is None:
        valor_extensao = ['dados=1']

    """# Encaminhando dados para pandas; Salvando em EXCEL"""
    print(f'Dados sendo encaminhados para salvar em planilha')
    sleep(1)
    Thread(target=arquivos_em_pandas(valor_extensao)).start()

    """# Declarando a lista de dados"""
    extensao = list()
    quantidade = list()
    valor_qtd_int = list()

    for valor_divisao_extensao in valor_extensao:
        print(f"{str(valor_divisao_extensao).split('=')[0].strip()}")
        print(f"{str(valor_divisao_extensao).split('=')[1].strip()}")

        extensao.append(str(valor_divisao_extensao).split('=')[0])
        quantidade.append(str(valor_divisao_extensao).split('=')[1])

    """# Analise dos valores do arquivo; server para o desenvolvedor analisar como os dados estão chegando"""
    print(extensao)
    print(quantidade)

    for valor_inteiro in quantidade:
        valor_qtd_int.append(int(valor_inteiro))

    """### Grafico barras"""
    """# Montando o grafico em barras"""
    plt.bar(extensao, valor_qtd_int, color='red')

    """# Define a legenda de cada barro, no exio X"""
    plt.xticks(extensao)

    """# A label para o eixo Y"""
    plt.ylabel('Quantidade encontrada')

    """# A label para o eixo X"""
    plt.xlabel('Extensões')

    """# Titulo do Grafico"""
    plt.title('Valor da busca')

    """# Rodando o grafico"""
    plt.show()


if __name__ == '__main__':
    arquivos_em_pandas()
