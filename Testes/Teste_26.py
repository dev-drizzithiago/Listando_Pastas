import os
import pathlib
import stat
import subprocess
import json

import pymediainfo

LISTA_EPISODIOS_AS_AVENTURAS_TINTIN = [
    'O Caranguejo das Tenazes de Ouro (primeira parte)',
    'O Caranguejo das Tenazes de Ouro (segunda parte)',
    'O Segredo do Licorne (primeira parte)',
    'O Segredo do Licorne (segunda parte)',
    'O Tesouro de Rackham o Terrível',
    'Os Charutos do Faraó (primeira parte)',
    'Os Charutos do Faraó (segunda parte)',
    'O Lótus Azul (primeira parte)',
    'O Lótus Azul (segunda parte)',
    'A Ilha Negra (primeira parte)',
    'A Ilha Negra (segunda parte)',
    'O Caso Girassol (primeira parte)',
    'O Caso Girassol (segunda parte)',
    'A Estrela Misteriosa',
    'O Ídolo Roubado (primeira parte)',
    'O Ídolo Roubado (segunda parte)',
    'O Cetro de Ottokar (primeira parte)',
    'O Cetro de Ottokar (segunda parte)',
    'Tintim no Tibete (primeira parte)',
    'Tintim no Tibete (segunda parte)',
    'Tintim e os Pícaros (pt-BR Tintim e os Tímpanos) (primeira parte)',
    'Tintim e os Pícaros (pt-BR Tintim e os Tímpanos) (segunda parte)',
    'Tintim no País do Ouro Negro (primeira parte)',
    'Tintim no País do Ouro Negro (segunda parte)',
    'Voo 714 para Sydney (primeira parte)',
    'Voo 714 para Sydney (segunda parte)',
    'Perdidos no Mar (primeira parte)',
    'Perdidos no Mar (segunda parte)',
    'As Sete Bolas de Cristal (primeira parte)',
    'As Sete Bolas de Cristal (segunda parte)',
    'O Templo do Sol (primeira parte)',
    'O Templo do Sol (segunda parte)',
    'As Jóias de Castafiore (primeira parte)',
    'As Joias de Castafiore (segunda parte)',
    'Rumo à Lua (primeira parte)',
    'Rumo à Lua (segunda parte)',
    'Explorando a Lua (primeira parte)',
    'Explorando a Lua (segunda parte)',
    'Tintim na América (último episódio)',
]
PASTA_VIDEOS_AS_AVENTURAS_TITIN = pathlib.Path(
    r'\\muonline\Mini_CELERON\Videos\Classicos\As Aventuras de Tintin Completo'
)

for item in os.listdir(PASTA_VIDEOS_AS_AVENTURAS_TITIN):
    CAMINHO_ABS = rf'{PASTA_VIDEOS_AS_AVENTURAS_TITIN}\{item}'

    informacao_arquivo = os.stat(rf'{CAMINHO_ABS}')

    # COMANDO_SHELL = rf'ffprobe -v quiet -print_format json -show_format -show_streams {CAMINHO_ABS}'
    # resultado = subprocess.run(COMANDO_SHELL, shell=True, capture_output=True, text=True)
    # metadados = json.loads(resultado.stdout)
    # print(json.dumps(metadados, indent=4))

    info = pymediainfo.MediaInfo.parse(CAMINHO_ABS)

    for track in info.tracks:
        if os.path.isfile(CAMINHO_ABS):
            if track.track_type == 'General':
                print(track.title)
        else:
            print('Não pode verificar uma pasta')
