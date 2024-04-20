lista_dados = ['Users\Thiago\OneDrive\Documentos\SimCity\Pictures ==> SPARK_2024-01-31_14-12-49.PNG',
               'Users\Thiago\OneDrive\Documentos\SimCity\Pictures ==> SPARK_2024-02-02_16-32-27.PNG',
               'Users\Thiago\OneDrive\Documentos\SimCity\Pictures ==> SPARK_2024-02-07_20-36-40.PNG',
               'Users\Thiago\OneDrive\Documentos\SimCity\Pictures ==> SPARK_2024-02-12_08-25-13.PNG',
               'Users\Thiago\OneDrive\Documentos\SimCity\Pictures ==> SPARK_2024-01-31_14-12-49.PNG',
               'Users\Thiago\OneDrive\Documentos\SimCity\Pictures ==> SPARK_2024-02-02_16-32-27.PNG',
               'Users\Thiago\OneDrive\Documentos\SimCity\Pictures ==> SPARK_2024-02-07_20-36-40.PNG',
               'Users\Thiago\OneDrive\Documentos\SimCity\Pictures ==> SPARK_2024-02-12_08-25-13.PNG',
               'Users\Thiago\OneDrive\Documentos\SimCity\Pictures ==> SPARK_2024-01-31_14-12-49.PNG',
               'Users\Thiago\OneDrive\Documentos\SimCity\Pictures ==> SPARK_2024-02-02_16-32-27.PNG',
               'Users\Thiago\OneDrive\Documentos\SimCity\Pictures ==> SPARK_2024-02-07_20-36-40.PNG',
               'Users\Thiago\OneDrive\Documentos\SimCity\Pictures ==> SPARK_2024-02-12_08-25-13.PNG',
               'Users\Thiago\OneDrive\Documentos\SimCity\Pictures ==> SPARK_2024-01-31_14-12-49.PNG',
               'Users\Thiago\OneDrive\Documentos\SimCity\Pictures ==> SPARK_2024-02-02_16-32-27.PNG',
               'Users\Thiago\OneDrive\Documentos\SimCity\Pictures ==> SPARK_2024-02-07_20-36-40.PNG',
               'Users\Thiago\OneDrive\Documentos\SimCity\Pictures ==> SPARK_2024-02-12_08-25-13.PNG']

for valor in lista_dados:
    valor_arquivo = str(valor).split('==>')[-1].strip()
    valor_pasta = str(valor).split('==>')[0].strip()

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
