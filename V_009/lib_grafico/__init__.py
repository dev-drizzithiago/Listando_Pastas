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
linhas_divisao = '-=-' * 20
lista_quantidade = list()
lista_extensao = list()
valor_qtd_int = list()


def arquivos_em_pandas(valor_extensao_pandas):
    """# Declaração interna"""
    dict_valores_graficos_PANDAS = dict()

    print(f'{linhas_divisao}\n')
    print(f'Iniciando salvamento em EXCEL')
    print(f'Dados entrandono no função "valor_extensao_pandas: [{valor_extensao_pandas}]')

    """# Apenas testes com pandas"""
    for dividinho_ext_qtd_pandas in valor_extensao_pandas:
        print(f"Dados no loop 'dividinho_ext_qtd_pandas': {str(dividinho_ext_qtd_pandas)}")
        lista_extensao.append(str(dividinho_ext_qtd_pandas).split('=')[0].strip())
        lista_quantidade.append(str(dividinho_ext_qtd_pandas).split('=')[1].strip())

    """# Adicionando os dados no dicionario PANDAS"""
    dict_valores_graficos_PANDAS['Extensão'] = lista_extensao
    dict_valores_graficos_PANDAS['Quantidade'] = lista_quantidade

    """# Analise dos valores do arquivo; server para o desenvolvedor analisar como os dados estão chegando"""
    print(f'Valor da "lista_exntesao": {lista_extensao}')
    print(f'Valor da "lista_quantidade": {lista_quantidade}')

    df_1 = pd.Series(lista_quantidade, index=lista_extensao)
    df_2 = pd.DataFrame(dict_valores_graficos_PANDAS)

    print(f'\n{df_1}\n')
    print(f'\n{df_2}\n')
    print('Dados salvos com sucesso na planilha!!\n')
    print(f'{linhas_divisao}\n')


def grafico_pizza(valor_extensao_pizza=None):
    """# Declaração interna"""
    dict_valores_graficos_PIZZA = dict()

    """#### Iniciando função"""
    print(f'\nIniciando grafico de [PIZZA]')
    print(f'Valores dos dados: {valor_extensao_pizza}')
    if valor_extensao_pizza is None:
        valor_extensao_pizza = ['dados=1']

    """# Divide os valores que vão chegar da busca"""
    for valor_divisao_extensao_PIZZA in valor_extensao_pizza:
        print(f"\nDados no loop 'dividindo_ext_qtd': {str(valor_divisao_extensao_PIZZA)}")
        lista_extensao.append(str(valor_divisao_extensao_PIZZA).split('=')[0].strip())
        lista_quantidade.append(str(valor_divisao_extensao_PIZZA).split('=')[1].strip())

    """# Adiciona os valores dentro do dicionário"""
    dict_valores_graficos_PIZZA['Extensão'] = lista_extensao
    dict_valores_graficos_PIZZA['Quantidade'] = lista_quantidade

    """# Analise dos valores do arquivo; server para o desenvolvedor analisar como os dados estão chegando"""
    print(f'Valor da "lista_exntesao": {lista_extensao}')
    print(f'Valor da "lista_quantidade": {lista_quantidade}')
    print(f'Valor do "dict_valores_graficos": {dict_valores_graficos_PIZZA}')

    """# Transforma os dados números que chegam como string em inteiros(int)"""
    for valor_inteiro in lista_quantidade:
        valor_qtd_int.append(int(valor_inteiro))

    """#### Teste grafico pizza"""
    """# Criando a representação, plotagem"""
    fig, ax = plt.subplots(figsize=(10, 5), subplot_kw=dict(aspect='equal'))

    """# Abaixo a função vai ser responsavel ela porcentagem dos valores"""

    def func(pct, allvals):
        """# Calc %"""
        absoluto = int(pct / 100. * np.sum(allvals))
        """# Legendao do grafico com %"""
        return "{:.1f}%\n({:d})".format(pct, absoluto)

    """# Criando o grafico e colocand as legendas"""
    wedges, textos, texto_auto = ax.pie(valor_qtd_int, textprops=dict(color="w"),
                                        autopct=lambda pct: func(pct, valor_qtd_int))

    """# Define a caixa de legenda externa, titulos, localização e onde vai ancorar o box"""
    ax.legend(wedges, lista_extensao, title='Valores da busca', loc="center left", bbox_to_anchor=(1, 0, 0.5, 1))

    """# Define o tamanho do texto dentro do grafico """
    plt.setp(texto_auto, size=6, weight='bold')

    """# Titulo do grafico"""
    ax.set_title('Extensões encontradas')

    """# Rodando o grafico"""
    plt.show()
    PlaySound('Exclamation', SND_ASYNC)
    showinfo("Parabéns!", "Grafico apresentado. \nRealize outra busca!")

    """# Encaminhando dados para pandas; Salvando em EXCEL"""
    print(f'Dados sendo encaminhados para salvar em planilha')
    sleep(1)
    Thread(target=arquivos_em_pandas(valor_extensao_pizza)).start()

    """# Limpeza das listas"""
    del lista_extensao[:]
    del lista_quantidade[:]
    del valor_qtd_int[:]
    print(f'Valor das lista: extensao {lista_extensao} \nquantidade {lista_quantidade}')
    print(f'{linhas_divisao}\n')


