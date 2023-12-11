from os import listdir
from pathlib import Path
from re import search, match

pasta_home = Path.home()
subpastas = Path()

for listando in listdir(pasta_home):
    resultado = search('BAT', listando)
    if resultado:
        print(listando)

