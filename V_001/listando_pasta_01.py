from pathlib import Path
from re import search
from time import sleep
from threading import Timer
from tkinter.filedialog import askopenfilename, askdirectory

lista_arquivos_listados = []
lista_pastas_listadas = []
cont_arq_total = 1
cont_arq = 1
cont_path = 1


def diretorio():
    diretorio_escolhido = askdirectory()
    return diretorio_escolhido


caminho_busca = Timer(diretorio(), 1)
busca_geral = Path(caminho_busca)
for valor_busca in busca_geral.glob('**/*'):
    if valor_busca.is_dir():
        nome_pasta = valor_busca.name
        print(f'[{cont_path}] - [{nome_pasta}]')
        cont_path += 1
        cont_arq += 1
    elif valor_busca.is_file():
        nome_arquivo = valor_busca.name
        status_arq = valor_busca.stat().st_size
        print(f'<{cont_arq}> - <{nome_arquivo}>')
        cont_arq += 1
        cont_arq_total += 1
print(f'Foram encontrados ao total de {cont_path} arquivos em {cont_path} pastas')
