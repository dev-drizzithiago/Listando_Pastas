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

        # Relogio
        label_frame_relogio = LabelFrame(janela_principal, text='Hora Certa')
        label_frame_relogio.pack(anchor='center', fill=BOTH)
        label_hora = Label(label_frame_relogio, text=f'{data_certa} - {hora_certa}', justify='center')
        label_hora.pack(anchor='center')

        # Combo
        variavel_combo = StringVar()
        label_frame_combo = LabelFrame(janela_principal, text='Categorias de arquivos')
        label_frame_combo.pack(fill=BOTH)

        combo_principal = Combobox(label_frame_combo, textvariable=variavel_combo)
        combo_principal['values'] = self.categorias
        combo_principal.set('Escolha uma categoria')
        combo_principal.pack()

        # lista principal
        label_frame_lista = LabelFrame(janela_principal, text='Escolha uma extensão')
        label_frame_lista.pack(side='top', fill=BOTH)
        lista_principal = Listbox(label_frame_lista)
        lista_principal.pack(fill=BOTH, pady=3, padx=3)

        janela_principal.mainloop()


obj_principal = ListandoPastas()
