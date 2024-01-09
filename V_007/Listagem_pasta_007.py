import tkinter as tk
from tkinter.ttk import *
from pathlib import Path
from tkinter.filedialog import *
from tkinter.messagebox import showinfo, showerror, showwarning
from tkinter.simpledialog import *


class ListagemPastas:
    def __init__(self):

        # Varias Global
        self.valor_combo_add = None
        self.valor_extensao = None
        self.pasta_home = Path.home()
        self.pastas_arquivos_extensao = Path(self.pasta_home, 'AppData', 'LocalLow', 'extensoes')
        self.lista_tipos_extensoes = ('VÍDEOS', 'IMAGENS', 'ARQUIVOS_LEITURA')
        self.lista_extensao_ativa_videos = False
        self.lista_extensao_ativa_imagem = False
        self.lista_extensao_ativa_texto = False

        # Janela principa
        self.janela_principal = tk.Tk()
        self.janela_principal.geometry('300x390')
        self.janela_principal.title('V_007')
        self.janela_principal.resizable(False, False)

        # Label Frame
        self.label_frame_001 = Frame(self.janela_principal)
        self.label_frame_001.pack(anchor='n', fill='both')
        self.label_frame_002 = Frame(self.janela_principal)
        self.label_frame_002.pack(anchor='center', fill='both')
        self.label_frame_003 = Frame(self.janela_principal)
        self.label_frame_003.pack()
        self.label_frame_004 = Frame(self.janela_principal)
        self.label_frame_004.pack()

        self.label_titulo_principal = Label(self.label_frame_001, text='MERCURTY TI', justify='center')
        self.label_titulo_principal.pack(side='top', fill='both')

        # Lista Combo principal
        self.var_combo = tk.StringVar()
        self.combo_tipo_arquivo_principal = Combobox(self.label_frame_001, textvariable=self.var_combo,
                                                     justify='center')
        self.combo_tipo_arquivo_principal['values'] = self.lista_tipos_extensoes
        self.combo_tipo_arquivo_principal.set('Escolha um tipo de Mídia')
        self.combo_tipo_arquivo_principal.pack(side='top', fill='both', ipady=3, ipadx=3)
        self.combo_tipo_arquivo_principal.current()
        self.var_combo.trace('w', self.tipos_extensao)

        # Lista de exntesão
        self.lista_extensao = tk.Listbox(self.label_frame_002, justify='center')
        self.lista_extensao.pack(side='top', fill='both', padx=5, pady=5)

        # botões
        self.botao_iniciar_busca = tk.Button(self.label_frame_003, text='Iniciar Busca', command=self.janela_inicio_busca)
        self.botao_add_ext = tk.Button(self.label_frame_003, text='Adicionar Extensões', command=self.janela_adicionar_registrar)
        self.botao_sair_programa = tk.Button(self.label_frame_003, text='Sair do programa')
        self.botao_iniciar_busca.pack(fill='both', padx=3, pady=3)
        self.botao_add_ext.pack(fill='both', padx=3, pady=3)
        self.botao_sair_programa.pack(fill='both', ipady=3, ipadx=3)

        # Looping janela
        self.janela_principal.mainloop()

    def tipos_extensao(self, *args):
        valor_categoria_busca = self.var_combo.get()
        self.lista_extensao.delete('0', 'end')
        if valor_categoria_busca == 'VÍDEOS':
            self.lista_extensao.insert('0', 'MP4', 'AVI')
            self.lista_extensao_ativa_videos = True
        elif valor_categoria_busca == 'IMAGENS':
            self.lista_extensao.insert('0', 'JPG', 'PNG', 'BMP')
            self.lista_extensao_ativa_imagem = True
        elif valor_categoria_busca == 'ARQUIVOS_LEITURA':
            self.lista_extensao.insert('0', 'TXT', 'PDF', 'DOCX')
            self.lista_extensao_ativa_txt = True

    def janela_adicionar_registrar(self):
        self.lista_tipos_extensoes_add = ('VÍDEOS', 'IMAGENS', 'ARQUIVOS_LEITURA')
        self.janela_add_extensao = tk.Tk()
        self.janela_add_extensao.geometry('400x300')
        self.janela_add_extensao.title('Adicionando uma extensão')

        self.label_frame_add_001 = LabelFrame(self.janela_add_extensao, text='Escolha uma categoria')
        self.label_frame_add_001.pack(fill='both')
        self.label_frame_add_002 = LabelFrame(self.janela_add_extensao)
        self.label_frame_add_002.pack(fill='both')

        self.frame_opcao_01 = Frame(self.label_frame_add_001)
        self.frame_opcao_01.pack(anchor='w')
        self.frame_opcao_02 = Frame(self.label_frame_add_001)
        self.frame_opcao_02.pack(anchor='center')

        # RADIOS
        self.var_radio = tk.StringVar()
        self.radio_opcao_01 = Radiobutton(self.frame_opcao_02, text='Vídeos', variable=self.var_radio, value=1)
        self.radio_opcao_01.pack(anchor='w')
        self.radio_opcao_02 = Radiobutton(self.frame_opcao_02, text='Imagens', variable=self.var_radio, value=2)
        self.radio_opcao_02.pack(anchor='w')
        self.radio_opcao_03 = Radiobutton(self.frame_opcao_02, text='Arq de Texto', variable=self.var_radio, value=3)
        self.radio_opcao_03.pack(anchor='w')

        # Entrada
        self.var_texto_ext = tk.StringVar()
        self.enter_txt_ext = Entry(self.label_frame_add_001, width=30, textvariable=self.var_texto_ext, justify='center')
        self.enter_txt_ext.pack(fill='both')

        # botoes
        self.botao_adicionar = Button(self.label_frame_add_002, text='Adicionar', command=self.registro_extensao)
        self.botao_adicionar.pack(anchor='center', ipady=3, ipadx=3)

    def registro_extensao(self):
        print(self.var_radio.get())
        print(self.var_texto_ext.get())

    def janela_inicio_busca(self):
        self.valor_extensao = 'jpg'
        valor_lista_extensao = self.lista_extensao.curselection()
        print(valor_lista_extensao, self.lista_extensao_ativa_videos)
        if self.lista_extensao_ativa_videos:
            if valor_lista_extensao == 0:
                self.valor_extensao = 'MP4'
            elif valor_lista_extensao == 1:
                self.valor_extensao = 'AVI'
        elif self.lista_extensao_ativa_imagem:
            if valor_lista_extensao == 0:
                self.valor_extensao = 'JPG'
            elif valor_lista_extensao == 1:
                self.valor_extensao = 'PNG'

        print(self.valor_extensao)
        # janela busca
        self.janela_busca = tk.Tk()
        self.janela_busca.geometry('600x300')
        self.janela_busca.title('Buscando por arquivos')

        # label frame busca
        self.label_frame_busca = LabelFrame(self.janela_busca, text='Resultado da busca', )
        self.label_frame_busca.pack(fill='both', ipady=5, ipadx=5)

        # Lista da busca
        self.var_busca = tk.Variable()
        self.lista_da_busca = tk.Listbox(self.label_frame_busca, justify='left')
        self.lista_da_busca.pack(fill='both', pady=3, padx=3, ipady=5)

        # valor_extensao = 'jpg'
        pasta_destino_busca = Path(askdirectory())
        for valor_da_busca in pasta_destino_busca.glob('**/*' + self.valor_extensao):
            if valor_da_busca.is_file():
                self.lista_da_busca.insert('0', valor_da_busca)
            elif valor_da_busca.is_dir():
                self.lista_da_busca.insert('0', valor_da_busca)


obj_principal = ListagemPastas()
