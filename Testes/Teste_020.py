lista_dados = [
    'C:\\Users\Thiago\OneDrive\Documentos\SimCity\Pictures ==> SPARK_2024-01-31_14-12-49.PNG',
    'C:\\Users\Thiago\OneDrive\Documentos\SimCity\Pictures ==> SPARK_2024-02-02_16-32-27.PNG',
    'C:\\Users\Thiago\OneDrive\Documentos\SimCity\Pictures ==> SPARK_2024-02-07_20-36-40.PNG',
    'C:\\Users\Thiago\OneDrive\Documentos\SimCity\Pictures ==> SPARK_2024-02-12_08-25-13.PNG',
    'C:\\Users\Thiago\OneDrive\Documentos\SimCity\Pictures ==> SPARK_2024-01-31_14-12-49.PNG',
    'C:\\Users\Thiago\OneDrive\Documentos\SimCity\Pictures ==> SPARK_2024-02-02_16-32-27.PNG',
    'C:\\Users\Thiago\OneDrive\Documentos\SimCity\Pictures ==> SPARK_2024-02-07_20-36-40.PNG',
    'C:\\Users\Thiago\OneDrive\Documentos\SimCity\Pictures ==> SPARK_2024-02-12_08-25-13.PNG'
]

lista_dados.sort()

for valor in lista_dados:
    valor_arquivo = str(valor).split('==>')[-1].strip()
    valor_pasta = str(valor).split('==>')[0].strip()


duplicado = dict()
for valor in lista_dados:
    if valor in duplicado:
        duplicado[valor] += 1
    else:
        duplicado[valor] = 1
for k, v in duplicado.items():
    if v > 1:
        print(f'{k} - {v}')

for i in range(0, len(lista_dados) - 1):
    comparacao_1 = lista_dados[i]
    if comparacao_1 == lista_dados[i + 1]:
        print(f'{comparacao_1}')
