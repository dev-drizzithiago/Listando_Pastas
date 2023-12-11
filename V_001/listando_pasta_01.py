from pathlib import Path
from re import search

lista_arquivos_listados = []
lista_pastas_listadas = []

caminho_busca = 'Z:\\Thiago\\'
busca_geral = Path(caminho_busca)

for valor_busca in busca_geral.glob('**/*'):
    if valor_busca.is_file():
        print(valor_busca.name)
    elif valor_busca.is_dir():
        print('\n')
        print(f'Pasta - [{valor_busca.name}]')
