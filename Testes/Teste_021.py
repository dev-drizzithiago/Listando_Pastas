import os
from tkinter.filedialog import askdirectory
from pathlib import Path
import glob
import shutil
import hashlib

lista_da_busca = []
lista_dados = []
duplicado = dict()
home = Path.home()

try:
    caminho_destino = 'C:/Users/Thiago/OneDrive/Documentos/Duplicados/'
    print(caminho_destino)
    os.mkdir(caminho_destino)
except FileNotFoundError:
    caminho_destino = 'C:/Users/Thiago/OneDrive/Documentos/Duplicados/'
    os.mkdir(caminho_destino)
except FileExistsError:
    pass

pasta_de_busca = Path(str(askdirectory(title='Escolha uma pasta')))
arquivo_unico = {}
for raiz, subdir, item in os.walk(pasta_de_busca):
    for valor_do_item in item:
        caminho_arquivo = os.path.join(raiz, valor_do_item)
        hash_file = hashlib.md5(open(caminho_arquivo, 'rb').read()).hexdigest()

    if hash_file not in arquivo_unico:
        arquivo_unico[hash_file] = caminho_arquivo
    else:
        print(f'verdadeiro {caminho_arquivo}')
