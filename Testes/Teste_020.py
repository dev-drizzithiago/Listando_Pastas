tempos = [0.5, 1.3, 2.5, 3.4, 0.5]
comparacoes = []
for i in range(0, len(tempos) - 1):
    if tempos[i] == tempos[i + 1]:
        comparacoes.append(tempos[i])
print(comparacoes)
