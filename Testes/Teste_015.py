import os

pastas = os.listdir()
total = 0
arq = open("lista_de_arquivos.txt", "w", encoding="utf-8")


def listar_pasta(pasta):
    tot = 0
    subpastas = list()
    if os.path.isdir(pasta):
        items = os.listdir(pasta)
        print("\n\nARQUIVOS NA PASTA '" + str(pasta).upper() + "' :", end='\n\n')
        arq.write("ARQUIVOS NA PASTA '" + str(pasta).upper() + "': \n")
        for item in items:
            novo_item = os.path.join(pasta, item)
            if os.path.isdir(novo_item):
                subpastas.append(novo_item)
                continue
            print(item)
            arq.write(item + "\n")
            tot += 1
        for subpasta in subpastas:
            tot += listar_pasta(subpasta)
    arq.write("\n")
    return tot


if __name__ == '__main__':
    for pasta in pastas:
        total += listar_pasta(pasta)
    print("Total de arquivos: " + str(total))
    arq.write("# Total de arquivos : " + str(total))
    arq.close()
