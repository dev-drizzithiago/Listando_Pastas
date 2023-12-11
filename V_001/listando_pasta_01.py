from os import listdir, chdir, getcwd
from re import search, match
from pathlib import Path
from os.path import isfile

pasta_home = 'Z:\\Thiago\\Fotos\\Sexo'
lista_arquivos_listados = []
lista_pastas_listadas = []

for c in listdir(pasta_home):
    if search('jpg', c):
        print(c)
    elif search('mp4', c):
        print(c)
