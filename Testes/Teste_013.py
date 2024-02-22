"""cria um path tree para o folder atual desse script"""
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')


def print_directory_tree(root_dir, padding=''):
    """
    Imprime a árvore de diretórios a partir do diretório especificado.

    Args:
        root_dir (str): O caminho para o diretório raiz a ser impresso.
        padding (str, optional): O espaçamento que será utilizado para identar
        os subdiretórios. Default é ''.

    Returns:
        None
    """

    # Obter o nome da pasta raiz
    head, tail = os.path.split(root_dir)
    if tail == ".git":
        return
    print(padding[:-1] + '+--' + tail + '/')

    # Listar os arquivos e pastas dentro do diretório raiz
    file_list = os.listdir(root_dir)

    # Ordenar a lista para que as pastas apareçam primeiro
    file_list.sort(key=lambda x: os.path.isdir(os.path.join(root_dir, x)))

    # Percorrer a lista de arquivos e pastas
    for file_name in file_list:
        full_path = os.path.join(root_dir, file_name)
        # Se for uma pasta, chamar a função recursivamente
        if os.path.isdir(full_path):
            print_directory_tree(full_path, padding + '|   ')
        # Se for um arquivo, imprimir o nome
        else:
            print(padding + '|-- ' + file_name)


# Exemplo de uso
print_directory_tree('.')
