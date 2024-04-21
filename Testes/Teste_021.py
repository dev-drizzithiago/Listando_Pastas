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
    caminho_destino = 'C:/Users/Thiago/OneDrive/Documentos/Duplicados/'
    print(caminho_destino)
    os.mkdir(caminho_destino)
except FileNotFoundError:
    caminho_destino = 'C:/Users/Thiago/OneDrive/Documentos/Duplicados/'
    os.mkdir(caminho_destino)
except FileExistsError:
    pass

pasta_de_busca = Path(str(askdirectory(title='Escolha uma pasta')))

for raiz, subdir, item in os.walk(pasta_de_busca):
    