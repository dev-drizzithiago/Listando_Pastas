import os
import pymediainfo

from tkinter.filedialog import askdirectory
PASTA_SELECIONADA_TESTE = r'\\muonline\Mini_CELERON\Videos\Novos\11 - 22 - 63 2016 - 1ª Temporada'
ARQUIVO_PARA_RENOMEAR_TESTE = r'D:\Estudos\Python\GitHub\Listando_Pastas\V_010\lista_episodios_tintin.txt'

def renomeando_arquivos(PASTA_SELECIONADA, ARQUIVO_PARA_RENOMEAR):
    indice = 1
    arquivo_aberto = open(ARQUIVO_PARA_RENOMEAR, 'r', encoding='utf8')
    for item_titulo in arquivo_aberto.readlines():
        print(item_titulo)
    arquivo_aberto.close()

    for item in os.listdir(PASTA_SELECIONADA):

        CAMINHO_ABS_ORIGINAL = rf'{PASTA_SELECIONADA}\{item}'
        CAMINHO_ABS_MODIFICADO = rf'{PASTA_SELECIONADA}'

        info = pymediainfo.MediaInfo.parse(CAMINHO_ABS_ORIGINAL)
        for track in info.tracks:
            if track.track_type == "General":
                try:
                    os.rename(
                        CAMINHO_ABS_ORIGINAL, rf'{CAMINHO_ABS_MODIFICADO}\{indice}.{''}.{track.file_extension}'
                    )
                    return True
                except:
                    return False

        indice += 1


if __name__ == '__main__':
    renomeando_arquivos(PASTA_SELECIONADA_TESTE, ARQUIVO_PARA_RENOMEAR_TESTE)
