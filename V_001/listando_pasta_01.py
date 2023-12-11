from os import listdir, chdir, getcwd, walk
from time import sleep
from re import search, match
from pathlib import Path
from os.path import isfile, isdir

lista_arquivos_listados = []
lista_pastas_listadas = []

caminho_busca = 'Z:\\Thiago\\Fotos\\'

for path, diretorios, arquivos in walk(caminho_busca):
    print(arquivos)
