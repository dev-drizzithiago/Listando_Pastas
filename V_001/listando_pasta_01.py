from pathlib import Path
from re import search

lista_arquivos_listados = []
lista_pastas_listadas = []
cont_arq = 1
cont_path = 1

caminho_busca = 'Z:\\Thiago\\'
busca_geral = Path(caminho_busca)

for valor_busca in busca_geral.glob('**/*'):
    if valor_busca.is_dir():
        print('\n')
        nome_pasta = valor_busca.name
    elif valor_busca.is_file():
        nome_arquivo = valor_busca.name
        print(f'{cont_arq} - {nome_arquivo}')
        cont_arq += 1

