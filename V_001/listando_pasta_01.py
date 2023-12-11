from os import listdir, chdir, getcwd
from time import sleep
from re import search, match
from pathlib import Path
from os.path import isfile

lista_arquivos_listados = []
lista_pastas_listadas = []


def locais():
    caminho = 'Z:\\Thiago\\Fotos\\Sexo\\'
    return caminho


local_busca = locais()

for listagem in listdir(local_busca):
    print(listagem)

