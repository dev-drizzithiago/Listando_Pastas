from tkinter import *
from tkinter.ttk import *
from pathlib import Path
from tkinter.filedialog import *
from tkinter.messagebox import *
from tkinter.simpledialog import *


class ListagemPastas:
    def __init__(self):
        # Varias Global
        self.pasta_home = Path.home()
        self.pastas_arquivos_extensao = Path(self.pasta_home, 'AppData', 'LocalLow', 'extensoes')
        self.lista_tipos_extensoes = ('VÍDEOS', 'IMAGENS', 'ARQUIVOS_LEITURA')

        # Janela principa
        self.janela_principal = Tk()
        self.janela_principal.geometry('300x390')
        self.janela_principal.title('V_007')
        self.janela_principal.resizable(False, False)

        # Label Frame
        self.label_frame_001 = Frame(self.janela_principal)
        self.label_frame_002 = Frame(self.janela_principal)
        self.label_frame_003 = Frame(self.janela_principal)
        self.label_frame_004 = Frame(self.janela_principal)
        self.label_frame_001.pack(anchor='n', fill='both')
        self.label_frame_002.pack(anchor='center', fill='both')
        self.label_frame_003.pack()

        self.label_titulo_principal = Label(self.label_frame_001, text='MERCURTY TI', justify='center')
        self.label_titulo_principal.pack(side='top', fill='both')

        # Lista Combo principal
        self.var_cambo = StringVar()
        self.combo_tipo_arquivo_principal = Combobox(self.label_frame_001, textvariable=self.var_cambo, justify='center')
        self.combo_tipo_arquivo_principal['values'] = self.lista_tipos_extensoes
        self.combo_tipo_arquivo_principal.set('Escolha um tipo de Mídia')
        self.combo_tipo_arquivo_principal.pack(side='top', fill='both')
        self.combo_tipo_arquivo_principal.current()
        self.var_cambo.trace('w', self.lista_tipos_extensoes)

        # Lista de exntesão
        self.lista_extensao = Listbox(self.label_frame_002, justify='center')
        self.lista_extensao.pack(side='top', fill='both', padx=5, pady=5)

        self.botao_iniciar_busca = Button(self.label_frame_003, text='Iniciar Busca')
        self.botao_adicionar_extensao = Button(self.label_frame_003, text='Adicionar Extensões')
        self.botao_iniciar_busca.pack(fill='both', padx=3, pady=3)
        self.botao_adicionar_extensao.pack(fill='both', padx=3, pady=3)

        # Looping janela
        self.janela_principal.mainloop()

    #def opcao_midia(self, *args):
    #    self.criando_registro_extensoes(self.combo_tipo_arquivo.get())

    def criando_registro_extensoes(self):

        self.janela_add_extensao = Tk()
        self.janela_add_extensao.geometry('400x300')
        self.janela_add_extensao.title('Adicionando uma extensão')

        self.label_frame_add_001 = LabelFrame(self.janela_add_extensao)
        self.label_frame_add_001.pack(fill='both')

        self.var_cambo = StringVar()
        self.combo_tipo_arquivo = Combobox(self.label_frame_001, textvariable=self.var_cambo, justify='center')
        self.combo_tipo_arquivo['values'] = self.lista_tipos_extensoes
        self.combo_tipo_arquivo.set('Escolha um tipo de Mídia')
        self.combo_tipo_arquivo.pack(side='top', fill='both')
        self.combo_tipo_arquivo.current()
        self.var_cambo.trace('w', self.lista_tipos_extensoes)

        if valor_extensao == 'VÍDEOS':
            valor = '\\ext_videos.txt'
        elif valor_extensao == 'IMAGENS':
            valor = '\\ext_imagem.txt'
        elif valor_extensao == 'ARQUIVOS_LEITURA':
            valor = '\\ext_arquivos.txt'

        try:
            valor_arq_txt = open(self.pastas_arquivos_extensao + valor, 'a')
            valor_arq_txt.write(f'')
        except FileNotFoundError:
            showerror('AVISO!', 'Arquivo não foi encontrado!')


obj_principal = ListagemPastas()
