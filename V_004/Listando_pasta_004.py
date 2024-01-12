from tkinter.filedialog import askdirectory
from pathlib import Path
from time import sleep
import tkinter as tk


class ListandoPastas:
    def __init__(self):
        # Variaveis
        self.scroll_listagem_001 = None
        self.lista_arquivos = None
        self.extensoes_imagem = ['JPG', 'JPEG', 'PNG', 'BMP', 'GIF']
        self.extensoes_documentos = ('PDF', 'TXT', 'DOCX')
        self.extensoes_arquivos = ("ISO", 'DLL')
        self.extensoes_midias = ('MP4', 'MP3', 'MPEG', 'AVI')

        # Janela principal
        self.janela_principal = tk.Tk()
        self.janela_principal.geometry('300x230')
        self.janela_principal.title('Listagem de arquivos')

        # Frames Label
        self.frame_label_principal_001 = tk.LabelFrame(self.janela_principal, text='Selecione um arquivo', pady=3, padx=3)
        self.frame_label_principal_002 = tk.LabelFrame(self.janela_principal, padx=3, pady=3)
        self.frame_label_principal_003 = tk.LabelFrame(self.janela_principal, padx=3, pady=3, text='Escolha uma mídia!')
        self.frame_label_principal_001.pack(fill='both')
        self.frame_label_principal_002.pack(fill='both')
        self.frame_label_principal_003.pack(fill='both')

        # Frames
        self.frame_txt_001 = tk.Frame(self.frame_label_principal_001, pady=3, padx=3)
        self.frame_txt_002 = tk.Frame(self.frame_label_principal_001, pady=3, padx=3)
        self.frame_txt_001.pack(side='top')
        self.frame_txt_002.pack(side='bottom')

        # Lista
        self.variavel_extensao = tk.Variable(value=self.extensoes_imagem)
        self.lista_extensoes_001 = tk.Listbox(self.frame_label_principal_001, listvariable=self.variavel_extensao,
                                              justify='center')
        self.lista_extensoes_001.pack(fill='both', expand='yes')

        # Botoes
        self.botao_entrar = tk.Button(self.frame_label_principal_002, text='Selecionar',
                                      command=self.iniciando_busca_arquivos)
        self.botao_entrar.pack(side='left')
        self.botao_sair_principal = tk.Button(self.frame_label_principal_002, text='Sair',
                                              command=self.janela_principal.destroy)
        self.botao_sair_principal.pack(side='right')

        self.janela_principal.mainloop()

    def iniciando_busca_arquivos(self):
        tipo_arquivo = self.lista_extensoes_001.curselection()
        valor_pasta_destino = askdirectory()
        pasta_destino_busca = Path(valor_pasta_destino)

        # janela listagem
        self.janela_listagem = tk.Tk()
        self.janela_listagem.geometry('800x230')
        self.janela_listagem.title('Listando arquivos...')

        # Frames
        self.frame_label_listagem_001 = tk.LabelFrame(self.janela_listagem, text='Arquivos listados', padx=3, pady=3)
        self.frame_label_listagem_002 = tk.LabelFrame(self.janela_listagem, pady=3, padx=3)
        self.frame_label_listagem_001.pack(fill='both')
        self.frame_label_listagem_002.pack(fill='both')

        # SCROLL
        self.scroll_listagem = tk.Scrollbar(self.frame_label_listagem_001)
        self.scroll_listagem.pack(side='right', fill='both')

        # Mesangem
        self.lista_arquivos = tk.Listbox(self.frame_label_listagem_001, selectmode=tk.EXTENDED, justify='left')
        for extensao_arq in tipo_arquivo:
            self.valor_extensao = str(self.extensoes_imagem[extensao_arq])
        self.lista_arquivos.config(yscrollcommand=self.scroll_listagem.set)  # SCROLL
        self.scroll_listagem.config(command=self.janela_listagem)  # SCROLL

        # Listagem de pasta
        for listagem in pasta_destino_busca.glob('**/*' + self.valor_extensao):
            if listagem.is_file():
                self.lista_arquivos.insert('end', listagem)
        self.lista_arquivos.pack(anchor='center', fill='both')
        # Botao
        self.botao_sair_listagem = tk.Button(self.frame_label_listagem_002, text='Sair da janela', padx=3, pady=3,
                                             command=self.janela_listagem.destroy)
        self.botao_sair_listagem.pack(anchor='se')


obj_listando_pasta = ListandoPastas()
