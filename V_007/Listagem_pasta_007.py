import tkinter as tk
from tkinter.ttk import *
from pathlib import Path
from tkinter.filedialog import askdirectory, asksaveasfile
from tkinter.messagebox import showinfo, showerror, showwarning
from tkinter.simpledialog import *


class ListagemPastas:
    def __init__(self):

        # Varias Global
        self.pasta_home = Path.home()
        self.pastas_arquivos_extensao = Path(self.pasta_home, 'AppData', 'LocalLow', 'extensoes')
        self.lista_ativa_imagem = False
        self.lista_ativa_videos = False
        self.lista_ativa_textos = False

        self.lista_salves_busca = list()

        self.lista_tipos_extensoes = ('VÍDEOS', 'IMAGENS', 'ARQUIVOS_LEITURA')
        self.extensoes_imagem = ('JPG', 'PNG', 'GIF', 'BMP', 'Bitmap', 'TIFF', 'RAW', 'EXIF', 'PPM', 'PGM', 'PBM', 'PNM',
                                 'SVG', 'WebP', )
        self.extensoes_videos = ('MP4', 'AVI', 'MKV', 'MOV', 'WMV', 'FLV', 'AVCHD', 'F4V', 'SWF', 'WEBM', 'HTML5')
        self.extensoes_arq_txt = ('TXT', 'PDF', 'DOCX', 'DOC', 'HTML', 'HTM', 'ODT', 'XLS', 'XLSX', 'ODS', 'PPT', 'PPTX')

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
        self.combo_tipo_arquivo_principal = Combobox(self.label_frame_001, textvariable=self.var_combo, justify='center')
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
        self.botao_iniciar_busca.pack(fill='both', padx=3, pady=3)
        self.botao_add_ext = tk.Button(self.label_frame_003, text='Adicionar Extensões', command=self.janela_adicionar_registrar)
        self.botao_add_ext.pack(fill='both', padx=3, pady=3)
        self.botao_sair_programa = tk.Button(self.label_frame_003, text='Sair do programa', command=self.janela_principal.destroy)
        self.botao_sair_programa.pack(fill='both', ipady=3, ipadx=3)

        # Looping janela
        self.janela_principal.mainloop()

    def tipos_extensao(self, *args):
        """
        Essa função está sendo destinada para escolhar uma categoria de arquivos, que o programa ira buscar.
        :param args: Quando se escolhe uma categoria, o programa vai listar as extensões dessa categoria em um ListBox
        e mostrar ao usuário, quando escolha uma categoria, as várias ativas irão retornar o valor "Verdadeiro"
        :return: self.lista_ativa_imagem
        :return: self.lista_ativa_videos
        :return: self.lista_ativa_textos
        """
        valor_categoria_busca = self.var_combo.get()
        self.lista_extensao.delete('0', 'end')
        if valor_categoria_busca == 'VÍDEOS':
            for valor_lista_video in self.extensoes_videos:
                self.lista_extensao.insert('end', valor_lista_video)
            self.lista_ativa_videos = True
        elif valor_categoria_busca == 'IMAGENS':
            for valor_lista_imgem in self.extensoes_imagem:
                self.lista_extensao.insert('end', valor_lista_imgem)
            self.lista_ativa_imagem = True
        elif valor_categoria_busca == 'ARQUIVOS_LEITURA':
            for valor_lista_texto in self.extensoes_arq_txt:
                self.lista_extensao.insert('end', valor_lista_texto)
            self.lista_ativa_textos = True

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
        global valor_opc_extensao, valor_extensao_busca

        # janela busca
        self.janela_busca = tk.Tk()
        self.janela_busca.geometry('600x300')
        self.janela_busca.title('Buscando por arquivos')

        # label frame busca
        self.label_frame_busca = LabelFrame(self.janela_busca, text='Resultado da busca', )
        self.label_frame_busca.pack(fill='both', ipady=5, ipadx=5)
        self.frame_busca_01 = Label(self.janela_busca)
        self.frame_busca_01.pack(anchor='s')

        # botao
        self.botao_voltar_menu = Button(self.frame_busca_01, text='Salvar', command=self.save_busca)
        self.botao_voltar_menu.pack(anchor='s')
        self.botao_busca_sair = Button(self.frame_busca_01, text='Fechar Janela', command=self.janela_busca.destroy)
        self.botao_busca_sair.pack(anchor='w')

        # Lista da busca

        self.var_busca = tk.Variable()
        self.lista_da_busca = tk.Listbox(self.label_frame_busca, justify='left')
        self.lista_da_busca.pack(fill='both', pady=3, padx=3, ipady=5)

        # proceddo da função
        valor_lista_extensao = self.lista_extensao.curselection()
        for valor_opc_extensao in valor_lista_extensao:
            print(valor_opc_extensao)

        if self.lista_ativa_imagem:
            valor_extensao_busca = self.extensoes_imagem[valor_opc_extensao]
            print(valor_extensao_busca)
            # self.lista_ativa_imagem = False
        elif self.lista_ativa_videos:
            valor_extensao_busca = self.extensoes_videos[valor_opc_extensao]
            print(valor_extensao_busca)
            # self.lista_ativa_videos = False
        elif self.lista_ativa_textos:
            valor_extensao_busca = self.extensoes_arq_txt[valor_opc_extensao]
            print(valor_extensao_busca)
            # self.lista_ativa_textos = False

        pasta_destino_busca = Path(askdirectory())
        for valor_da_busca in pasta_destino_busca.glob('**/*' + valor_extensao_busca):
            if valor_da_busca.is_file():
                self.lista_da_busca.insert('0', valor_da_busca)
                self.lista_salves_busca.append(valor_da_busca)
            elif valor_da_busca.is_dir():
                self.lista_da_busca.insert('0', valor_da_busca)

        for valor_salve in self.lista_salves_busca:
            print(valor_salve)

    def save_busca(self):
        asksaveasfile(self.lista_salves_busca)


obj_principal = ListagemPastas()
