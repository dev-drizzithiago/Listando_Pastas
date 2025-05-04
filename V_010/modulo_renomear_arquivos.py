import os
import pymediainfo
from tkinter.filedialog import askdirectory

def renomeando_arquivos(PASTA_SELECIONADA):
    indice = 1
    for item in os.listdir(PASTA_SELECIONADA):
        CAMINHO_ABS_ORIGINAL = rf'{PASTA_SELECIONADA}\{item}'
        CAMINHO_ABS_MODIFICADO = rf'{PASTA_SELECIONADA}'

        info = pymediainfo.MediaInfo.parse(CAMINHO_ABS_ORIGINAL)
        for track in info.tracks:
            if track.track_type == "General":
                print(track.to_data())
                print(track.file_extension)
                try:
                    os.rename(
                        CAMINHO_ABS_ORIGINAL, rf'{CAMINHO_ABS_MODIFICADO}\{indice}.novo_nome.{track.file_extension}'
                    )
                    return True
                except:
                    return False

        indice += 1
        # print(CAMINHO_ABS_ORIGINAL)

