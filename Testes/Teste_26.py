import os
import pathlib
import ffmpeg
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
    r'Z:\Videos\Classicos\As Aventuras de Tintin Completo'
)

indice = 1
for item in os.listdir(PASTA_VIDEOS_AS_AVENTURAS_TITIN):
    # print()
    # print(item)
    CAMINHO_ABS_ORIGINAL = rf'{PASTA_VIDEOS_AS_AVENTURAS_TITIN}\{item}'
    CAMINHO_ABS_MODIFICADO = rf'{PASTA_VIDEOS_AS_AVENTURAS_TITIN}'

    info = pymediainfo.MediaInfo.parse(CAMINHO_ABS_ORIGINAL)

    for track in info.tracks:
        if os.path.isfile(CAMINHO_ABS_ORIGINAL):
            if track.track_type == 'General':

                processo = ffmpeg.input(CAMINHO_ABS_ORIGINAL).output(
                    rf'{CAMINHO_ABS_MODIFICADO}/{indice}.{LISTA_EPISODIOS_AS_AVENTURAS_TINTIN[indice - 1]} - {track.other_duration[0]}', metadado=f'title={item}'
                ).run(overwrite_output=True, capture_stdout=True, capture_stderr=True)
                saida, error = processo
                print('Saída', saida)
                print('ERROR', error)

                indice += 1
                # print(track.title)
                # print(track.codecs_image)
                # print(track.other_duration[4])
                # print(track.to_data())

        else:
            print('Não pode verificar uma pasta')


    # print(CAMINHO_ABS_ORIGINAL)
