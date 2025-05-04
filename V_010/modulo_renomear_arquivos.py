import os
import pymediainfo
from tkinter.filedialog import askdirectory
PASTA_SELECIONADA_TESTE = r'\\muonline\Mini_CELERON\Videos\Novos\11 - 22 - 63 2016 - 1ª Temporada'
def renomeando_arquivos(PASTA_SELECIONADA):
    indice = 1
    for item in os.listdir(PASTA_SELECIONADA):
        CAMINHO_ABS_ORIGINAL = rf'{PASTA_SELECIONADA}\{item}'
        CAMINHO_ABS_MODIFICADO = rf'{PASTA_SELECIONADA}'

        info = pymediainfo.MediaInfo.parse(CAMINHO_ABS_ORIGINAL)
        for track in info.tracks:
            if track.track_type == "General":
                try:
                    os.rename(
                        CAMINHO_ABS_ORIGINAL, rf'{CAMINHO_ABS_MODIFICADO}\{indice}.novo_nome.{track.file_extension}'
                    )
                    return True
                except:
                    return False

        indice += 1


if __name__ == '__main__':
    renomeando_arquivos(PASTA_SELECIONADA_TESTE)
