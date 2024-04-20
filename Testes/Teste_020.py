
lista_dados = [1, 1, 2, 3, 4, 5, 5, 6, 7, 8, 10]
lista_dados.sort()

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
    print(f'Item para comparar {comparacao_1}')
    for j in range(1, len(lista_dados) - 1):
        comparacao_2 = lista_dados[j + i]
        print(f'Item comparador {comparacao_2}')
        if comparacao_1 == comparacao_2:
            print(f'{comparacao_2}')
