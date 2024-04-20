import os
from tkinter.filedialog import askdirectory
from pathlib import Path
import glob
import shutil

lista_da_busca = []
lista_dados = []
duplicado = dict()
home = Path.home()

try:
    caminho_destino = Path(home, 'OneDrive', 'Documentos', 'Duplicados')
    print(caminho_destino)
    os.mkdir(str(caminho_destino).replace('\\', '/'))
except FileNotFoundError:
    caminho_destino = Path(home, 'OneDrive', 'Documentos', 'Duplicados\\')
    os.mkdir(str(caminho_destino).replace('\\', '/'))
except FileExistsError:
    print(f"Pasta ja existe! \n{str(caminho_destino).replace('\\', '/')}")

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

for indice in range(0, len(lista_dados)):
    valor_item = lista_dados[indice]

    if indice % 2 == 0:
        valor_diretorio = lista_dados[indice]
        print(f'Indice:{indice} - {valor_diretorio}')
    else:
        print(f'Indice:{indice} - {valor_item}')
        caminho_origem = str(valor_diretorio + '/' + valor_item)
        arquivos = glob.glob(caminho_origem)
        print(f'Caminho de origem: {caminho_origem}')
        print('=-=' * 20)

    if valor_item in duplicado:
        duplicado[valor_item] += 1
        try:
            shutil.move(caminho_origem, caminho_destino)
            print('Arquivo movido!')
        except:
            print('Não foi possível mover os arquivos para pasta de destino!')
    else:
        duplicado[valor_item] = 1

for k, v in duplicado.items():
    if v > 1:
        print(f'Arquivos repetidos: {k}')

print('=-=' * 20)

for i in range(0, len(lista_dados) - 1):
    comparacao_1 = lista_dados[i]
    if comparacao_1 == lista_dados[i + 1]:
        print(f'{comparacao_1}')
