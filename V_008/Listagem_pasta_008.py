import tkinter as tk
from time import sleep
from pathlib import Path
from threading import Thread
from datetime import datetime
from tkinter.ttk import Combobox
from tkinter.filedialog import askdirectory
from tkinter.messagebox import showinfo, showerror
# from tkinter.simpledialog import *



valor_hora = datetime.now()
data_certa = valor_hora.strftime('%d/%m/%Y')
hora_certa = valor_hora.strftime('%H:%M')


class CorpoPrincipal:
    def __init__(self):

        # Variaveis geral
        self.lista_busca_save = list()
        self.pasta_destino_padrao = Path.home()

        self.categorias = ('Arquivo Imagem', 'Arquivos de Vídeo', 'Arquivos de Leitura',
                           'Arquivos execução', 'Arquivos compreesão')
        self.extensoes_imagem = ('JPG', 'PNG', 'GIF', 'BMP', 'Bitmap', 'TIFF', 'RAW', 'EXIF', 'PPM', 'PGM', 'PBM', 'PNM'
                                 , 'SVG', 'WebP',)
        self.extensoes_videos = ('MP4', 'AVI', 'MKV', 'MOV', 'WMV', 'FLV', 'AVCHD', 'F4V', 'SWF', 'WEBM', 'HTML5',
                                 'WEBM')
        self.extensoes_textos = (
            'TXT', 'PDF', 'DOCX', 'DOC', 'HTML', 'HTM', 'ODT', 'XLS', 'XLSX', 'ODS', 'PPT', 'PPTX')
        self.extensoes_execul = ('EXE', 'DLL', 'IN', 'BAT')
        self.extensoes_arqzip = ('ZIP', '')

        self.ativo_imagem = False
        self.ativo_Videos = False
        self.ativo_textos = False
        self.ativo_execul = False
        self.ativo_arqzip = False
        self.call_windows = False

        # janela princpal
        janela_principal = tk.Tk()
        janela_principal.geometry('450x450')
        janela_principal.config(padx=5, pady=5)
        janela_principal.title('V_008')

        # Relogio
        label_frame_relogio = tk.LabelFrame(janela_principal, text='Hora Certa')
        label_frame_relogio.pack(anchor='center', fill=tk.BOTH)
        label_hora = tk.Label(label_frame_relogio, text=f'{data_certa} - {hora_certa}', justify='center')
        label_hora.pack(anchor='center')

        # Combo
        self.variavel_combo = tk.StringVar()
        label_frame_combo = tk.LabelFrame(janela_principal, text='Categorias de arquivos')
        label_frame_combo.pack(fill=tk.BOTH)
        self.combo_principal = Combobox(label_frame_combo, textvariable=self.variavel_combo, justify='center')
        self.combo_principal['values'] = self.categorias
        self.combo_principal.set('Escolha uma categoria')
        self.combo_principal.current()
        self.combo_principal.pack(fill=tk.BOTH, pady=5, padx=5)
        self.variavel_combo.trace('w', self.combo_selecao_categoria)

        # lista principal
        self.variavel_lista_principal = tk.IntVar()
        label_frame_lista = tk.LabelFrame(janela_principal, text='Escolha uma extensão')  # label_frame_lista
        label_frame_lista.pack(side='top', fill=tk.BOTH)  # label_frame_lista
        barra_rolagem = tk.Scrollbar(label_frame_lista)  # Barra rolagem principal
        barra_rolagem.pack(side=tk.RIGHT, fill=tk.Y)  # Barra rolagem principal
        self.lista_principal = tk.Listbox(label_frame_lista, selectmode=tk.SINGLE, justify='center')  # Lista Principal
        self.lista_principal.pack(fill=tk.BOTH, pady=3, padx=3)  # Lista Principal
        barra_rolagem.config(command=self.lista_principal.yview)  # Barra rolagem principal
        self.lista_principal.config(yscrollcommand=barra_rolagem.set)  # Barra rolagem principal

        # Botoes
        label_frame_botao_princial = tk.LabelFrame(janela_principal, text="Escolha uma Opcão")
        label_frame_botao_princial.pack(fill=tk.BOTH)
        label_frame_iniciar_busca = tk.LabelFrame(label_frame_botao_princial, text='Buscando por arquivos')
        label_frame_iniciar_busca.pack(anchor='n')

        botao_iniciar_busca = tk.Button(label_frame_iniciar_busca, text='Iniciar busca', width=20, height=1,
                                        command=self.janela_busca)
        botao_iniciar_busca.pack(anchor='center', pady=3, padx=3)

        label_frame_botao_especif = tk.LabelFrame(label_frame_botao_princial, text='Digite uma extensão para busca',
                                                  width=20, height=1)
        label_frame_botao_especif.pack(side='left')
        botao_busca_especifica = tk.Button(label_frame_botao_especif, text='Buscando por extensão especifica', width=20,
                                           height=1)
        botao_busca_especifica.pack(anchor='center', pady=3, padx=3)

        label_frame_sair_programa = tk.LabelFrame(label_frame_botao_princial, text='Saindo do programa', width=20,
                                                  height=1)
        label_frame_sair_programa.pack(side='right')
        botao_sair_programa = tk.Button(label_frame_sair_programa, text='Fechar Programa', width=20, height=1,
                                        command=janela_principal.destroy)
        botao_sair_programa.pack(anchor='center', pady=3, padx=3)

        janela_principal.mainloop()

    def combo_selecao_categoria(self, *args):
        valor_categoria = self.variavel_combo.get()
        self.lista_principal.delete('0', 'end')

        if valor_categoria == 'Arquivo Imagem':
            self.ativo_imagem = True
            for valor_lista in self.extensoes_imagem:
                self.lista_principal.insert('end', valor_lista)

        elif valor_categoria == 'Arquivos de Vídeo':
            self.ativo_Videos = True
            for valor_lista in self.extensoes_videos:
                self.lista_principal.insert('end', valor_lista)

        elif valor_categoria == 'Arquivos de Leitura':
            self.ativo_textos = True
            for valor_lista in self.extensoes_textos:
                self.lista_principal.insert('end', valor_lista)

        elif valor_categoria == 'Arquivos execução':
            self.ativo_execul = True
            for valor_lista in self.extensoes_execul:
                self.lista_principal.insert('end', valor_lista)

        elif valor_categoria == 'Arquivos compreesão':
            self.ativo_arqzip = True
            for valor_lista in self.extensoes_arqzip:
                self.lista_principal.insert('end', valor_lista)

        print(f'Valor da Categoria da lista - [{valor_categoria}]')

    def fechar_janela_busca(self):
        self.janela_busca.destroy()

    def janela_busca(self):
        global valor_selecao
        valor_opcao_selecao = self.lista_principal.curselection()
        for valor_selecao in valor_opcao_selecao:
            print(f'Valor da seleção - [{valor_selecao}]')
            pass

        if self.ativo_imagem:
            self.valor_extensao_busca = self.extensoes_imagem[valor_selecao]
            print(f'Valor extensão IMAGEM {self.valor_extensao_busca}')

        elif self.ativo_Videos:
            self.valor_extensao_busca = self.extensoes_videos[valor_selecao]
            print(f'Valor extensão VIDEOS {self.valor_extensao_busca}')

        elif self.ativo_textos:
            self.valor_extensao_busca = self.extensoes_textos[valor_selecao]
            print(f'Valor extensão TEXTO {self.valor_extensao_busca}')

        elif self.ativo_execul:
            self.valor_extensao_busca = self.extensoes_execul[valor_selecao]
            print(f'Valor extensão EXE {self.valor_extensao_busca}')

        elif self.ativo_arqzip:
            self.valor_extensao_busca = self.extensoes_arqzip[valor_selecao]
            print(f'Valor extensão ZIP {self.valor_extensao_busca}')

        print(f'Valor da exntesão - [{self.valor_extensao_busca}]')

        sleep(2)
        # Janela de busca
        self.janela_busca = tk.Tk()
        self.janela_busca.config(padx=5, pady=5)
        self.janela_busca.geometry('900x500')
        self.janela_busca.title(f'Buscar por arquivos')

        # Label Frame horario
        label_frame_hora = tk.LabelFrame(self.janela_busca, text='Hora Certa')
        label_frame_hora.pack(fill=tk.BOTH)
        label_hora_data = tk.Label(label_frame_hora, text=f'{data_certa} - {hora_certa}', justify='center')
        label_hora_data.pack(anchor='center')

        # Listagem da busca

        label_frame_lista_busca = tk.LabelFrame(self.janela_busca, text='Resultado da Busca', border=2)
        label_frame_lista_busca.pack(fill=tk.BOTH)
        label_lista_busca = tk.Label(self.janela_busca, text='Arquivos encontrados:')
        label_lista_busca.pack(side='top', padx=5, pady=5)

        # BARRA ROLAGEM
        barra_rolagem_busca_Y = tk.Scrollbar(label_frame_lista_busca)
        barra_rolagem_busca_Y.pack(fill=tk.Y, side='right')
        barra_ralagem_busta_X = tk.Scrollbar(label_frame_lista_busca, orient=tk.HORIZONTAL)
        barra_ralagem_busta_X.pack(fill=tk.X, side='bottom')

        self.variavel_lista_busca = tk.IntVar()
        self.lista_busca = tk.Listbox(label_frame_lista_busca, listvariable=self.variavel_lista_busca,
                                      selectmode=tk.SINGLE, justify='left')
        self.lista_busca.pack(fill=tk.BOTH, anchor='center', padx=5, pady=5)

        barra_rolagem_busca_Y.config(command=self.lista_busca.yview)
        self.lista_busca.config(yscrollcommand=barra_rolagem_busca_Y.set)
        barra_ralagem_busta_X.config(command=self.lista_busca.xview)
        self.lista_busca.config(xscrollcommand=barra_ralagem_busta_X.set)

        # Label Frame botão
        label_botao_geral = tk.LabelFrame(self.janela_busca, border=2)
        label_botao_geral.pack(anchor='center', fill='both')

        # botao iniciar
        frame_botao_iniciar = tk.Frame(label_botao_geral)
        frame_botao_iniciar.pack(anchor='center', padx=5, pady=5)
        botao_iniciar_busca = tk.Button(frame_botao_iniciar, text='Iniciar', border=5, width=20, height=1,
                                        command=self.thead_iniciar_processo_busca)
        botao_iniciar_busca.pack(anchor='center', ipady=5, ipadx=5)

        # BOTAO SAIR
        frame_botao_fechar_app = tk.Frame(label_botao_geral)
        frame_botao_fechar_app.pack(side='right', ipady=5, padx=5)
        botao_fechar_app = tk.Button(frame_botao_fechar_app, text='Voltar ao menu principal', border=5, width=20,
                                     height=1, command=self.fechar_janela_busca)
        botao_fechar_app.pack(anchor='center', ipady=5, ipadx=5)

        # INFORMAÇÃO SOBRE DESTINO
        frame_botao_destino = tk.Frame(label_botao_geral)
        frame_botao_destino.pack(side='left', padx=5, pady=5)
        self.var_destino_da_busca = tk.StringVar()
        self.var_destino_da_busca.set(f'Destino padrão - [{self.pasta_destino_padrao}]')
        self.label_info_destino = tk.Label(frame_botao_destino, text=self.var_destino_da_busca.get())
        self.label_info_destino.pack(anchor='n')
        botao_destino_busca = tk.Button(frame_botao_destino, text='Escolher outro destino', border=2,
                                        command=self.conf_destino_da_busca)
        botao_destino_busca.pack(anchor='center', padx=4, pady=4)

        # MENSAGEM EM GERAL
        var_msg_estatus = tk.StringVar()
        label_frame_msg_busca_geral = tk.LabelFrame(self.janela_busca, text='Extensão selecionada!')
        label_frame_msg_busca_geral.pack(anchor='center')
        self.label_msg_busca = tk.Label(label_frame_msg_busca_geral, text=var_msg_estatus.get(), relief='raised')
        self.label_msg_busca.pack(anchor='center', ipady=4, ipadx=4)
        self.label_msg_busca['text'] = self.valor_extensao_busca

    # Funções complexas
    def conf_destino_da_busca(self):
        self.destino_ativo = True
        self.pasta_destino_padrao = Path(askdirectory())
        self.label_info_destino['text'] = self.pasta_destino_padrao
        showinfo('AVISO', F'Buscar no diretorio [{self.pasta_destino_padrao}]')

        # THREADS

    def thead_iniciar_processo_busca(self):
        Thread(target=self.iniciando_processo_busca()).start()

    def thread_save_busca(self):
        pass

    def iniciando_processo_busca(self):
        print(self.valor_extensao_busca)
        valor_da_busca = self.valor_extensao_busca

        try:
            pasta_destino = Path(self.pasta_destino_padrao)
            for resultado_da_busca in pasta_destino.glob('**/*' + valor_da_busca):
                if resultado_da_busca.is_file():
                    Thread(self.lista_busca.insert('end', resultado_da_busca))
                elif resultado_da_busca.is_dir():
                    Thread(self.lista_busca.insert('end', resultado_da_busca))
        except:
            showerror('AVISO', 'Não foi possível ler nenhuma extensão')


obj_principal = CorpoPrincipal()
