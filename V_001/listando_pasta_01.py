from os import listdir
from pathlib import Path
from re import search, match

pasta_home = Path.home()
subpastas = Path()
arquivos = ['pdf']
lista_arquivos = []

for listando in listdir(pasta_home):
    if search(arquivos, listando):
        print(listando)

