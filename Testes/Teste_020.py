import os.path
from tkinter.filedialog import askdirectory
from pathlib import Path

lista_da_busca = []
lista_dados = []
duplicado = dict()
pasta_de_busca = Path(str(askdirectory()))

for resultado_busca in pasta_de_busca.glob('**/*'):
    if resultado_busca.is_file():
        lista_da_busca.append(resultado_busca)

for valor in lista_da_busca:
    valor_pasta_lista = str(valor).split('\\')[:-2]
    lista_dados.append((str(valor_pasta_lista))
                       .replace('[', '')
                       .replace(']', '')
                       .replace(',', '\\')
                       .replace("'", '')
                       .replace(' ', '')
                       .replace('\\', '/')
                       .strip())

    lista_dados.append(str(valor).split('\\')[-1].strip())

for indice in range(0, 2, len(lista_dados)):
    valor_item = lista_dados[indice]

    print(f'Indice:{indice} - {valor_item}')
    if valor_item in duplicado:
        duplicado[valor_item] += 1
    else:
        duplicado[valor_item] = 1
for k, v in duplicado.items():
    if v > 1:
        print(f'{k} - {v}')

for i in range(0, len(lista_dados) - 1):
    comparacao_1 = lista_dados[i]
    if comparacao_1 == lista_dados[i + 1]:
        print(f'{comparacao_1}')
