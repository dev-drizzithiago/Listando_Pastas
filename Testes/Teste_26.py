import os
import pathlib
import ffmpeg
import pymediainfo


"""


O método `.run()` no `ffmpeg-python` executa o comando FFmpeg gerado pelo código, processando o arquivo de 
entrada e aplicando as transformações configuradas. Ele é essencial para que as operações sejam realmente executadas! 
Algumas opções interessantes que você pode usar:

### 🔧 **Principais opções do `.run()`**
1. **Executar normalmente**:
   ```python
   ffmpeg.input("video.mp4").output("video_editado.mp4").run()
   ```
   Aqui, FFmpeg processa o vídeo e cria um novo arquivo com as alterações.

2. **Forçar sobrescrição** (`overwrite_output=True`):
   ```python
   ffmpeg.input("video.mp4").output("video.mp4").run(overwrite_output=True)
   ```
   Essa opção evita que FFmpeg pergunte se você quer substituir um arquivo existente.

3. **Capturar saída e erro do FFmpeg** (`capture_stdout=True`, `capture_stderr=True`):
   ```python
   processo = ffmpeg.input("video.mp4").output("video_editado.mp4").run(capture_stdout=True, capture_stderr=True)
   stdout, stderr = processo
   print("Saída:", stdout)
   print("Erros:", stderr)
   ```
   Isso é útil para depuração, caso FFmpeg retorne erros.

4. **Modo assíncrono (`async=True`)**:
   ```python
   ffmpeg.input("video.mp4").output("video_editado.mp4").run(async=True)
   ```
   Executa o comando em segundo plano sem bloquear o restante do código Python.

💡 Quer modificar outra funcionalidade ou explorar algo específico? Me avisa! 🚀
"""

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
                    rf'{CAMINHO_ABS_MODIFICADO}/{indice}.{CAMINHO_ABS_MODIFICADO[indice - 1]} - {track.other_duration[0]}', metadado=f'title={item}'
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
