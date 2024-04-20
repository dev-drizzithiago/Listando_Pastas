import os.path
from tkinter.filedialog import askdirectory
from pathlib import Path
lista_da_busca = []
lista_dados = []
pasta_de_busca = Path(str(askdirectory()))

for resultado_busca in pasta_de_busca.glob('**/*'):
    if resultado_busca.is_file():
        lista_da_busca.append(resultado_busca)

for valor in lista_da_busca:
    valor_arquivo = str(valor).split('\\')[-1].strip()
    valor_pasta_lista = str(valor).split('\\')[:-2]
    valor_pasta = (str(valor_pasta_lista).replace('[', '').replace(']', '').
                   replace(',', '\\').replace("'", '').replace(' ', '').
                   replace('\\', '/').strip())
    
    lista_dados = [valor_pasta, valor_arquivo]

    print(lista_dados)
duplicado = dict()
for valor in lista_dados:
    if str(valor).split('\\')[-1].strip() in duplicado:
        duplicado[str(valor).split('\\')[-1].strip()] += 1
    else:
        duplicado[str(valor).split('\\')[-1].strip()] = 1
for k, v in duplicado.items():
    if v > 1:
        print(f'{k} - {v}')

for i in range(0, len(lista_dados) - 1):
    comparacao_1 = lista_dados[i]
    if comparacao_1 == lista_dados[i + 1]:
        print(f'{comparacao_1}')
