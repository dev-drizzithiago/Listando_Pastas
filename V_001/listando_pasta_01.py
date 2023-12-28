from pathlib import Path
from time import sleep
from tkinter.filedialog import askopenfilename, askdirectory

lista_arquivos_listados = []
lista_pastas_listadas = []
cont_arq_total = 0
cont_arq = 0
cont_path = 0


def diretorio():
    diretorio_escolhido = askdirectory()
    return diretorio_escolhido


def end_diretorio():
    return Path(diretorio())


print('_-_' * 16)
valor_arquivo = input('Digite a extensão do arquivo: ')
if len(valor_arquivo) != 0:
    valor_arquivo = '.' + valor_arquivo

busca_geral = end_diretorio()
print(f'Busca pelos arquivos [{valor_arquivo}], no diretório [{busca_geral}]')
sleep(1)
for valor_busca in busca_geral.glob('**/*' + valor_arquivo):
    if valor_busca.is_dir():
        nome_pasta = valor_busca.name
        cont_path += 1
        cont_arq += 1
        print(f'[{cont_path}] - [{nome_pasta}]')
    elif valor_busca.is_file():
        nome_arquivo = valor_busca.name
        status_arq = valor_busca.stat().st_size
        cont_arq += 1
        cont_arq_total += 1
        print(f'<{cont_arq}> - <{nome_arquivo}>')
print(f'Foram encontrados ao total de {cont_path} arquivos em {cont_path} pastas')
