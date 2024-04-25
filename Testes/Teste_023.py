import os, hashlib


def duplicados(path, extension):
    ret = {}

    # Para cada arquivo no diretorio
    for filename in os.listdir(path):

        # Somente arquivos com a extensão desejada
        if filename.endswith(extension):

            # Monta o caminho completo do arquivo
            fullpath = os.path.abspath(os.path.join(path, filename))

            # Calcula o hash MD5 (assinatura) do arquivo
            with open(fullpath, 'rb') as f:
                md5sum = hashlib.md5(f.read()).hexdigest()

            # Adiciona arquivo em um dicionário de listas
            # no qual a chave eh a assinatura do arquivo
            if md5sum not in ret:
                ret[md5sum] = []
            ret[md5sum].append(fullpath)

    # Filtra e retorna somente arquivos duplicados
    return {k: v for k, v in ret.items() if len(v) > 1}


print(duplicados(path='D:\\Scripts_Python\\Nova pasta\\', extension='.jpg'))
