import pandas as pd
import matplotlib.pyplot as plt


valor_ext_grafico = ['txt=10', 'pdf=7','log=1',
                     'png=2', 'jpg=9', 'zip=1',
                     'rar=1', 'mp4=11', 'jpeg=1']

"""# Declaração Variaveis"""
extensao = list()
quantidade = list()
valor_quantidade_int = list()

dict_valores_graficos = {'Extensao': None, 'Quantidade': None}

"""# Lendos arquivo 'valor_ext_grafico"""
for dividindo_valores in valor_ext_grafico:
    extensao.append(str(dividindo_valores.split('=')[0]).strip())
    quantidade.append(str(dividindo_valores.split('=')[1]).strip())
    dict_valores_graficos['Extensao'] = extensao

for valor in quantidade:
    valor_quantidade_int.append(int(valor))
    dict_valores_graficos['Quantidade'] = valor_quantidade_int

print(dict_valores_graficos)

print(extensao)
print(quantidade)

df = pd.DataFrame(dict_valores_graficos)
df.plot(kind='bar')
print(df)
plt.show()

