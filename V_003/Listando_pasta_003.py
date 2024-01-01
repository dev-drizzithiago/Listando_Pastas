from pathlib import Path
from time import sleep
import tkinter as tk
from tkinter.filedialog import askdirectory
from tkinter.messagebox import showinfo


class JanelaTK:
    def __init__(self):
        # GERAL
        self.pasta_destino = Path(Path.home())
        self.extensoes = ['TUDO', 'JPG', 'MP4', 'TXT']
        self.linhas_aparencia = '-=-' * 30
        # Janela principal
        self.janela_principal = tk.Tk()
        self.janela_principal.geometry('350x250')

        # FRAMES
        self.frame_txt_01 = tk.Frame(self.janela_principal)
        self.frame_txt_01.pack(anchor='n')
        self.frame_txt_02 = tk.Frame(self.janela_principal)
        self.frame_txt_02.pack(anchor='center')

        self.frame_botao_001 = tk.Frame(self.janela_principal)
        self.frame_botao_001.pack(anchor='s')
        self.frame_botao_sair = tk.Frame(self.janela_principal)
        self.frame_botao_sair.pack(anchor='se')

        # VARIAVEIS
        self.var_extersao = tk.Variable(value=self.extensoes)

        # LABELSdw
        caixa_entrada = tk.Label(self.frame_txt_01, text="Escolha uma extensão de arquivo")
        caixa_entrada.pack(anchor='n')

        self.lista_arqs = tk.Listbox(self.frame_txt_01, listvariable=self.var_extersao, selectmode=tk.EXTENDED)
        self.lista_arqs.pack(anchor='s')

        self.botao_entrar = tk.Button(self.frame_botao_001, text='Pasta HOME', command=self.extensao_selecionado)
        self.botao_entrar.pack(side='left')
        self.botao_destino = tk.Button(self.frame_botao_001, text='Escolher Caminho', command=self.diretorio)
        self.botao_destino.pack(side='right')
        self.botao_sair = tk.Button(self.frame_botao_sair, text='Sair', padx=5, pady=5,
                                    command=self.janela_principal.destroy)
        self.botao_sair.pack(side='bottom')

        self.janela_principal.mainloop()

    def extensao_selecionado(self):
        selecao = self.lista_arqs.curselection()  # Tupla
        for extensao in selecao:
            if extensao == 0:
                self.opcao_arquivo = ''
            else:
                self.opcao_arquivo = self.extensoes[extensao]
            tk.messagebox.showinfo('AVISO!!', self.opcao_arquivo)
            self.buscando_arquivos()

    def diretorio(self):
        destino_selecao = askdirectory()
        self.pasta_destino = Path(destino_selecao)
        self.extensao_selecionado()

    def buscando_arquivos(self):
        print('inciando busca...')
        sleep(1)
        print(self.linhas_aparencia)
        print('Buscando arquivos ', self.opcao_arquivo)
        print(self.linhas_aparencia)
        for listagem in self.pasta_destino.glob('**/*' + self.opcao_arquivo):
            if listagem.is_file():
                print(listagem)
        print('\nBusca finalizada!')


obj_janela_busca = JanelaTK()
