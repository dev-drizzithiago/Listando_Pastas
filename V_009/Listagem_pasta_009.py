import tkinter as tk
from tkinter.ttk import *

from time import sleep
from pathlib import Path
from threading import Thread
from tkinter.messagebox import showerror
from tkinter.simpledialog import askstring

pasta_destino = Path().home()
pasta_arq_registro_extensao = str(Path(pasta_destino, 'AppData', 'LocalLow', 'extensoes'))


class ListandoArquivos:
    def __init__(self):
        self.categorias_busca = ('Arquivo Imagem', 'Arquivos de Vídeo', 'Arquivos de Leitura', 'Arquivos execução',
                                 'Arquivos compreesão')

        self.ativo_status_extensao = False
        # dwself.ativo_info_escolha_ext = False

        self.ativo_busca_imagem = False
        self.ativo_busca_videos = False
        self.ativo_busca_textos = False
        self.ativo_busca_execul = False
        self.ativo_busca_arqzip = False

        # Janela Principal
        self.janela_principal = tk.Tk()
        self.janela_principal.title('Versão 009')
        self.janela_principal.geometry('1000x700')
        self.icone_busca = tk.PhotoImage(file='lupa.png')
        self.janela_principal.iconphoto(True, self.icone_busca)

        # Label FRAME PRINCIPAL
        self.label_frame_geral = LabelFrame(self.janela_principal, text='Janela Principal')
        self.label_frame_geral.pack(fill=tk.BOTH, ipadx=5, ipady=5)

        # COMBO DE EXTENSÃO
        self.var_combo_categoria = tk.StringVar()
        self.label_frame_combo_categora = LabelFrame(self.label_frame_geral)
        self.label_frame_combo_categora.pack(side='top', fill=tk.BOTH)
        self.combo_extensao_categoria = Combobox(self.label_frame_combo_categora, justify='center')
        self.combo_extensao_categoria.pack(anchor='center', fill='both')
        self.combo_extensao_categoria['values'] = self.categorias_busca
        self.combo_extensao_categoria['textvariable'] = self.var_combo_categoria
        self.combo_extensao_categoria.set('Escolha uma categoria de extensão')
        self.var_combo_categoria.trace('w', self.combo_categoria_busca)

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
        self.lista_result_busca.config(selectmode=tk.SINGLE)
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
        self.botao_escolha_extensao = Button(self.label_frame_botoes_opcoes, text='Selecione/Digite uma extensão')
        self.botao_escolha_extensao.config(width=30)
        self.botao_escolha_extensao.config(command=self.thread_botao_extensao)
        self.botao_escolha_extensao.pack(anchor='sw', ipady=5, ipadx=5)
        self.botao_adicionar_extensao = Button(self.label_frame_botoes_opcoes, text='Adicionar Extensões', width=20)
        self.botao_adicionar_extensao['state'] = tk.DISABLED
        self.botao_adicionar_extensao['command'] = self.janela_add_ext_arq_txt
        self.botao_adicionar_extensao.pack(anchor='sw', ipady=5, ipadx=5)

        # Barra de progresso da busca
        self.label_frame_progresso = LabelFrame(self.label_frame_geral, text='Progresso da busca...!')
        self.label_frame_progresso.pack(side='bottom', fill='both')
        self.barra_progresso_busca = Progressbar(self.label_frame_progresso, orient=tk.HORIZONTAL, mode='determinate')
        self.barra_progresso_busca.pack(anchor='center', fill='both', pady=3, padx=3)

        self.janela_principal.mainloop()

    def janela_add_ext_arq_txt(self):
        tk.messagebox.showinfo("AVISO IMPORTANTE", 'Para deixar mais organizado a lista '
                                                   'de extensões, é aconselhavel que seja escolhido a '
                                                   'categoria que corresponda com a extensão que ira adicionar')
        janela_add_extensao = tk.Tk()
        janela_add_extensao.geometry('400x400')
        janela_add_extensao.title('Janele para adicionar extensão')
        # janela_add_extensao.iconphoto(True, self.icone_busca)

        label_frame_add_ext_geral = tk.LabelFrame(janela_add_extensao, text='Janele para adicionar extensão')
        label_frame_add_ext_geral.pack(anchor='center', fill='both', pady=5, padx=5)

        self.var_caixa_entrada_ext = tk.StringVar
        label_frame_caixa_entrada = tk.LabelFrame(label_frame_add_ext_geral, text='Digite uma extensão no campo abaixo')
        label_frame_caixa_entrada.pack(side='top', fill='both', pady=5, padx=5)
        self.caixa_entrada_extensao = tk.Entry(label_frame_caixa_entrada, justify='center')
        self.caixa_entrada_extensao['textvariable'] = self.var_caixa_entrada_ext
        self.caixa_entrada_extensao.pack(anchor='center', fill='both', pady=5, padx=5)

        # Botões
        label_frame_botao_add_ext = tk.LabelFrame(label_frame_add_ext_geral, text='Escolha uma opção')
        label_frame_botao_add_ext.pack(anchor='center', fill='both', pady=5, padx=5)
        botao_adicionar_ext = tk.Button(label_frame_botao_add_ext, text='Adicionar', width=20, height=1)
        botao_adicionar_ext['command'] = self.thread_adicionar_extensao
        botao_adicionar_ext.pack(anchor='center', pady=5, padx=5)
        botao_corrigir_caixa_entrada = tk.Button(label_frame_botao_add_ext, text='Corrigir Entrada', width=20)
        botao_corrigir_caixa_entrada.pack(side='left', pady=5, padx=5)
        botao_voltar_janela_principal = tk.Button(label_frame_botao_add_ext, text='Janela Principal', width=20)
        botao_voltar_janela_principal['command'] = janela_add_extensao.destroy
        botao_voltar_janela_principal.pack(side='right', pady=5, padx=5)

        # informações
        label_frame_info_add = tk.LabelFrame(label_frame_add_ext_geral, text='Foi adicionado a extensão')
        label_frame_info_add.pack(side='bottom', pady=5, padx=5)
        self.var_label_info_add_extensao = tk.StringVar()
        self.label_info_add_extensao = tk.Label(label_frame_info_add, text=self.var_label_info_add_extensao.get())
        self.label_info_add_extensao.pack(anchor='center', pady=5, padx=5)

    # INICIANDO AS THREADS
    def thread_botao_iniciar(self):
        print('Iniciando THREAD [INICIAR BUSCA]')
        if self.ativo_status_extensao:
            Thread(target=self.iniciar_busca).start()
        else:
            showerror('AVISO!', 'Voce não escolheu nenhuma extensão')

    def thread_selecionar_extensao(self):
        Thread(target=self.selecionar_extensao_busca()).start()

    def thread_botao_extensao(self):
        print('Iniciando THREAD [BUSCA ESPECIFICA POR EXTENSAO]')
        Thread(target=self.digitar_extensao()).start()

    def thread_adicionar_extensao(self):
        print('Iniciando THREAD [ADICIONAR EXTENSAO]')
        Thread(self.adicionado_extensao_arq_txt()).start()

    # INICIO DAS FUNÇÕES
    def combo_categoria_busca(self, *args):
        self.lista_de_extensoes.delete('0', 'end')

        arq_imagem = '\\extensao_imagem.log'
        arq_videos = '\\extensao_videos.log'
        arq_textos = '\\extensao_textos.log'
        arq_execul = '\\extensao_execul.log'
        arq_arqzip = '\\extensao_arqzip.log'

        valor_categoria_busca = self.var_combo_categoria.get()
        if valor_categoria_busca == 'Arquivo Imagem':
            self.ativo_busca_imagem = True
            self.ativo_busca_videos = False
            self.ativo_busca_textos = False
            self.ativo_busca_execul = False
            self.ativo_busca_arqzip = False
            self.botao_adicionar_extensao['state'] = tk.NORMAL
            self.arq_extensao_add = str(pasta_arq_registro_extensao + arq_imagem)

        elif valor_categoria_busca == 'Arquivos de Vídeo':
            self.ativo_busca_imagem = False
            self.ativo_busca_videos = True
            self.ativo_busca_textos = False
            self.ativo_busca_execul = False
            self.ativo_busca_arqzip = False
            self.botao_adicionar_extensao['state'] = tk.NORMAL
            self.arq_extensao_add = str(pasta_arq_registro_extensao + arq_videos)

        elif valor_categoria_busca == 'Arquivos de Leitura':
            self.ativo_busca_imagem = False
            self.ativo_busca_videos = False
            self.ativo_busca_textos = True
            self.ativo_busca_execul = False
            self.ativo_busca_arqzip = False
            self.botao_adicionar_extensao['state'] = tk.NORMAL
            self.arq_extensao_add = str(pasta_arq_registro_extensao + arq_textos)

        elif valor_categoria_busca == 'Arquivos execução':
            self.ativo_busca_imagem = False
            self.ativo_busca_videos = False
            self.ativo_busca_textos = False
            self.ativo_busca_execul = True
            self.ativo_busca_arqzip = False
            self.botao_adicionar_extensao['state'] = tk.NORMAL
            self.arq_extensao_add = str(pasta_arq_registro_extensao + arq_execul)

        elif valor_categoria_busca == 'Arquivos compreesão':
            self.ativo_busca_imagem = False
            self.ativo_busca_videos = False
            self.ativo_busca_textos = False
            self.ativo_busca_execul = False
            self.ativo_busca_arqzip = True
            self.botao_adicionar_extensao['state'] = tk.NORMAL
            self.arq_extensao_add = str(pasta_arq_registro_extensao + arq_arqzip)
        self.leitura_arq_extensao_add_lista_principal()

    def selecionar_extensao_busca(self):
        valor_extensao = self.lista_de_extensoes.curselection()
        for valor_extensao in valor_extensao:
            pass
        if self.ativo_busca_imagem:
            self.extensao_selecao_busca = self.lista_ext_imagem[valor_extensao]
            self.ativo_status_extensao = True

    def adicionado_extensao_arq_txt(self):
        valor_entrada_extensao = self.caixa_entrada_extensao.get().upper()
        if len(valor_entrada_extensao) == 0:
            tk.messagebox.showerror('ERROR', 'Você precisa digitar uma extensão')
        else:
            print(valor_entrada_extensao)

            if self.ativo_busca_imagem:
                try:
                    arq_txt = open(self.arq_extensao_add, 'a')
                    arq_txt.write(f'{valor_entrada_extensao}\n')
                    arq_txt.close()
                    self.label_info_add_extensao.config(text=valor_entrada_extensao)
                    tk.messagebox.showinfo('AVISO', f'Extensão {valor_entrada_extensao} '
                                                    f'foi adicionada com sucesso!')
                    self.caixa_entrada_extensao.delete('0', 'end')
                except:
                    tk.messagebox.showerror('ERROR', 'Não foi possível adicionar a extensão')

            elif self.ativo_busca_videos:
                try:
                    arq_txt = open(self.arq_extensao_add, 'a')
                    arq_txt.write(f'{valor_entrada_extensao}\n')
                    arq_txt.close()
                    self.label_info_add_extensao.config(text=valor_entrada_extensao)
                    tk.messagebox.showinfo('AVISO', f'Extensão {valor_entrada_extensao} '
                                                    f'foi adicionada com sucesso!')
                    self.caixa_entrada_extensao.delete('0', 'end')
                except:
                    tk.messagebox.showerror('ERROR', 'Não foi possível adicionar a extensão')

            elif self.ativo_busca_textos:
                try:
                    arq_txt = open(self.arq_extensao_add, 'a')
                    arq_txt.write(f'{valor_entrada_extensao}\n')
                    arq_txt.close()
                    self.label_info_add_extensao.config(text=valor_entrada_extensao)
                    tk.messagebox.showinfo('AVISO', f'Extensão {valor_entrada_extensao} '
                                                    f'foi adicionada com sucesso!')
                    self.caixa_entrada_extensao.delete('0', 'end')
                except:
                    tk.messagebox.showerror('ERROR', 'Não foi possível adicionar a extensão')

            elif self.ativo_busca_execul:
                try:
                    arq_txt = open(self.arq_extensao_add, 'a')
                    arq_txt.write(f'{valor_entrada_extensao}\n')
                    arq_txt.close()
                    self.label_info_add_extensao.config(text=valor_entrada_extensao)
                    tk.messagebox.showinfo('AVISO', f'Extensão {valor_entrada_extensao} '
                                                    f'foi adicionada com sucesso!')
                    self.caixa_entrada_extensao.delete('0', 'end')
                except:
                    tk.messagebox.showerror('ERROR', 'Não foi possível adicionar a extensão')

            elif self.ativo_busca_arqzip:
                try:
                    arq_txt = open(self.arq_extensao_add, 'a')
                    arq_txt.write(f'{valor_entrada_extensao}\n')
                    arq_txt.close()
                    self.label_info_add_extensao.config(text=valor_entrada_extensao)
                    tk.messagebox.showinfo('AVISO', f'Extensão {valor_entrada_extensao} '
                                                    f'foi adicionada com sucesso!')
                    self.caixa_entrada_extensao.delete('0', 'end')
                except:
                    tk.messagebox.showerror('ERROR', 'Não foi possível adicionar a extensão')

    def leitura_arq_extensao_add_lista_principal(self):
        self.lista_ext_imagem = list()
        self.lista_ext_videos = list()
        self.lista_ext_textos = list()
        self.lista_ext_execul = list()
        self.lista_ext_arqzip = list()

        if self.ativo_busca_imagem:
            leitura_arq_imagem = open(self.arq_extensao_add, 'r')
            for valor_leitura in leitura_arq_imagem.readlines():
                self.lista_de_extensoes.insert('end', valor_leitura)
                self.lista_ext_imagem.append(valor_leitura)

        elif self.ativo_busca_videos:
            leitura_arq_videos = open(self.arq_extensao_add, 'r')
            for valor_leitura in leitura_arq_videos.readlines():
                self.lista_de_extensoes.insert('end', valor_leitura)
                self.lista_ext_videos.append(valor_leitura)

        elif self.ativo_busca_textos:
            leitura_arq_textos = open(self.arq_extensao_add, 'r')
            for valor_leitura in leitura_arq_textos.readlines():
                self.lista_de_extensoes.insert('end', valor_leitura)
                self.lista_ext_textos.append(valor_leitura)

        elif self.ativo_busca_execul:
            leitura_arq_execul = open(self.arq_extensao_add, 'r')
            for valor_leitura in leitura_arq_execul.readlines():
                self.lista_de_extensoes.insert('end', valor_leitura)
                self.lista_ext_execul.append(valor_leitura)

        elif self.ativo_busca_arqzip:
            leitura_arq_arqzip = open(self.arq_extensao_add, 'r')
            for valor_leitura in leitura_arq_arqzip.readlines():
                self.lista_de_extensoes.insert('end', valor_leitura)
                self.lista_ext_arqzip.append(valor_leitura)

    def digitar_extensao(self):
        valor_lista_extensao = self.lista_de_extensoes.curselection()
        if len(valor_lista_extensao) == 0:
            self.extensao_selecao_busca = askstring('AVISO', 'Selecionar/Digitar uma Extensão para busca')
            self.label_info_extensao.config(text=self.extensao_selecao_busca)
            self.ativo_status_extensao = True
        else:
            for valor_extensao in valor_lista_extensao:
                pass
            if self.ativo_busca_imagem:
                self.extensao_selecao_busca = self.lista_ext_imagem[valor_extensao]
                self.label_info_extensao.config(text=self.extensao_selecao_busca)
                self.ativo_status_extensao = True

    def iniciar_busca(self):
        valor_da_busca = self.extensao_selecao_busca
        print(f'Valor da extensão {valor_da_busca}')
        print(f'Caminha do busca {pasta_destino}')
        cont_arquivos = 1
        cont_pastas = 1
        self.label_status['text'] = 'Iniciando busca'
        sleep(1)
        self.barra_progresso_busca.start(100)
        for busca in pasta_destino.glob('**/*' + valor_da_busca):
            self.label_status.config(text='Processando, aguarde...!')
            self.lista_result_busca.insert('end', f'{cont_arquivos} - {busca}')
            cont_arquivos += 1
        self.barra_progresso_busca.stop()
        self.label_status['text'] = 'Busca Finalizada!'
        self.label_qtd_arq_busca.config(text=f'Foram encontrados {cont_arquivos} arquivos com a extensão'
                                             f' [{valor_da_busca}]')


obj_start = ListandoArquivos()
