from os import listdir
from pathlib import Path
from re import search, match

pasta_home = Path.home()
subpastas = Path()
arquivos = ['pdf', 'jpg']
lista_arquivos = []

for registrando in listdir(pasta_home):
    lista_arquivos.append(registrando)

for busca in lista_arquivos:
    resultado = match(arquivos, busca)
    if resultado:
        print(busca)

