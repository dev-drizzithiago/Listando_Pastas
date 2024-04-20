from tkinter.filedialog import askdirectory
from pathlib import Path

lista_dados = []
pasta_de_busca = Path(str(askdirectory()))

for resultado_busca in pasta_de_busca.glob('**/*'):
    if resultado_busca.is_file():
        lista_dados.append(resultado_busca)
        print(resultado_busca)

for valor in lista_dados:
    valor_arquivo = str(valor).split('\\')[-1].strip()
    valor_pasta = str(valor).split('\\')[:-2]

duplicado = dict()
for valor in lista_dados:
    if str(valor).split('==>')[-1].strip() in duplicado:
        duplicado[str(valor).split('==>')[-1].strip()] += 1
    else:
        duplicado[str(valor).split('==>')[-1].strip()] = 1
for k, v in duplicado.items():
    if v > 1:
        print(f'{k} - {v}')

for i in range(0, len(lista_dados) - 1):
    comparacao_1 = lista_dados[i]
    if comparacao_1 == lista_dados[i + 1]:
        print(f'{comparacao_1}')
