import tkinter as tk
from tkinter.ttk import *

from time import sleep
from pathlib import Path, PurePath
from threading import Thread
from datetime import datetime
from tkinter.messagebox import showerror
from tkinter.simpledialog import askstring
from tkinter.filedialog import askdirectory, asksaveasfile

valor_pasta_destino = Path().home()
pasta_arq_registro_extensao = str(Path(valor_pasta_destino, 'AppData', 'LocalLow', 'extensoes'))
valor_datatime = datetime.now()
data_atual = valor_datatime.strftime('%d/%m/%Y')
hora_atual = valor_datatime.strftime('%H:%M')

"""
mostrar as busca conforme os arquivos em pastas

Fotos:
arquivos...
"""


# _+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+

class ListandoArquivos:
    def __init__(self):
        self.categorias_busca = ('Arquivo Imagem', 'Arquivos de Vídeos/Audios', 'Arquivos de Leitura',
                                 'Arquivos execução', 'Arquivos compreesão')

        self.lista_analise_arq_busca = list()
        self.lista_analise_pasta_busca = list()

        # _+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+
        self.ativo_add_ext_especifica = False
        self.ativo_finalizacao_busca = False
        self.ativo_status_extensao = False
        self.ativo_status_destinos = False
        self.ativo_busca_imagem = False
        self.ativo_busca_videos = False
        self.ativo_busca_textos = False
        self.ativo_busca_execul = False
        self.ativo_busca_arqzip = False
        self.ativo_time_busca = False

        # _+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+
        # Janela Principal
        self.janela_principal = tk.Tk()
        self.janela_principal.title('Versão 009')
        self.janela_principal.geometry('1000x640+150+100')
        self.janela_principal.resizable(0, 0)

        self.icone_busca = tk.PhotoImage(file='lupa.png')
        self.janela_principal.iconphoto(True, self.icone_busca)

        # _+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+
        # Estilos
        estilo = Style()
        # estilo.theme_use('default')
        estilo.configure('red.Horizontal.TProgressbar', background='#FFFF00')
        estilo.configure('TButton', background='#4682B4', padding=1)
        estilo.configure('TLabelFrame', background='#4682B4', border=5)
        estilo.configure('TListBox', background='#4682B4')

        # _+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+
        # Label FRAME PRINCIPAL
        self.label_frame_geral = LabelFrame(self.janela_principal, text='Janela Principal')
        self.label_frame_geral.pack(fill=tk.BOTH, pady=5, padx=5)

        # _+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+
        # COMBO DE EXTENSÃO
        self.var_combo_categoria = tk.StringVar()
        self.label_frame_combo_categora = LabelFrame(self.label_frame_geral)
        self.label_frame_combo_categora.pack(side='top', fill=tk.BOTH, pady=2, padx=2)
        self.combo_extensao_categoria = Combobox(self.label_frame_combo_categora, justify='center')
        self.combo_extensao_categoria.pack(anchor='center', fill='both')
        self.combo_extensao_categoria['values'] = self.categorias_busca
        self.combo_extensao_categoria['textvariable'] = self.var_combo_categoria
        self.combo_extensao_categoria.set('Escolha uma categoria de extensão')
        self.var_combo_categoria.trace('w', self.combo_categoria_busca)

        # _+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+
        # INFORMAÇÕES SOBRE EXTENSÃO
        self.label_lista_extensao = LabelFrame(self.label_frame_geral, text='Escolha uma extensão')
        self.label_lista_extensao.pack(side='top', fill='both', pady=2, padx=2)
        # BARRA DE ROLAGEM
        self.barra_rolagem_extensao = Scrollbar(self.label_lista_extensao, orient=tk.VERTICAL)
        self.barra_rolagem_extensao.pack(side='right', fill=tk.Y)
        # LISTA EXTENSAO
        self.lista_de_extensoes = tk.Listbox(self.label_lista_extensao, selectmode=tk.SINGLE, justify='center')
        self.lista_de_extensoes.config(height=3)
        self.lista_de_extensoes.config(selectforeground='#000000')
        self.lista_de_extensoes.config(selectbackground='#A9A9A9')
        self.lista_de_extensoes.config(selectborderwidth=5)
        self.lista_de_extensoes.pack(anchor='center', fill='both')
        # BARRA ROLAGEM
        self.barra_rolagem_extensao.config(command=self.lista_de_extensoes.yview)
        self.lista_de_extensoes.config(yscrollcommand=self.barra_rolagem_extensao.set)

        # LABEL DE INFORMAÇÕES
        self.label_frame_info_ext = LabelFrame(self.label_frame_geral, text='Você escolheu a extensão..!')
        self.label_frame_info_ext.pack(anchor='n')
        self.var_label_info_extensao = tk.StringVar()
        self.var_label_info_extensao.set(' VAZIO ')
        self.label_info_extensao = Label(self.label_frame_info_ext, text=f'[{self.var_label_info_extensao.get()}]')
        self.label_info_extensao.pack(anchor='center')

        # _+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+
        # Busca Geral
        self.var_lista_busca = tk.StringVar()
        self.label_frame_lista_busca = LabelFrame(self.label_frame_geral, text='Resultado da BUSCA')
        self.label_frame_lista_busca.pack(anchor='center', fill='both', pady=2, padx=2)

        # BARRA ROLAGEM CONFIGURAÇÃO
        self.barra_rolagem_lista_busca_Y = Scrollbar(self.label_frame_lista_busca, orient=tk.VERTICAL)
        self.barra_rolagem_lista_busca_Y.pack(side='right', fill=tk.Y)
        self.barra_rolagem_lista_busca_X = Scrollbar(self.label_frame_lista_busca, orient=tk.HORIZONTAL)
        self.barra_rolagem_lista_busca_X.pack(side='bottom', fill=tk.X)

        # LISTA DO RESULTADO DA BUSCA
        self.lista_result_busca = tk.Listbox(self.label_frame_lista_busca, listvariable=self.var_lista_busca.get())
        self.lista_result_busca.config(height=5)
        self.lista_result_busca.config(selectmode=tk.SINGLE)
        self.lista_result_busca.pack(anchor='center', fill=tk.BOTH, padx=2, pady=2)

        # BARRA ROLAGEM APLICAÇÃO
        self.barra_rolagem_lista_busca_Y.config(command=self.lista_result_busca.yview)
        self.lista_result_busca.config(yscrollcommand=self.barra_rolagem_lista_busca_Y.set)
        self.barra_rolagem_lista_busca_X.config(command=self.lista_result_busca.xview)
        self.lista_result_busca.config(xscrollcommand=self.barra_rolagem_lista_busca_X.set)

        # LABEM FRAME INFO BUSCA
        self.label_frame_geral_info = LabelFrame(self.label_frame_geral, text='Informações da busca...!')
        self.label_frame_geral_info.config(relief=tk.RIDGE)
        self.label_frame_geral_info.pack(anchor='center', fill='both', pady=2, padx=2)

        # LABEL STATUS GERAL
        self.var_label_status_geral = tk.StringVar()
        self.label_status = Label(self.label_frame_geral_info, text=self.var_label_status_geral.get())
        self.label_status.config(justify='center')
        self.label_status.pack(anchor='s', pady=2, padx=2)

        # LABEL CONTAGEM ARQUIVOS
        self.var_status_contagem_arquivos = tk.StringVar()
        self.var_status_contagem_arquivos.set('Aguardando informações')
        self.status_contagem_arquivos = Label(self.label_frame_geral_info)
        self.status_contagem_arquivos.config(text=self.var_status_contagem_arquivos.get())
        self.status_contagem_arquivos.config(justify='center')
        # self.status_contagem_arquivos.pack(anchor='s', pady=2, padx=2)
        self.status_contagem_arquivos.place(y=0, x=5)

        # LABEL CONTAGEM PASTAS
        self.var_status_contagem_pastas = tk.StringVar()
        self.var_status_contagem_pastas.set('Aguardando informações')
        self.status_contagem_pastas = Label(self.label_frame_geral_info)
        self.status_contagem_pastas.config(text=self.var_status_contagem_pastas.get())
        self.status_contagem_pastas.config(justify='center')
        # self.status_contagem_pastas.pack(anchor='s', pady=2, padx=2)
        self.status_contagem_pastas.place(y=20, x=5)

        # LABEL CONTAGEM GERAL ARQUIVOS E PASTAS
        self.var_msg_tot_busca = tk.StringVar()
        self.var_msg_tot_busca.set('Aguardando informações')
        self.msg_tot_busca = Label(self.label_frame_geral_info, text=self.var_msg_tot_busca.get())
        self.msg_tot_busca.config(justify='center')
        # self.msg_tot_busca.pack(anchor='s', pady=2, padx=2)
        self.msg_tot_busca.place(y=0, x=650)

        # LABEL TIME DA BUSCA
        self.var_label_time_busca = tk.StringVar()
        self.var_label_time_busca.set('00:00:00')
        self.label_time_busca = Label(self.label_frame_geral_info, text=self.var_label_time_busca.get())
        self.label_time_busca.pack(anchor='s', pady=2, padx=2)

        # _+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+
        # BOTÕES
        self.label_frame_botoes_opcoes = LabelFrame(self.label_frame_geral, text='Escolha um opção')
        self.label_frame_botoes_opcoes.pack(side='bottom', fill='both', pady=2, padx=2)

        # BOTÃO Iniciar Busca
        self.botao_iniciar_busca = Button(self.label_frame_botoes_opcoes, text='Iniciar Busca')
        self.botao_iniciar_busca.config(width=30)
        self.botao_iniciar_busca.config(command=self.thread_botao_iniciar)
        self.botao_iniciar_busca.pack(anchor='center', pady=2, padx=2)

        # BOTÃO Selecionar extensão
        self.botao_escolha_extensao = Button(self.label_frame_botoes_opcoes, text='Selecione/Digite uma extensão')
        self.botao_escolha_extensao.config(width=30)
        self.botao_escolha_extensao.config(command=self.thread_botao_extensao)
        self.botao_escolha_extensao.place(y=1)

        # BOTÃO Adicionar extensão
        self.botao_adicionar_extensao = Button(self.label_frame_botoes_opcoes, text='Adicionar Extensões')
        self.botao_adicionar_extensao.config(width=30)
        self.botao_adicionar_extensao.config(state=tk.DISABLED)
        self.botao_adicionar_extensao.config(command=self.janela_add_ext_arq_txt)
        self.botao_adicionar_extensao.place(y=50)
        self.botao_adicionar_extensao.pack(anchor='w')

        # BOTÃO DESTINO DA BUSCA
        self.botao_destino_busca = Button(self.label_frame_botoes_opcoes, text='Selecionar Pasta para Busca')
        self.botao_destino_busca.config(width=30)
        self.botao_destino_busca.config(command=self.thread_selecionar_destino_busca)
        self.botao_destino_busca.place(y=1, x=788)

        # BOTÃO SAVE BUSCA
        self.botao_save_busca = Button(self.label_frame_botoes_opcoes, text='Salvar Busca')
        self.botao_save_busca.config(width=30)
        self.botao_save_busca.config(state=tk.DISABLED)
        self.botao_save_busca.config(command=lambda: self.salvando_resultado())
        self.botao_save_busca.place(y=30, x=788)

        # _+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+
        # Barra de progresso da busca
        self.label_frame_progresso = LabelFrame(self.label_frame_geral, text='Progresso da busca...!')
        self.label_frame_progresso.pack(side='bottom', fill='both', pady=2, padx=2)
        self.barra_progresso_busca = Progressbar(self.label_frame_progresso)
        self.barra_progresso_busca.config(orient=tk.HORIZONTAL)
        self.barra_progresso_busca.config(mode='determinate')
        self.barra_progresso_busca.config(style='red.Horizontal.TProgressbar')
        self.barra_progresso_busca.pack(anchor='center', fill='both', pady=2, padx=2)

        # LOOP DA JANELA PRINCIPAL
        self.janela_principal.mainloop()

    # _+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+
    def janela_add_ext_arq_txt(self):
        print('Iniciando janela para add extensões')
        tk.messagebox.showinfo("AVISO IMPORTANTE", 'Para deixar mais organizado a lista '
                                                   'de extensões, é aconselhavel que seja escolhido a '
                                                   'categoria que corresponda com a extensão que ira adicionar')
        janela_add_extensao = tk.Tk()
        janela_add_extensao.geometry('400x400+150+100')
        janela_add_extensao.resizable(0, 0)
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

    def linha_aparencia(self):
        print('-=-' * 48)

    # _+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+
    # INICIANDO AS THREADS
    def thread_botao_iniciar(self):
        print('Iniciando THREAD [INICIAR BUSCA]')
        if self.ativo_status_extensao:
            Thread(target=self.iniciar_busca).start()
        else:
            showerror('AVISO!', 'Voce não escolheu nenhuma extensão')

    def thread_botao_extensao(self):
        print('Iniciando THREAD [BUSCA ESPECIFICA POR EXTENSAO]')
        Thread(target=self.digitar_extensao()).start()

    def thread_adicionar_extensao(self):
        print('Iniciando THREAD [ADICIONAR EXTENSAO]')
        Thread(self.adicionado_extensao_arq_txt()).start()

    def thread_selecionar_destino_busca(self):
        Thread(target=self.pasta_destino_busca()).start()

    def thread_time_busca(self):
        print('Iniciando THREAD de time')
        Thread(target=self.time_busca()).start()

    # _+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+
    # INICIO DAS FUNÇÕES
    def time_busca(self):
        print('Iniciando time da busca')
        msg_info_time = str
        contagem_segundos = 0
        contagem_minutos = 0
        contagem_horas = 0
        if self.ativo_time_busca:
            while self.ativo_time_busca:
                if contagem_segundos == 0:
                    msg_info_time = str(f'00:00:00')
                    self.label_time_busca['text'] = msg_info_time
                else:
                    if contagem_segundos < 10 and contagem_minutos == 0 and contagem_horas == 0:
                        msg_info_time = str(f'00:00:0{contagem_segundos}')
                    elif contagem_segundos > 9 and contagem_minutos == 0 and contagem_horas == 0:
                        msg_info_time = str(f'00:00:{contagem_segundos}')

                    elif contagem_segundos < 10 and contagem_minutos < 10 > 1 and contagem_horas == 0:
                        msg_info_time = str(f'00:0{contagem_minutos}:0{contagem_segundos}')
                    elif contagem_segundos > 9 and contagem_minutos < 10 and contagem_horas == 0:
                        msg_info_time = str(f'00:0{contagem_minutos}:{contagem_segundos}')
                    elif contagem_segundos < 10 and contagem_minutos > 9 and contagem_horas == 0:
                        msg_info_time = str(f'00:{contagem_minutos}:0{contagem_segundos}')
                    elif contagem_segundos > 9 and contagem_minutos > 9 and contagem_horas == 0:
                        msg_info_time = str(f'00:{contagem_minutos}:{contagem_segundos}')

                    elif contagem_segundos < 10 and contagem_minutos < 10 and contagem_horas < 10:
                        msg_info_time = str(f'0{contagem_horas}:0{contagem_minutos}:0{contagem_segundos}')
                    elif contagem_segundos > 9 and contagem_minutos < 10 and contagem_horas < 10:
                        msg_info_time = str(f'0{contagem_horas}:0{contagem_minutos}:{contagem_segundos}')
                    elif contagem_segundos < 10 and contagem_minutos > 9 and contagem_horas < 10:
                        msg_info_time = str(f'0{contagem_horas}:{contagem_minutos}:0{contagem_segundos}')
                    elif contagem_segundos > 9 and contagem_minutos > 9 and contagem_horas < 10:
                        msg_info_time = str(f'0{contagem_horas}:{contagem_minutos}:{contagem_segundos}')
                    elif contagem_segundos < 10 and contagem_minutos < 10 and contagem_horas > 9:
                        msg_info_time = str(f'{contagem_horas}:0{contagem_minutos}:0{contagem_segundos}')
                    elif contagem_segundos > 9 and contagem_minutos < 10 and contagem_horas > 9:
                        msg_info_time = str(f'{contagem_horas}:0{contagem_minutos}:{contagem_segundos}')
                    elif contagem_segundos > 9 and contagem_minutos > 9 and contagem_horas > 9:
                        msg_info_time = str(f'{contagem_horas}:{contagem_minutos}:{contagem_segundos}')

                    if contagem_segundos == 59:
                        if contagem_minutos == 59:
                            contagem_segundos = 0
                            contagem_minutos = 0
                            contagem_horas += 1
                        else:
                            contagem_segundos = 0
                            contagem_minutos += 1

                self.label_time_busca['text'] = msg_info_time
                contagem_segundos += 1
                sleep(1)

    def combo_categoria_busca(self, *args):
        print('Processando o Combo')
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

        elif valor_categoria_busca == 'Arquivos de Vídeos/Audios':
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
        self.leitura_arq_extensao_add_lista_principal()  # CHAMA A FUNÇÃO

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
            else:
                tk.messagebox.showwarning('AVISO IMPORTANTE', 'Você precisa selecionar uma categoria')
            self.lista_de_extensoes.delete('0', 'end')
            self.leitura_arq_extensao_add_lista_principal()

    def leitura_arq_extensao_add_lista_principal(self):
        self.lista_ext_imagem = list()
        self.lista_ext_videos = list()
        self.lista_ext_textos = list()
        self.lista_ext_execul = list()
        self.lista_ext_arqzip = list()

        if self.ativo_busca_imagem:
            try:
                leitura_arq_imagem = open(self.arq_extensao_add, 'r')
                for valor_leitura in leitura_arq_imagem.readlines():
                    self.lista_de_extensoes.insert('end', valor_leitura)
                    self.lista_ext_imagem.append(valor_leitura)
            except FileNotFoundError:
                tk.messagebox.showerror('ERROR', 'Arquivo de IMAGEM não existe \n'
                                                 'Você pode adicionar ou digitar uma extensão \n'
                                                 'Basta clicar no botão "Selecioinar/Digitar uma extensão"')

        elif self.ativo_busca_videos:
            try:
                leitura_arq_videos = open(self.arq_extensao_add, 'r')
                for valor_leitura in leitura_arq_videos.readlines():
                    self.lista_de_extensoes.insert('end', valor_leitura)
                    self.lista_ext_videos.append(valor_leitura)
            except FileNotFoundError:
                tk.messagebox.showerror('ERROR', 'Arquivo de VIDEOS não existe \n'
                                                 'Você pode adicionar ou digitar uma extensão \n'
                                                 'Basta clicar no botão "Selecioinar/Digitar uma extensão"')

        elif self.ativo_busca_textos:
            try:
                leitura_arq_textos = open(self.arq_extensao_add, 'r')
                for valor_leitura in leitura_arq_textos.readlines():
                    self.lista_de_extensoes.insert('end', valor_leitura)
                    self.lista_ext_textos.append(valor_leitura)
            except FileNotFoundError:
                tk.messagebox.showerror('ERROR', 'Arquivo de Textos não existe \n'
                                                 'Você pode adicionar ou digitar uma extensão \n'
                                                 'Basta clicar no botão "Selecioinar/Digitar uma extensão"')

        elif self.ativo_busca_execul:
            try:
                leitura_arq_execul = open(self.arq_extensao_add, 'r')
                for valor_leitura in leitura_arq_execul.readlines():
                    self.lista_de_extensoes.insert('end', valor_leitura)
                    self.lista_ext_execul.append(valor_leitura)
            except FileNotFoundError:
                tk.messagebox.showerror('ERROR', 'Arquivo de EXE não existe \n'
                                                 'Você pode adicionar ou digitar uma extensão \n'
                                                 'Basta clicar no botão "Selecioinar/Digitar uma extensão"')

        elif self.ativo_busca_arqzip:
            try:
                leitura_arq_arqzip = open(self.arq_extensao_add, 'r')
                for valor_leitura in leitura_arq_arqzip.readlines():
                    self.lista_de_extensoes.insert('end', valor_leitura)
                    self.lista_ext_arqzip.append(valor_leitura)
            except FileNotFoundError:
                tk.messagebox.showerror('ERROR', 'Arquivo de ZIP não existe \n'
                                                 'Você pode adicionar ou digitar uma extensão \n'
                                                 'Basta clicar no botão "Selecioinar/Digitar uma extensão"')

    def digitar_extensao(self):
        valor_lista_extensao = self.lista_de_extensoes.curselection()
        if len(valor_lista_extensao) == 0:
            extensao_digitada = askstring('AVISO', 'Selecionar/Digitar uma Extensão para busca')

            if len(extensao_digitada) == 0:
                extensao_digitada = "Busca por vários arquivos"
                self.extensao_selecao_busca = ''
            else:
                self.extensao_selecao_busca = extensao_digitada
            self.label_info_extensao.config(text=extensao_digitada.upper())
            self.ativo_status_extensao = True

        else:
            for valor_extensao in valor_lista_extensao:
                pass
            if self.ativo_busca_imagem:
                self.extensao_selecao_busca = self.lista_ext_imagem[valor_extensao].strip()
                self.label_info_extensao.config(text=self.extensao_selecao_busca)
                self.ativo_status_extensao = True

            elif self.ativo_busca_videos:
                self.extensao_selecao_busca = self.lista_ext_videos[valor_extensao].strip()
                self.label_info_extensao.config(text=self.extensao_selecao_busca)
                self.ativo_status_extensao = True

            elif self.ativo_busca_textos:
                self.extensao_selecao_busca = self.lista_ext_textos[valor_extensao].strip()
                self.label_info_extensao.config(text=self.extensao_selecao_busca)
                self.ativo_status_extensao = True

            elif self.ativo_busca_execul:
                self.extensao_selecao_busca = self.lista_ext_execul[valor_extensao].strip()
                self.label_info_extensao.config(text=self.extensao_selecao_busca)
                self.ativo_status_extensao = True

            elif self.ativo_busca_arqzip:
                self.extensao_selecao_busca = self.lista_ext_arqzip[valor_extensao].strip()
                self.label_info_extensao.config(text=self.extensao_selecao_busca)
                self.ativo_status_extensao = True
        self.lista_de_extensoes.delete('0', 'end')
        valor_lista_extensao = 0

    def pasta_destino_busca(self):
        self.pasta_local_de_busca = tk.filedialog.askdirectory()
        self.ativo_status_destinos = True

    def iniciar_busca_V1_desativado(self):  # Desativado

        if self.ativo_status_destinos:
            pasta_destino = Path(self.pasta_local_de_busca)
        else:
            pasta_destino = Path(valor_pasta_destino)

        print(f'Valor "ativo_finalizacao_busca" {self.ativo_finalizacao_busca}')

        if self.ativo_finalizacao_busca:
            valor_resposta = tk.messagebox.askquestion('AVISO', 'Deseja salvar a busca anterior?')
            self.msg_tot_busca.config(text="Idenficamos nova busca, aguarde!!")
            self.status_contagem_arquivos.config(text='Idenficamos nova busca, aguarde!!')
            self.status_contagem_pastas.config(text='Identicamos nova busca, aguarde!!')
            if valor_resposta == 'no':
                tk.messagebox.showwarning('AVISO', "Você optou em não salvar a busca")
                self.lista_result_busca.delete('0', 'end')
                self.contagem_extensao.clear()
                print('Lista de resultado foi limpa!')
            else:
                self.salvando_resultado()
                self.lista_result_busca.delete('0', 'end')
                self.ativo_finalizacao_busca = False

        valor_da_busca = self.extensao_selecao_busca
        print('Iniciando busca...')
        print(f'Valor da extensão [{valor_da_busca}]')
        print(f'Caminho do busca [{pasta_destino}]')
        cont_arquivos = 1
        cont_pastas = 1
        self.label_status['text'] = 'Iniciando busca'
        sleep(1)

        # Desativando botoes
        self.botao_save_busca['state'] = 'disabled'
        self.botao_iniciar_busca['state'] = 'disabled'
        self.botao_destino_busca['state'] = 'disabled'
        self.botao_escolha_extensao['state'] = 'disabled'

        self.ativo_time_busca = True
        Thread(target=self.time_busca).start()

        self.barra_progresso_busca.start(100)
        for busca in pasta_destino.glob('**/*' + valor_da_busca):
            self.label_status.config(text='Processando, aguarde...!')
            if busca.is_file():
                self.lista_result_busca.insert('end', f'[ {cont_arquivos} ] - *[ {busca} ]')
                self.lista_analise_arq_busca.append(f'{cont_arquivos} - {busca}')
                self.status_contagem_arquivos.config(text=f'Encontrado [ {cont_arquivos} ] arquivos... \n')
                cont_arquivos += 1
            elif busca.is_dir():
                self.lista_result_busca.insert('end', f'[ {cont_pastas} ] - \\[ {busca} ]')
                self.lista_analise_pasta_busca.append(f'{cont_pastas} - {busca}')
                self.status_contagem_pastas.config(text=f'Encontrado [ {cont_pastas} ] pastas...')
                cont_pastas += 1
        self.barra_progresso_busca.stop()
        self.label_status['text'] = 'Busca Finalizada!'
        self.botao_save_busca.config(state=tk.NORMAL)
        self.ativo_finalizacao_busca = True
        self.ativo_time_busca = False
        print('Busca finalizada!!')

        # ATIVANDO OS BOTÕES DEPOIS DA BUSCA
        self.botao_save_busca['state'] = 'normal'
        self.botao_iniciar_busca['state'] = 'normal'
        self.botao_destino_busca['state'] = 'normal'
        self.botao_escolha_extensao['state'] = 'normal'

        self.msg_tot_busca.config(text=f'Foram encontrados {cont_arquivos} arquivos com a extensão'
                                       f' [ {valor_da_busca} ] e... \n'
                                       f' [ {cont_pastas} ] Pasta/s ')
        self.analise_dados_busca()

    def iniciar_busca_V2_desativado(self):
        contagem_extensao = dict()
        contagem_pastas = dict()
        pastas_encontradas = dict()
        extensao_encontradas = dict()
        lista_extensoes = list()
        lista_pastas = list()
        contador_arquivos = 1
        contador_pastas = 1

        if self.ativo_status_destinos:
            pasta_destino = Path(self.pasta_local_de_busca)
        else:
            pasta_destino = Path(valor_pasta_destino)

        # Ativando o time
        self.ativo_time_busca = True
        Thread(target=self.time_busca).start()

        # Ativando BARRA DE PROGRESSO
        self.barra_progresso_busca.start()

        # Informação da busca
        self.label_status.config(text='Iniciando processo de busca, aguarde!')
        sleep(1)

        for valor_busca in pasta_destino.glob('**/*' + self.extensao_selecao_busca):
            dividindo_arquivos_extensao = str(valor_busca).split('.')
            dividindo_arquivos_pastas = str(valor_busca).split('\\')
            lista_extensoes.append(dividindo_arquivos_extensao[-1])
            lista_pastas.append(dividindo_arquivos_pastas[-2])

            if valor_busca.is_dir():
                if valor_busca in pastas_encontradas:
                    pastas_encontradas[valor_busca] += 1
                else:
                    pastas_encontradas[valor_busca] = 1
            elif valor_busca.is_file():
                if valor_busca in extensao_encontradas:
                    extensao_encontradas[valor_busca] += 1
                else:
                    extensao_encontradas[valor_busca] = 1

        self.lista_result_busca.insert('end', f'{data_atual} - {hora_atual}')
        self.lista_result_busca.insert('end', '')
        self.lista_result_busca.insert('end', '\nPastas', '-=-' * 48)

        # Busca Pastas
        self.linha_aparencia()
        self.label_status.config(text='Carregando as informações da busca na lista!')
        for chave, valor_encontrado in pastas_encontradas.items():
            self.lista_result_busca.insert('end', f'{contador_pastas}-\\{chave}')
            print(f'Valor da busca {contador_pastas} - \\{chave} : {valor_encontrado}')
            contador_pastas += 1
            self.status_contagem_pastas.config(text=f'Pastas encontradas [{contador_pastas}]')
        self.lista_result_busca.insert('end', '')
        self.lista_result_busca.insert('end', '\nArquivos', '-=-' * 48)

        # Busca Arquivos
        for chave, valor_encontrado in extensao_encontradas.items():
            self.lista_result_busca.insert('end', f'{contador_arquivos}-**{chave}')
            print(f'Valor da busca {contador_arquivos} - **{chave} : {valor_encontrado}')
            contador_arquivos += 1
            self.status_contagem_arquivos.config(text=f'Arquivos encontrados [{contador_arquivos}]')

        self.linha_aparencia()
        print('Busca Finalizada!')
        self.label_status.config(text='Busca Finalizada!')
        self.lista_result_busca.insert('end', '')
        self.lista_result_busca.insert('end', 'Busca finalizada!')
        self.lista_result_busca.insert('end', '-=-' * 50)

        self.msg_tot_busca.config(text=f'Fora encontrados {contador_arquivos} Arquivos e \n'
                                       f'{contador_pastas} pastas')

        # Desativando o TIME
        self.ativo_time_busca = False

        # Desativando BARRA DE PROGRESSO
        self.barra_progresso_busca.stop()

        print('Quantidade de arquivos')
        self.linha_aparencia()
        for valor in lista_extensoes:
            if valor in contagem_extensao:
                contagem_extensao[valor] += 1
            else:
                contagem_extensao[valor] = 1
        for ext, contagem in contagem_extensao.items():
            print(f'{ext}:{contagem}')

        self.linha_aparencia()
        for valor in lista_pastas:
            if valor in contagem_pastas:
                contagem_pastas[valor] += 1
            else:
                contagem_pastas[valor] = 1
        for pasta, contagem in contagem_pastas.items():
            print(f'{pasta}:{contagem}')

    def iniciar_busca(self):
        from glob import glob
        from os import walk
        from re import search
        # Verifica se foi selecionado uma pasta, caso não tenha sido, a busca vai ficar na pasta home do usuário
        if self.ativo_status_destinos:
            valor_path_busca = Path(self.pasta_local_de_busca)
        else:
            valor_path_busca = Path(valor_pasta_destino)
        for raiz, subs, itens in walk(str(valor_path_busca)):
            print()
            print(raiz)
            self.linha_aparencia()
            for valor_itens in itens:
                if search(self.extensao_selecao_busca, valor_itens):
                    if len(valor_itens) == 0:
                        print(f'Não foram encontrados nenhum item com o valor {valor_itens}')
                    else:
                        print(valor_itens)

    def analise_dados_busca(self):
        self.criando_relatorio_pdf()
        # Declarações de variaveis
        self.contagem_extensao = {}
        self.contagem_pastas = {}

        for valor_lista_busca in self.lista_analise_arq_busca:
            divisao_valor_extensao = str(valor_lista_busca).split('.')
            divisao_valor_pastas = str(valor_lista_busca).split('\\')
            valor_extensao = str(divisao_valor_extensao[-1]).lower().strip()
            valor_pastas = str(divisao_valor_pastas[-2].lower()).strip()

            if valor_pastas in self.contagem_pastas:
                self.contagem_pastas[valor_pastas] += 1
            else:
                self.contagem_pastas[valor_pastas] = 1

            if valor_extensao in self.contagem_extensao:
                self.contagem_extensao[valor_extensao] += 1
            else:
                self.contagem_extensao[valor_extensao] = 1

        print('-=-' * 40)
        print('Tipos de extensão - Quantidade Arquivos')
        for extensao, quantidade in self.contagem_extensao.items():
            print(f'       {extensao} ------ : ------ [{quantidade}] ')

        print('-=-' * 40)
        print('Pastas --- Quantidade de arquivos')
        for pastas, quantidade in self.contagem_pastas.items():
            print(f'{pastas} - {quantidade}')

        del self.lista_analise_arq_busca[:]

    def criando_relatorio_pdf(self):
        pass

    def salvando_resultado(self):
        tipo_de_arquivo = [('Texto(.log)', '*.log')]
        arquivo_save = asksaveasfile(filetypes=tipo_de_arquivo, defaultextension=tipo_de_arquivo)
        try:
            for valor_busca in self.lista_analise_arq_busca:
                arquivo_save.write(f'{valor_busca} - {data_atual} - {hora_atual} \n')
            arquivo_save.close()
            tk.messagebox.showinfo('AVISO', 'Sua busca foi salva com sucesso')
        except:
            tk.messagebox.showwarning('AVISO', 'Busca não pode ser salva no sistema!')


obj_start = ListandoArquivos()

''' # Realiza a busca
 for valor_da_busca in valor_path_busca.glob('**/*' + self.extensao_selecao_busca):
     if valor_da_busca.is_dir():
         pasta_busca = Path(str(valor_da_busca))
         self.linha_aparencia()
         print(f'Busca realizada na pasta [{pasta_busca}]')
         for valor in pasta_busca.glob('**/*' + self.extensao_selecao_busca):
             if valor.is_dir():
                 print(valor)
     elif PurePath('**/*' + self.extensao_selecao_busca).parts:
         print(valor_da_busca)
         
         
                 for valor_da_busca in valor_path_busca.iterdir():
            if valor_da_busca.is_dir():
                valor_pasta_busca = Path(valor_da_busca)
                print()
                print(f'Valor diretorio {valor_da_busca}')
                self.linha_aparencia()
                for valor_busca_file in valor_pasta_busca.glob('**/*' + self.extensao_selecao_busca):
                    if valor_busca_file.is_file():
                        valor_arquivo = str(valor_busca_file).split('\\')[-1]
                        print(valor_arquivo)
            else:
                print(str(valor_da_busca).split('\\')[-1])
         
                 
         
         '''
