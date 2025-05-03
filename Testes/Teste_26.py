import os
import pathlib
import subprocess
import json


PASTA_VIDEOS_AS_AVENTURAS_TITIN = pathlib.Path(r'\\muonline\Mini_CELERON\Videos\Classicos\As Aventuras de Tintin Completo')

for item in os.listdir(PASTA_VIDEOS_AS_AVENTURAS_TITIN):
    # print(os.stat(rf'{PASTA_VIDEOS_AS_AVENTURAS_TITIN}\{item}').st_dev)

    COMANDO_SHELL = f'ffprobe -v quiet -print_format json -show_format -show_streams {item}'

    resultado = subprocess.run(COMANDO_SHELL, shell=True, capture_output=True, text=True)
    metadados = json.loads(resultado.stdout)

    print(json.dumps(metadados, indent=4))

