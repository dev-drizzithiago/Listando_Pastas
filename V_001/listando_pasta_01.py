from os import listdir, chdir, getcwd
from time import sleep
# from tkinter import
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
    if search('jpg', listagem):
        print(listagem)
    elif search('mp4', listagem):
        print(listagem)
    else:
        sub_pasta = locais() + listagem
        print(f'Listando diretorio {sub_pasta} ')
        sleep(1)
        for listagem_sub in listdir(sub_pasta):
            print(listagem_sub)
