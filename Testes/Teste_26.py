import os
import pathlib


PASTA_VIDEOS_AS_AVENTURAS_TITIN = pathlib.Path(r'\\muonline\Mini_CELERON\Videos\Classicos\As Aventuras de Tintin Completo')

for item in os.listdir(PASTA_VIDEOS_AS_AVENTURAS_TITIN):
    print(os.stat(rf'{PASTA_VIDEOS_AS_AVENTURAS_TITIN}\{item}').st_size)