def grafico_barras(valor_extensao_barras=None):
    """# Declaração interna"""
    dict_valores_graficos_BARRA = dict()
    print(f'\nIniciando grafico de [Barras]')
    print(f'Valores dos dados: {valor_extensao_barras}')
    if valor_extensao_barras is None:
        valor_extensao_barras = ['dados=1']

    for valor_divisao_extensao_BARRAS in valor_extensao_barras:
        print(f"Dados no loop 'dividindo_ext_qtd': {str(valor_divisao_extensao_BARRAS)}")
        lista_extensao.append(str(valor_divisao_extensao_BARRAS).split('=')[0].strip())
        lista_quantidade.append(str(valor_divisao_extensao_BARRAS).split('=')[1].strip())

    """# Adiciona os valores dentro do dicionário"""
    dict_valores_graficos_BARRA['Extensão'] = lista_extensao
    dict_valores_graficos_BARRA['Quantidade'] = lista_quantidade

    """# Analise dos valores do arquivo; server para o desenvolvedor analisar como os dados estão chegando"""
    print(f'Valor da "lista_exntesao": {lista_extensao}')
    print(f'Valor da "lista_quantidade": {lista_quantidade}')
    print(f'Valor do "dict_valores_graficos": {dict_valores_graficos_BARRA}')

    for valor_inteiro in lista_quantidade:
        valor_qtd_int.append(int(valor_inteiro))

    """### Grafico barras"""
    """# Montando o grafico em barras"""
    plt.bar(lista_extensao, valor_qtd_int, color='red')

    """# Define a legenda de cada barro, no exio X"""
    plt.xticks(lista_extensao)

    """# A label para o eixo Y"""
    plt.ylabel('Quantidade encontrada')

    """# A label para o eixo X"""
    plt.xlabel('Extensões')

    """# Titulo do Grafico"""
    plt.title('Valor da busca')

    """# Rodando o grafico"""
    plt.show()
    showinfo("Parabéns!", "Grafico apresentado. \nRealize outra busca!")
    PlaySound('Exclamation', SND_ASYNC)

    print(f'{linhas_divisao}\n')
    """# Encaminhando dados para pandas; Salvando em EXCEL"""
    print(f'Dados sendo encaminhados para salvar em planilha')
    sleep(1)
    Thread(target=arquivos_em_pandas(valor_extensao_barras)).start()

    """# Limpeza das listas"""
    del lista_extensao[:]
    del lista_quantidade[:]
    del valor_qtd_int[:]
    print(f'Valor das lista: extensao {lista_extensao} \nquantidade {lista_quantidade}')
    print(f'{linhas_divisao}\n')


if __name__ == '__main__':
    grafico_barras()
    grafico_pizza()
