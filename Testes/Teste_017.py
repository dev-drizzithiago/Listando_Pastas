import matplotlib.pyplot as plt

meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho']
valores = [9, 5, 10, 2, 0, 8]

plt.plot(meses, valores)
plt.show()


"""# Teste de Grafico"""
grafico_pizza = 'Maça', 'Banana', 'uva', 'Goiaba'
valores_pizza = [3, 5, 10, 9]
teste_1, teste_2 = plt.subplots()
teste_2.pie(valores_pizza, labels=grafico_pizza)