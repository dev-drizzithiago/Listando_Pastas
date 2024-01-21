import tkinter
from time import sleep
from tkinter import *
from tkinter.ttk import *
from threading import Thread
from datetime import datetime
from tkinter.messagebox import *
from tkinter.simpledialog import *

valor_hora = datetime.now()
data_certa = valor_hora.strftime('%d/%m/%Y')
hora_certa = valor_hora.strftime('%H:%M')


class ListandoPastas:
    def __init__(self):
        # Variaveis geral
        self.categorias = ('Limpar lista', 'Arquivos de Vídeo', 'Arquivo Imagem', 'Arquivos de Leitura',
                           'Arquivos execução', 'Arquivos compreesão')
        self.extensoes_imagem = ('JPG', 'PNG', 'GIF', 'BMP', 'Bitmap', 'TIFF', 'RAW', 'EXIF', 'PPM', 'PGM', 'PBM', 'PNM'
                                 , 'SVG', 'WebP',)
        self.extensoes_videos = ('MP4', 'AVI', 'MKV', 'MOV', 'WMV', 'FLV', 'AVCHD', 'F4V', 'SWF', 'WEBM', 'HTML5',
                                 'WEBM')
        self.extensoes_arq_txt = (
            'TXT', 'PDF', 'DOCX', 'DOC', 'HTML', 'HTM', 'ODT', 'XLS', 'XLSX', 'ODS', 'PPT', 'PPTX')
        self.extensoes_de_app = ('EXE', 'DLL', 'IN', 'BAT')
        self.extensoes_compreensao = ('ZIP', '')

        self.ativo_imagem = False
        self.ativo_Videos = False
        self.ativo_textos = False
        self.ativo_execul = False
        self.ativo_arqzip = False

        # janela princpal
        janela_principal = Tk()
        janela_principal.geometry('450x450')
        janela_principal.config(padx=5, pady=5)
        janela_principal.title('V_008')

        # Relogio
        label_frame_relogio = LabelFrame(janela_principal, text='Hora Certa')
        label_frame_relogio.pack(anchor='center', fill=BOTH)
        label_hora = Label(label_frame_relogio, text=f'{data_certa} - {hora_certa}', justify='center')
        label_hora.pack(anchor='center')

        # Combo
        self.variavel_combo = StringVar()
        label_frame_combo = LabelFrame(janela_principal, text='Categorias de arquivos')
        label_frame_combo.pack(fill=BOTH)
        self.combo_principal = Combobox(label_frame_combo, textvariable=self.variavel_combo, justify='center')
        self.combo_principal['values'] = self.categorias
        self.combo_principal.set('Escolha uma categoria')
        self.combo_principal.current()
        self.combo_principal.pack(fill=BOTH, pady=5, padx=5)
        self.variavel_combo.trace('w', self.combo_selecao_categoria)

        # lista principal
        self.variavel_lista_principal = IntVar()
        label_frame_lista = LabelFrame(janela_principal, text='Escolha uma extensão')
        label_frame_lista.pack(side='top', fill=BOTH)
        self.lista_principal = Listbox(label_frame_lista, selectmode=SINGLE, justify='center')
        self.lista_principal.pack(fill=BOTH, pady=3, padx=3)

        # Botoes
        label_frame_botao_princial = LabelFrame(janela_principal, text="Escolha uma Opcão")
        label_frame_botao_princial.pack(fill=BOTH)

        label_frame_iniciar_busca = LabelFrame(label_frame_botao_princial, text='Buscando por arquivos')
        label_frame_iniciar_busca.pack(anchor='n')
        botao_iniciar_busca = Button(label_frame_iniciar_busca, text='Iniciar busca', width=20, height=1,
                                     command=self.thread_iniciar_busca)
        botao_iniciar_busca.pack(anchor='center', pady=3, padx=3)

        label_frame_botao_especif = LabelFrame(label_frame_botao_princial, text='Digite uma extensão para busca',
                                               width=20, height=1)
        label_frame_botao_especif.pack(side='left')
        botao_busca_especifica = Button(label_frame_botao_especif, text='Buscando por arquivos', width=20, height=1)
        botao_busca_especifica.pack(anchor='center', pady=3, padx=3)

        label_frame_sair_programa = LabelFrame(label_frame_botao_princial, text='Saindo do programa', width=20,
                                               height=1)
        label_frame_sair_programa.pack(side='right')
        botao_sair_programa = Button(label_frame_sair_programa, text='Fechar Programa', width=20, height=1,
                                     command=janela_principal.destroy)
        botao_sair_programa.pack(anchor='center', pady=3, padx=3)

        janela_principal.mainloop()

    def janela_busca(self):
        # Funções da busca
        # janela busca

        self.janela_busca = Tk()
        self.janela_busca.config(padx=5, pady=5)
        self.janela_busca.geometry('700x400')
        self.janela_busca.title(f'Buscar por arquivos')

        # Label Frame horario
        label_frame_hora = LabelFrame(self.janela_busca, text='Hora Certa')
        label_frame_hora.pack(fill=BOTH)
        label_hora_data = Label(label_frame_hora, text=f'{data_certa} - {hora_certa}', justify='center')
        label_hora_data.pack(anchor='center')

        # Listagem da busca
        label_frame_lista_busca = LabelFrame(self.janela_busca, text='Resultado da Busca', border=2)
        label_frame_lista_busca.pack(fill=BOTH)
        label_lista_busca = Label(label_frame_lista_busca, text='Arquivos encontrados:')
        label_lista_busca.pack(side='top', padx=5, pady=5)
        self.variavel_lista_busca = IntVar()
        self.lista_busca = Listbox(label_frame_lista_busca, listvariable=self.variavel_lista_busca, selectmode=SINGLE,
                                   justify='center')
        self.lista_busca.pack(fill=BOTH, anchor='center', padx=5, pady=5)

        # Label Frame botão iniciar
        label_botao_iniciar = LabelFrame(self.janela_busca, border=2)
        label_botao_iniciar.pack(anchor='center', fill='both')
        botao_iniciar_busca = Button(label_botao_iniciar, text='Iniciar', border=5, width=20, height=1,
                                     command=self.thead_iniciar_processo_busca)
        botao_iniciar_busca.pack(anchor='center', ipady=5, ipadx=5)

        # MENSAGEM EM GERAL
        label_frame_msg_busca = LabelFrame(self.janela_busca, text='Extensão para ser processada!')
        label_frame_msg_busca.pack(anchor='center')
        self.var_msg_estatus = StringVar()
        self.var_msg_estatus.set(self.valor_status_msg)
        label_msg_busca = Message(label_frame_msg_busca, text=self.var_msg_estatus.get(), relief='raised', justify='center')
        label_msg_busca.pack(anchor='center', fill=BOTH, ipady=4, ipadx=4)

    # INICIO DAS THREADS
    def thread_iniciar_busca(self, *args):
        Thread(target=self.opcao_de_busca()).start()
        Thread(target=self.janela_busca()).start()

    def thead_iniciar_processo_busca(self, *args):
        Thread(target=self.opcao_de_busca()).start()
        Thread(target=self.iniciando_processo_busca()).start()

    # ESCOLHA EXTENSÃO
    def combo_selecao_categoria(self, *args):
        self.limpar_lista()
        valor_categoria = self.variavel_combo.get()
        if valor_categoria == 'Arquivos de Vídeo':
            for valor_lista in self.extensoes_videos:
                self.lista_principal.insert('end', valor_lista)
            self.ativo_Videos = True

        elif valor_categoria == 'Arquivo Imagem':
            for valor_lista in self.extensoes_imagem:
                self.lista_principal.insert('end', valor_lista)
            self.ativo_imagem = True

        elif valor_categoria == 'Arquivos de Leitura':
            for valor_lista in self.extensoes_arq_txt:
                self.lista_principal.insert('end', valor_lista)
            self.ativo_textos = True

        elif valor_categoria == 'Arquivos execução':
            for valor_lista in self.extensoes_de_app:
                self.lista_principal.insert('end', valor_lista)
            self.ativo_execul = True

        elif valor_categoria == 'Arquivos compreesão':
            for valor_lista in self.extensoes_compreensao:
                self.lista_principal.insert('end', valor_lista)
            self.ativo_arqzip = True

    def opcao_de_busca(self):
        valor_extensao_busca_lista = self.lista_principal.curselection()
        try:
            if self.ativo_Videos:
                for opcao_busca in valor_extensao_busca_lista:
                    self.valor_extesao_busca = self.extensoes_videos[opcao_busca]
                    self.valor_status_msg = self.extensoes_videos[opcao_busca]
            elif self.ativo_imagem:
                for opcao_busca in valor_extensao_busca_lista:
                    self.valor_extesao_busca = self.extensoes_imagem[opcao_busca]
                    self.valor_status_msg = self.extensoes_imagem[opcao_busca]
            elif self.ativo_textos:
                for opcao_busca in valor_extensao_busca_lista:
                    self.valor_extesao_busca = self.extensoes_arq_txt[opcao_busca]
                    self.valor_status_msg = self.extensoes_arq_txt[opcao_busca]
            elif self.ativo_execul:
                for opcao_busca in valor_extensao_busca_lista:
                    self.valor_extesao_busca = self.extensoes_de_app[opcao_busca]
                    self.valor_status_msg = self.extensoes_de_app[opcao_busca]
            elif self.ativo_arqzip:
                for opcao_busca in valor_extensao_busca_lista:
                    self.valor_extesao_busca = self.extensoes_compreensao[opcao_busca]
                    self.valor_status_msg = self.extensoes_compreensao[opcao_busca]
        except:
            pass

    def limpar_lista(self):
        self.lista_principal.delete('0', 'end')

    def iniciando_processo_busca(self):
        print(self.valor_extesao_busca)


obj_principal = ListandoPastas()
