import tkinter as tk
from tkinter.ttk import *

from time import sleep
from pathlib import Path
from threading import Thread
from tkinter.messagebox import showerror
from tkinter.simpledialog import askstring


pasta_destino = Path().home()
pasta_arq_registro_extensao = Path(pasta_destino, 'AppData', 'LocalLow', 'extensoes')


class ListandoArquivos:
    def __init__(self):
        self.ativo_status_extensao = False
        self.ativo_info_escolha_ext = False

        # Janela Principal
        self.janela_principal = tk.Tk()
        self.janela_principal.title('Versão 009')
        self.janela_principal.geometry('1000x700')
        # self.janel_principal.geometry('alturaXlargura')

        # Label FRAME PRINCIPAL
        self.label_frame_geral = LabelFrame(self.janela_principal, text='Janela Principal')
        self.label_frame_geral.pack(fill=tk.BOTH, ipadx=5, ipady=5)

        # COMBO DE EXTENSÃO
        self.var_combo_categoria = tk.StringVar()
        self.label_frame_combo_categora = LabelFrame(self.label_frame_geral)
        self.label_frame_combo_categora.pack(side='top', fill=tk.BOTH)
        self.combo_extensao_categoria = Combobox(self.label_frame_combo_categora, values='teste', justify='center')
        self.combo_extensao_categoria.pack(anchor='center', fill='both')
        self.combo_extensao_categoria.set('Escolha uma categoria de extensão')
        self.var_combo_categoria.trace('w', self.combo_categoria_extensao)

        # INFORMAÇÕES SOBRE EXTENSÃO
        self.label_lista_extensao = LabelFrame(self.label_frame_geral, text='Escolha uma extensão')
        self.label_lista_extensao.pack(side='top', fill='both')

        self.barra_rolagem_extensao = Scrollbar(self.label_lista_extensao, orient=tk.VERTICAL)
        self.barra_rolagem_extensao.pack(side='right', fill=tk.Y)

        self.lista_de_extensoes = tk.Listbox(self.label_lista_extensao, selectmode=tk.SINGLE, justify='center')
        self.lista_de_extensoes.pack(anchor='center', fill='both')

        self.barra_rolagem_extensao.config(command=self.lista_de_extensoes.yview)
        self.lista_de_extensoes.config(yscrollcommand=self.barra_rolagem_extensao.set)

        # LABEL DE INFORMAÇÕES
        self.label_frame_info_ext = LabelFrame(self.label_frame_geral, text='Você escolheu a extensão..!')
        self.label_frame_info_ext.pack(anchor='n')
        self.var_label_info_extensao = tk.StringVar()
        self.label_info_extensao = Label(self.label_frame_info_ext, text=f'[{self.var_label_info_extensao.get()}]')
        self.label_info_extensao.pack(anchor='center')

        # Busca Geral
        self.var_lista_busca = tk.StringVar()
        self.label_frame_lista_busca = LabelFrame(self.label_frame_geral, text='Resultado da BUSCA')
        self.label_frame_lista_busca.pack(anchor='center', fill='both')

        self.barra_rolagem_lista_busca_Y = Scrollbar(self.label_frame_lista_busca, orient=tk.VERTICAL)
        self.barra_rolagem_lista_busca_Y.pack(side='right', fill=tk.Y)
        self.barra_rolagem_lista_busca_X = Scrollbar(self.label_frame_lista_busca, orient=tk.HORIZONTAL)
        self.barra_rolagem_lista_busca_X.pack(side='bottom', fill=tk.X)

        self.lista_result_busca = tk.Listbox(self.label_frame_lista_busca, listvariable=self.var_lista_busca.get())
        self.lista_result_busca.pack(anchor='center', fill=tk.BOTH)

        self.barra_rolagem_lista_busca_Y.config(command=self.lista_result_busca.yview)
        self.lista_result_busca.config(yscrollcommand=self.barra_rolagem_lista_busca_Y.set)

        self.barra_rolagem_lista_busca_X.config(command=self.lista_result_busca.yview)
        self.lista_result_busca.config(xscrollcommand=self.barra_rolagem_lista_busca_X.set)

        self.var_label_status_geral = tk.StringVar()
        self.label_status = Label(self.label_frame_geral, text=self.var_label_status_geral.get())
        self.label_status.pack(anchor='s')

        self.var_label_info_qtd_arq = tk.StringVar()
        self.label_qtd_arq_busca = Label(self.label_frame_geral, text=self.var_label_info_qtd_arq.get())
        self.label_qtd_arq_busca.pack(anchor='s')

        # Botoes
        self.label_frame_botoes_opcoes = LabelFrame(self.label_frame_geral, text='Escolha um opção')
        self.label_frame_botoes_opcoes.pack(side='bottom', fill='both')

        self.botao_iniciar_busca = Button(self.label_frame_botoes_opcoes, text='Iniciar Busca', width=20,
                                          command=self.thread_botao_iniciar)
        self.botao_iniciar_busca.pack(anchor='center')
        self.botao_escolha_extensao = Button(self.label_frame_botoes_opcoes, text='Digite uma extensão', width=20,
                                             command=self.thread_botao_extensao)
        self.botao_escolha_extensao.pack(anchor='sw', ipady=5, ipadx=5)
        self.botao_adicionar_extensao = Button(self.label_frame_botoes_opcoes, text='Adicionar Extensões', width=20,
                                               command=self.add_extensao)
        self.botao_adicionar_extensao.pack(anchor='sw', ipady=5, ipadx=5)

        # Barra de progresso da busca
        self.label_frame_progresso = LabelFrame(self.label_frame_geral, text='Progresso da busca...!')
        self.label_frame_progresso.pack(side='bottom', fill='both')
        self.barra_progresso_busca = Progressbar(self.label_frame_progresso, orient=tk.HORIZONTAL, mode='determinate')
        self.barra_progresso_busca.pack(anchor='center', fill='both', pady=3, padx=3)

        self.janela_principal.mainloop()

    # INICIANDO AS THREADS
    def thread_botao_iniciar(self):
        if self.ativo_status_extensao:
            Thread(target=self.iniciar_busca).start()
        else:
            showerror('AVISO!', 'Voce não escolheu nenhuma extensão')

    def thread_botao_extensao(self):
        Thread(target=self.digitar_extensao()).start()

    # INICIO DAS FUNÇÕES
    def combo_categoria_extensao(self):
        valor_categoria = self.combo_extensao_categoria.get()

    def add_extensao(self):
        self.categorias = ('Arquivo Imagem', 'Arquivos de Vídeo', 'Arquivos de Leitura', 'Arquivos execução',
                           'Arquivos compreesão')
        self.janela_add_extensao = tk.Tk()
        self.janela_add_extensao.geometry('400x400')
        self.label_frame_add_ext = LabelFrame(self.janela_add_extensao, text='Janela Adicionar Extensão')
        self.label_frame_add_ext.pack(side='top', fill='both', padx=5, pady=5)
        self.label_add_ext_combo = LabelFrame(self.label_frame_add_ext, text='Escolha uma Categora para adicionar a extensão')
        self.label_add_ext_combo.pack(side='top', fill='both')

        # COMBO
        self.var_combo_add_ext = tk.StringVar()
        self.combo_add_ext_cat = Combobox(self.label_add_ext_combo, textvariable=self.var_combo_add_ext, justify='center')
        self.combo_add_ext_cat.pack(anchor='center', fill='both')

        # CAIXA DE ENTRADA
        self.label_add_ext = tk.Label(self.label_frame_add_ext, text="Digite uma extensão", border=2, bd=2)
        self.label_add_ext.pack(anchor='center',  fill='both', pady=3, padx=3)
        self.var_caixa_entrada = tk.StringVar()
        self.caixa_entrada_ext = tk.Entry(self.label_frame_add_ext, textvariable=self.var_caixa_entrada.get(), bd=5)
        self.caixa_entrada_ext.pack(anchor='center', fill='both')

        # BOTOES
        self.botao_add_ext = tk.Button(self.label_frame_add_ext, text='Adicionar', border=2, bd=2)
        self.botao_add_ext.pack(side='bottom')

    def digitar_extensao(self):
        self.extensao_selecao = askstring('AVISO', 'Digite um Extensão')
        self.label_info_extensao.config(text=self.extensao_selecao)
        self.ativo_status_extensao = True

    def iniciar_busca(self):
        cont_arquivos = 1
        cont_pastas = 1
        self.label_status['text'] = 'Iniciando busca'
        sleep(1)
        self.barra_progresso_busca.start(100)
        valor_da_busca = self.extensao_selecao
        for busca in pasta_destino.glob('**/*' + valor_da_busca):
            self.label_status.config(text='Processando, aguarde...!')
            self.lista_result_busca.insert('end', f'{cont_arquivos} - {busca}')
            cont_arquivos += 1
        self.barra_progresso_busca.stop()
        self.label_status['text'] = 'Busca Finalizada!'
        self.label_qtd_arq_busca.config(text=f'Foram encontrados {cont_arquivos} arquivos com a extensão'
                                             f' [{valor_da_busca.upper()}]')


obj_start = ListandoArquivos()
