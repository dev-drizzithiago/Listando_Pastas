import os
import pymediainfo
from tkinter.filedialog import askdirectory

def renomeando_arquivos(PASTA_SELECIONADA):
    indice = 1
    for item in os.listdir(PASTA_SELECIONADA):
        CAMINHO_ABS_ORIGINAL = rf'{PASTA_SELECIONADA}\{item}'
        CAMINHO_ABS_MODIFICADO = rf'{PASTA_SELECIONADA}'

        # ffmpeg.input(CAMINHO_ABS_ORIGINAL).output(
        #     CAMINHO_ABS_MODIFICADO, metadata=f"title={LISTA_EPISODIOS_AS_AVENTURAS_TINTIN[indice - 1]}"
        # ).run(overwrite_output=True)

        info = pymediainfo.MediaInfo.parse(CAMINHO_ABS_ORIGINAL)
        print(item)
        for track in info.tracks:
            if track.track_type == "General":
                print(track.to_data())
                print(track.file_extension)

                os.rename(CAMINHO_ABS_ORIGINAL, rf'{CAMINHO_ABS_MODIFICADO}\{indice}.novo_nome.{track.file_extension}')

        indice += 1
        # print(CAMINHO_ABS_ORIGINAL)
