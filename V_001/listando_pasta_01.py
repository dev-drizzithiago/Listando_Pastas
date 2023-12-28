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

busca_geral_diretorio = end_diretorio()
print(f'Busca pelos arquivos [{valor_arquivo}], no diretório [{busca_geral_diretorio}]')
sleep(1)
for valor_busca_pasta in busca_geral_diretorio.glob('**/*' + valor_arquivo):
    if valor_busca_pasta.is_dir():
        nome_pasta = valor_busca_pasta.name
        lista_pastas_listadas.append(nome_pasta)
        cont_path += 1
        print(f'[{cont_path}] - [{nome_pasta}]')
    elif valor_busca_pasta.is_file():
        nome_arquivo = valor_busca_pasta.name
        lista_arquivos_listados.append(nome_arquivo)
        status_arq = valor_busca_pasta.stat().st_size
        cont_arq += 1
        cont_arq_total += 1
        print(f'<{cont_arq}> - <{nome_arquivo}>')
print(lista_pastas_listadas)
print(lista_arquivos_listados)
print(f'Foram encontrados ao total de {cont_path} arquivos em {cont_arq} pastas')
