import tkinter
from tkinter import *
from tkinter.ttk import *
from datetime import datetime
from tkinter.simpledialog import *
from tkinter.messagebox import *

valor_hora = datetime.now()
data_certa = valor_hora.strftime('%D/%M/%Y')
hora_certa = valor_hora.strftime('%H:%M')


class ListandoPastas:
    def __init__(self):
        # Variaveis geral
        self.categorias = ('Todos', 'Arquivos de Vídeo', 'Arquivo Imagem', 'Arquivos de Leitura',
                           'Arquivos execução', 'Arquivos compreesão')
        self.extensoes_imagem = (
            'JPG', 'PNG', 'GIF', 'BMP', 'Bitmap', 'TIFF', 'RAW', 'EXIF', 'PPM', 'PGM', 'PBM', 'PNM',
            'SVG', 'WebP',)
        self.extensoes_videos = ('MP4', 'AVI', 'MKV', 'MOV', 'WMV', 'FLV', 'AVCHD', 'F4V', 'SWF', 'WEBM', 'HTML5',
                                 'WEBM')
        self.extensoes_arq_txt = (
            'TXT', 'PDF', 'DOCX', 'DOC', 'HTML', 'HTM', 'ODT', 'XLS', 'XLSX', 'ODS', 'PPT', 'PPTX')
        self.extensoes_de_app = ('EXE', 'DLL', 'IN', 'BAT')
        self.extensoes_compreensao = ('ZIP', '')

        # janela princpal
        janela_principal = Tk()
        janela_principal.geometry('350x390')
        janela_principal.config(padx=5, pady=5)
        janela_principal.title('V_008')

        # Relogio
        label_frame_relogio = LabelFrame(janela_principal, text='Hora Certa')
        label_frame_relogio.pack(anchor='center', fill=BOTH)
        label_hora = Label(label_frame_relogio, text=f'{data_certa} - {hora_certa}', justify='center')
        label_hora.pack(anchor='center')

        # Combo
        variavel_combo = StringVar()
        label_frame_combo = LabelFrame(janela_principal, text='Categorias de arquivos')
        label_frame_combo.pack(fill=BOTH)

        combo_principal = Combobox(label_frame_combo, textvariable=variavel_combo, justify='center')
        combo_principal['values'] = self.categorias
        combo_principal.set('Escolha uma categoria')
        combo_principal.pack(fill=BOTH, pady=5, padx=5)

        # lista principal
        label_frame_lista = LabelFrame(janela_principal, text='Escolha uma extensão')
        label_frame_lista.pack(side='top', fill=BOTH)
        lista_principal = Listbox(label_frame_lista)
        lista_principal.pack(fill=BOTH, pady=3, padx=3)

        # Botoes
        label_frame_botao_princial = LabelFrame(janela_principal, text="Escolha uma Opcão")
        label_frame_botao_princial.pack(fill=BOTH)
        label_frame_iniciar_busca = LabelFrame(label_frame_botao_princial, text='Buscando por arquivos')
        label_frame_iniciar_busca.pack(side='top', fill=BOTH)
        botao_iniciar_busca = Button(label_frame_iniciar_busca, text='Iniciar busca')
        botao_iniciar_busca.pack(anchor='center', pady=3, padx=3, fill=BOTH)

        janela_principal.mainloop()


obj_principal = ListandoPastas()
