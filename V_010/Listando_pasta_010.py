"""#### Declaração de Modulos"""
from tkinter.messagebox import showwarning, showinfo, showerror
from tkinter.filedialog import askdirectory
from tkinter.ttk import *
import tkinter as tk
import os.path

"""#### Modulos do sistema"""
from os import walk
from re import search, findall

"""### Modulos básicos"""
from time import sleep
from pathlib import Path
from datetime import datetime

"""# Modulo THREAD"""
from threading import Thread


class ProgramaPrincipal:
    def __init__(self):

        """##### Declarações de variaveis"""
        tipos_categorias = ['ARQUIVOS', 'IMAGEM', 'VIDEOS', 'AUDIO', 'POWERPOINT', 'EXCEL', 'TEXTOS', 'PROGRAMACAO',
                            'ACCESS', 'WORD', 'HTML']
        tipos_categorias.sort()

        self.dados_do_processo_busca = list()
        self.tempo_gasto_da_busca = None
        # ______________________________________________________________________________________________________________
        """# Pasta padrão da busca; sempre tento usar a pasta do usuário"""
        self.func_pasta_destino()
        # ______________________________________________________________________________________________________________
        """#### Declaraçõas de ativações"""
        self.ativar_selecionar_pasta_destino = False
        self.ativar_arquivo_encontrado = False
        self.ativar_uma_extensao = False
        self.ativo_time_busca = False
        self.ativar_combo = False

        self.ativar_segundos = False
        self.ativar_minutos = False
        self.ativar_horas = False

        # -=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
        """# Janela principal"""
        self.janela_principal = tk.Tk()
        self.janela_principal.title('V_010')
        self.janela_principal.geometry('1100x680+150+5')
        self.janela_principal.resizable(0, 0)
        # self.thread_botao_duplicidade()
        # -=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
        """#### LabelFrame Principal"""
        self.label_frame_principal = tk.LabelFrame(self.janela_principal)
        self.label_frame_principal.config(text='Bem vindo ao buscador de arquivos!')
        self.label_frame_principal.config(width=1000, height=680)
        self.label_frame_principal.pack(fill=tk.BOTH, pady=5, padx=10)

        # -=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
        """#### FRAMES"""

        """$$$$$$$ Frame SUPERIOR: Responsavel por mostrar as opções de buscas"""
        self.frames_superior = tk.Frame(self.label_frame_principal, bg='#C0C0C0')
        self.frames_superior.config(width=1070, height=220)
        self.frames_superior.place(y=1, x=2)
        # ______________________________________________________________________________________________________________
        """COMBO BOX"""
        self.var_combo_box_categoria = tk.StringVar()
        self.combo_box_cat = Combobox(self.frames_superior)
        self.combo_box_cat.place(y=3, x=2)
        self.combo_box_cat.config(textvariable=self.var_combo_box_categoria, width=174)
        self.combo_box_cat.config(values=tipos_categorias, justify='center')
        self.combo_box_cat.set('Escolha uma categoria')
        self.var_combo_box_categoria.trace('w', self.selecao_combo_extensao)
        # ______________________________________________________________________________________________________________

        # -=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
        """$$$$$$$ Frame Central: Reposanvel por mostrar as informações da busca"""
        self.frames_central = tk.Frame(self.label_frame_principal, bg='#D3D3D3')
        self.frames_central.config(width=1070, height=120)
        self.frames_central.config(bd=2)
        self.frames_central.place(y=223, x=2)
        # ______________________________________________________________________________________________________________
        """#### Labels"""

        """# Label INFO categoria combo"""
        self.var_lbl_ext_cat = tk.StringVar()
        self.label_ext_cat = tk.Label(self.frames_central, text=self.var_lbl_ext_cat)
        self.label_ext_cat.config(text='Categoria', bg='#D3D3D3')
        self.label_ext_cat.place(y=1, x=1)
        # ______________________________________________________________________________________________________________
        """# Label INFO quantidade de arquivos encontrados"""
        self.var_lbl_qtd_arquivos = tk.StringVar()
        self.lbl_qtd_arquivos = tk.Label(self.frames_central, text=self.var_lbl_qtd_arquivos)
        self.lbl_qtd_arquivos.config(text='Quantidade de arquivos encontrados', bg='#D3D3D3')
        self.lbl_qtd_arquivos.place(y=1, x=400)
        # ______________________________________________________________________________________________________________
        """# Quantidade de pastas que foram encontrado arquivos"""
        self.var_lbl_qtd_pasta = tk.StringVar()
        self.lbl_qtd_pasta = tk.Label(self.frames_central, text=self.var_lbl_qtd_pasta)
        self.lbl_qtd_pasta.config(text='Quantidade de pastas verificadas: ', bg='#D3D3D3')
        self.lbl_qtd_pasta.place(y=20, x=400)
        # ______________________________________________________________________________________________________________
        """# Label INFO hora certa"""
        self.var_lbl_hora_certa = tk.StringVar()
        self.lbl_hora_certa = tk.Label(self.frames_central, text=self.var_lbl_hora_certa)
        self.lbl_hora_certa.config(bg='#D3D3D3')
        self.lbl_hora_certa.place(y=1, x=855)
        # ______________________________________________________________________________________________________________
        """# Label INFO tempo da busca"""
        self.var_lbl_tempo_busca = tk.StringVar()
        self.lbl_tempo_busca = tk.Label(self.frames_central, text=self.var_lbl_tempo_busca)
        self.lbl_tempo_busca.config(text='Tempo de busca', bg="#D3D3D3")
        self.lbl_tempo_busca.place(y=20, x=855)
        # ______________________________________________________________________________________________________________
        """# Label INFO pasta destino"""
        self.var_lbl_pts_dest = tk.StringVar()
        self.lbl_pts_dest = tk.Label(self.frames_central, text=self.var_lbl_pts_dest)
        self.lbl_pts_dest.config(text=f'Pasta padrão: [{self.diretorio_home}]', bg='#D3D3D3')
        self.lbl_pts_dest.place(y=40, x=1)
        # ______________________________________________________________________________________________________________
        """# Label INFO extensões selecionadas"""
        self.var_lbl_ext_selec = tk.StringVar()
        self.lbl_ext_selec = tk.Label(self.frames_central, text=self.var_lbl_ext_selec)
        self.lbl_ext_selec.config(text=f'Escolha uma extensão para busca', bg='#D3D3D3')
        self.lbl_ext_selec.place(y=20, x=1)
        # ______________________________________________________________________________________________________________
        """# Label INFO arquivos encontrados em real time"""
        self.var_lbl_info_real_time = tk.StringVar()
        self.lbl_info_real_time = tk.Label(self.frames_central, text=self.var_lbl_info_real_time)
        self.lbl_info_real_time.config(text='Arquivos encontrados: ', bg='#D3D3D3')
        self.lbl_info_real_time.place(y=60, x=1)
        # ______________________________________________________________________________________________________________
        """# Barra progresso"""
        self.barra_progresso_busca = Progressbar(self.frames_central, orient=tk.HORIZONTAL)
        self.barra_progresso_busca.config(mode='determinate', length=1060)
        self.barra_progresso_busca.place(y=90, x=1)

        # -=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
        """$$$$$$$ Frame Inferior: Responsável por registro das informações de busca"""
        self.frames_inferior = tk.Frame(self.label_frame_principal, bg='#DCDCDC')
        self.frames_inferior.config(width=1070, height=75, bd=2)
        self.frames_inferior.place(y=348, x=2)
        # ______________________________________________________________________________________________________________
        """# Label Frames dos botões"""

        """# Label Frame INICIO"""
        self.frame_label_inicio = tk.LabelFrame(self.frames_inferior, text='Iniciar busca')
        self.frame_label_inicio.config(bg='#DCDCDC', pady=5, padx=5)
        self.frame_label_inicio.place(y=5, x=1)
        # ______________________________________________________________________________________________________________
        """# Label Frame Diretorio"""
        self.frame_label_diretorio = tk.LabelFrame(self.frames_inferior, text='Pasta Destino')
        self.frame_label_diretorio.config(bg='#DCDCDC', pady=5, padx=5)
        self.frame_label_diretorio.place(y=5, x=140)
        # ______________________________________________________________________________________________________________
        """# Frame Label para botão de limpeza da lista de extensões"""
        self.frame_label_limpeza_chk = tk.LabelFrame(self.frames_inferior, text='Limpar listas')
        self.frame_label_limpeza_chk.config(bg='#DCDCDC', pady=5, padx=5)
        self.frame_label_limpeza_chk.place(y=5, x=785)
        # ______________________________________________________________________________________________________________
        """# Frame Label para botão de encontrar duplicidade"""
        self.frame_label_duplicidade = tk.LabelFrame(self.frames_inferior, text='Verificar Duplicidade')
        self.frame_label_duplicidade.config(bg='#DCDCDC', pady=5, padx=5)
        self.frame_label_duplicidade.place(y=5, x=925)
        # ______________________________________________________________________________________________________________
        """#### BOTÕES """

        """# Botão INICIAR PROCESSO"""
        self.botao_inicio_processo = tk.Button(self.frame_label_inicio, text='Aplicar')
        self.botao_inicio_processo.config(width=15, pady=5, padx=5, bg='#D3D3D3')
        self.botao_inicio_processo.config(command=self.thread_botao_inicio_da_busca)
        self.botao_inicio_processo.pack(anchor='n', fill='both')
        # ______________________________________________________________________________________________________________
        """# Botao Pasta destino"""
        self.botao_destino_busca = tk.Button(self.frame_label_diretorio, text='Aplicar')
        self.botao_destino_busca.config(width=15, pady=5, padx=5, bg='#D3D3D3')
        self.botao_destino_busca.config(command=self.thread_botao_pasta_destino)
        self.botao_destino_busca.pack(anchor='n', fill='both')
        # self.botao_destino_busca.bind("<Button-1>", self.evento_mouse)
        # ______________________________________________________________________________________________________________
        """# Botão limpeza lista de extensão"""
        self.botao_limpar_checkbuttun = tk.Button(self.frame_label_limpeza_chk, text='Aplicar')
        self.botao_limpar_checkbuttun.config(width=15, pady=5, padx=5, bg='#D3D3D3')
        self.botao_limpar_checkbuttun.config(command=self.thread_botao_limpeza_checkbutton)
        self.botao_limpar_checkbuttun.pack(anchor='n', fill='both')
        # ______________________________________________________________________________________________________________
        """# Botão limpeza lista de extensão"""
        self.botao_duplicidade = tk.Button(self.frame_label_duplicidade, text='Aplicar')
        self.botao_duplicidade.config(width=15, pady=5, padx=5, bg='#D3D3D3')
        self.botao_duplicidade.config(command=self.thread_botao_duplicidade, state=tk.DISABLED)
        self.botao_duplicidade.pack(anchor='n', fill='both')
        # ______________________________________________________________________________________________________________
        """# Frame Label Listas de buscas"""
        self.frame_label_lista_resultado = tk.LabelFrame(self.label_frame_principal, text='Resultado das buscas')
        self.frame_label_lista_resultado.config(width=983)
        self.frame_label_lista_resultado.place(y=430, x=1)
        # ______________________________________________________________________________________________________________
        """# Lista de busca"""
        self.var_lista_result_busca = tk.IntVar()
        self.lista_de_result_busca = tk.Listbox(self.label_frame_principal, width=117, height=10, bg='#DCDCDC')
        self.lista_de_result_busca.config(font='Arial', justify='left', selectmode=tk.SINGLE)
        self.lista_de_result_busca.place(y=435, x=2)
        # ______________________________________________________________________________________________________________
        """# Barra de Rolagem Y Lista RESULTADO"""
        self.barra_rolagem_lista_busca_y = Scrollbar(self.label_frame_principal, orient=tk.VERTICAL)
        self.barra_rolagem_lista_busca_y.place(in_=self.lista_de_result_busca, relx=1.0, relheight=1.0)
        self.barra_rolagem_lista_busca_y.place(bordermode='outside')
        self.barra_rolagem_lista_busca_y.config(command=self.lista_de_result_busca.yview)
        self.lista_de_result_busca.config(yscrollcommand=self.barra_rolagem_lista_busca_y.set)
        # ______________________________________________________________________________________________________________
        """# Barrade de Rolagem X Lista RESULTADO"""
        self.barra_rolagem_lista_busca_x = Scrollbar(self.label_frame_principal, orient=tk.HORIZONTAL)
        self.barra_rolagem_lista_busca_x.place(in_=self.lista_de_result_busca, relx=0.0, rely=1.0, relwidth=1.0)
        self.barra_rolagem_lista_busca_x.place(bordermode='outside')
        self.barra_rolagem_lista_busca_x.config(command=self.lista_de_result_busca.xview)
        self.lista_de_result_busca.config(yscrollcommand=self.barra_rolagem_lista_busca_x.set)
        # ______________________________________________________________________________________________________________
        """# Lista de Duplicados   DESATIVADO"""
        self.var_lista_duplicados = tk.IntVar()
        self.lista_duplicados = tk.Listbox(self.label_frame_principal, width=55, height=10, bg='#DCDCDC')
        self.lista_duplicados.config(font='Arial', justify='left', selectmode=tk.SINGLE)
        # self.lista_duplicados.place(y=435, x=550)
        # ______________________________________________________________________________________________________________
        """# Barra de Rolagem Y Lista Duplicados  DESATIVADO"""
        self.barra_rolagem_lista_duplicados_y = Scrollbar(self.label_frame_principal, orient=tk.VERTICAL)
        self.barra_rolagem_lista_duplicados_y.place(in_=self.lista_duplicados, relx=1.0, relheight=1.0)
        self.barra_rolagem_lista_duplicados_y.place(bordermode='outside')
        self.barra_rolagem_lista_duplicados_y.config(command=self.lista_duplicados.yview)
        self.lista_duplicados.config(yscrollcommand=self.barra_rolagem_lista_duplicados_y.set)
        # ______________________________________________________________________________________________________________
        """# Barrade de Rolagem X Lista Duplicados DESATIVADO"""
        self.barra_rolagem_lista_duplicados_x = Scrollbar(self.label_frame_principal, orient=tk.HORIZONTAL)
        self.barra_rolagem_lista_duplicados_x.place(in_=self.lista_duplicados, relx=0.0, rely=1.0, relwidth=1.0)
        self.barra_rolagem_lista_duplicados_x.place(bordermode='outside')
        self.barra_rolagem_lista_duplicados_x.config(command=self.lista_duplicados.xview)
        self.lista_duplicados.config(yscrollcommand=self.barra_rolagem_lista_duplicados_x.set)
        # ______________________________________________________________________________________________________________

        # -=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
        """#### Iniciando o relogio"""
        self.thread_hora_certa()

        # -=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
        """###### LOOP DA JANELA ######"""
        self.janela_principal.mainloop()

    """##### THREADS DOS BOTÕES"""

    def thread_botao_inicio_da_busca(self):
        """

        :return:
        """
        print(f'\n Iniciandoaò THREAD para função inicio_da_busca_principal')
        Thread(target=self.botao_inicio_da_busca_principal).start()

    def thread_botao_limpeza_checkbutton(self):
        """

        :return:
        """
        print(f'\n Iniciandoaò THREAD para função [limpeza_checkbutton_destroy]')
        Thread(target=self.botao_limpeza_checkbutton_destroy).start()

    def thread_botao_pasta_destino(self):
        print(f'\n Iniciandoaò THREAD para função [botao_pasta_destino]')
        Thread(target=self.botao_pasta_destino).start()

    def thread_hora_certa(self):
        print(f'Iniciando THREAD hora_certa')
        Thread(target=self.data_hora_certa).start()

    def thread_tempo_processo_busca(self):
        print(f'Iniciando THREAD tempo_precesso_busca')
        Thread(target=self.tempo_processo_busca).start()

    def thread_botao_duplicidade(self):
        print(f'Iniciando THREAD botao_duplicidade')
        Thread(target=self.func_botao_duplicidade).start()

    """#### Sistema de combo e criaçãodo checkbutton"""

    def selecao_combo_extensao(self, *args):
        self.ativar_combo = True
        print(f'Combo ativado: {self.ativar_combo}')
        """### Declaraçõa de variaveis básicas"""
        colunas = 1
        linhas = 25
        contador = 0
        self.lista_var = list()
        self.botoes_chek = list()
        self.destroy_botao = list()

        """### Declaraçõd do dicionário de extensões"""
        self.lista_de_extensoes = dict(

            ARQUIVOS=['exe', 'dll', 'ini', 'in', 'bat', 'bin', 'cab', 'csv', 'dif', 'dll', 'iso', 'jar', 'msi', 'mui',
                      'rar', 'sys', 'tmp', 'wmd', 'lua', 'pas', 'r', 'rar', 'dmg', '7z', 'tar', 'aspx', 'nsl', 'dtd',
                      'ico', 'modell-usb', 'modell', 'version', 'gitattributes', 'awk', 'inc', 'lib', 'iec', 'ime',
                      'sdb', 'dat', 'bfc', 'data', 'properties', 'jar', 'src', 'cpx', 'tlb', 'rs', 'ax', 'acm', 'json',
                      'com', 'mof', 'nls', 'rsp', 'sdi', 'sep', 'tbl', 'tsp', 'uce', 'ocx', 'msc', 'rtf', 'drv', 'scr',
                      'cmd', 'conf', 'wsf', 'config'],

            IMAGEM=['ai', 'art', 'blend', 'bmp', 'cdr', 'cgm', 'cin', 'cpt', 'dpx', 'dxf', 'dwg', 'eps', 'emf', 'exr',
                    'fla', 'swf', 'fpx', 'gif', 'iff', 'ilbm', 'jpeg', 'jpg', 'jpg2', 'jp2', 'mng', 'pbm', 'pcd', 'pdf',
                    'pgm', 'pict', 'png', 'ppm', 'ps', 'psd', 'psp', 'svg', 'svgz', 'skp', 'skb', 'swf', 'tiff', 'tif',
                    'wbmp', 'wmf', 'xar', 'xcf', 'xpm'],

            VIDEOS=['flv', 'mov', 'mp4', 'mpeg', 'mpg', 'vob', 'wmv', 'iff'   'avi'  'asf', 'dvr-ms', 'mov', 'mpeg-2',
                    'ogg', 'ogm', 'realMedia', 'matroska', 'MKV', '3gp', 'vob'],

            AUDIO=['aac', 'adt', 'adts', 'cda', 'm4a', 'mp3', 'wav', 'aif', 'aifc', 'aiff', 'mid', 'midi'],

            POWERPOINT=['pot', 'potm', 'potx', 'ppam', 'pps', 'ppsm', 'ppsx', 'ppt', 'pptm', 'pptx'],

            EXCEL=['xla', 'xlam', 'xll', 'xlm', 'xls', 'xlsm', 'xlsx', 'xlt', 'xltm', 'xltx'],

            TEXTOS=['pdf', 'rtf', 'wbk', 'wpd', 'wp5', 'txt', 'log', 'xml'],

            PROGRAMACAO=['py', 'java', 'vbs', 'css', 'php', 'pyi'],

            ACCESS=['accdb', 'accde', 'accdr', 'accdt', 'mdb'],

            WORD=['doc', 'docm', 'dot', 'dotx', 'docx'],

            HTML=['xps', 'htm', 'html'])

        valor_categoria_extensao = self.var_combo_box_categoria.get()
        self.categoria_filtro = self.var_combo_box_categoria.get()
        print(f'\n Categoria selecionada: [{valor_categoria_extensao}]')
        self.combo_box_cat.config(state=tk.DISABLED)
        for chave, valor in self.lista_de_extensoes.items():

            """# Define qual categoria de extensão vai ser apresentado na janela"""
            if chave == valor_categoria_extensao:

                """# Label que mostra qual categoria foi escolhida."""
                self.label_ext_cat.config(text=f'Categoria selecionada: [{valor_categoria_extensao}]')

                """### Loop de para separar as extensões e criar um checkbutton para cada extensao"""
                print(f'{contador}-linhas{linhas}-colunas{colunas}')  # Primeira linha dos codigos de linhas
                for valor_extensao in valor:
                    self.lista_var.append(tk.IntVar())
                    self.botoes_chek.append(tk.Checkbutton(self.frames_superior, text=valor_extensao.upper(),
                                                           variable=self.lista_var[contador],
                                                           bg='#C0C0C0'))
                    self.botoes_chek[-1].place(y=linhas, x=colunas)

                    if linhas == 195:
                        linhas = 25
                        colunas += 120
                    else:
                        linhas += 17
                    contador += 1

                    """### Mapeamento das coordenadas de criação das opções do checkbutton"""
                    print(f'{contador}-linhas[{linhas}]-colunas[{colunas}]')

    """#### Processos simples"""

    def evento_mouse(self):
        showinfo('Teste', 'teste')

    def data_hora_certa(self):
        """

        :return:
        """
        valor_data = datetime.now()
        self.data_certa = valor_data.strftime('%d/%m/%Y')
        self.hora_certa = valor_data.strftime("%H:%M")
        self.lbl_hora_certa.config(text=f'Inicio do programa:[{self.hora_certa}-{self.data_certa}]')

    def func_pasta_destino(self):
        # ______________________________________________________________________________________________________________
        """# Pasta padrão da busca; sempre tento usar a pasta do usuário"""
        self.diretorio_home = Path.home()

    def botao_limpeza_checkbutton_destroy(self):
        print(f'\nRemovendo os botões check\n')
        if self.ativar_combo:
            for valor_destroy in self.botoes_chek:
                valor_destroy.destroy()
            """# Tambem limpa a lista de busca"""
            self.lista_de_result_busca.delete('0', 'end')
            self.func_pasta_destino()
            self.lbl_pts_dest.config(text=self.diretorio_home)
        else:
            showwarning("AVISO", 'Não existe lista para limpar')
        self.ativar_combo = False
        self.lbl_ext_selec.config(text=f'Aguardando informações', bg='#C0C0C0')

        """# Ativação e reconfiguração do combo"""
        print(f'Atualizando as informações do Combo')
        self.combo_box_cat.set('Escolha uma categoria')
        self.combo_box_cat.config(state=tk.NORMAL)

        print(f'"Combo Ativado: {self.ativar_combo}')

    """#### Inicio dos processos """

    def tempo_processo_busca(self):
        """
        Função vai se responsavel em contar o tempo que a busca foi realizada.
        :return:
        """
        print('\nIniciando time da busca')
        msg_info_time = str
        contagem_segundos = 0
        contagem_minutos = 0
        contagem_horas = 0
        if self.ativo_time_busca:
            while self.ativo_time_busca:
                if contagem_segundos == 0:
                    msg_info_time = str(f'00:00:00')
                    self.lbl_tempo_busca['text'] = msg_info_time
                else:
                    # Contagem dos SEGUNDOS
                    if contagem_segundos < 10 and contagem_minutos == 0 and contagem_horas == 0:
                        msg_info_time = str(f'00:00:0{contagem_segundos}')
                        self.ativar_segundos = True
                    elif contagem_segundos > 9 and contagem_minutos == 0 and contagem_horas == 0:
                        msg_info_time = str(f'00:00:{contagem_segundos}')
                        self.ativar_segundos = True

                    # Contagem dos MINUTOS
                    elif contagem_segundos < 10 and contagem_minutos < 10 > 1 and contagem_horas == 0:
                        msg_info_time = str(f'00:0{contagem_minutos}:0{contagem_segundos}')
                        self.ativar_minutos = True
                        self.ativar_segundos = False
                    elif contagem_segundos > 9 and contagem_minutos < 10 and contagem_horas == 0:
                        msg_info_time = str(f'00:0{contagem_minutos}:{contagem_segundos}')
                        self.ativar_minutos = True
                        self.ativar_segundos = False
                    elif contagem_segundos < 10 and contagem_minutos > 9 and contagem_horas == 0:
                        msg_info_time = str(f'00:{contagem_minutos}:0{contagem_segundos}')
                        self.ativar_minutos = True
                        self.ativar_segundos = False
                    elif contagem_segundos > 9 and contagem_minutos > 9 and contagem_horas == 0:
                        msg_info_time = str(f'00:{contagem_minutos}:{contagem_segundos}')
                        self.ativar_minutos = True
                        self.ativar_segundos = False

                    # Contagem das horas
                    elif contagem_segundos < 10 and contagem_minutos < 10 and contagem_horas < 10:
                        msg_info_time = str(f'0{contagem_horas}:0{contagem_minutos}:0{contagem_segundos}')
                        self.ativar_horas = True
                        self.ativar_minutos = False
                        self.ativar_segundos = False
                    elif contagem_segundos > 9 and contagem_minutos < 10 and contagem_horas < 10:
                        msg_info_time = str(f'0{contagem_horas}:0{contagem_minutos}:{contagem_segundos}')
                        self.ativar_horas = True
                        self.ativar_minutos = False
                        self.ativar_segundos = False
                    elif contagem_segundos < 10 and contagem_minutos > 9 and contagem_horas < 10:
                        msg_info_time = str(f'0{contagem_horas}:{contagem_minutos}:0{contagem_segundos}')
                        self.ativar_horas = True
                        self.ativar_minutos = False
                        self.ativar_segundos = False
                    elif contagem_segundos > 9 and contagem_minutos > 9 and contagem_horas < 10:
                        msg_info_time = str(f'0{contagem_horas}:{contagem_minutos}:{contagem_segundos}')
                        self.ativar_horas = True
                        self.ativar_minutos = False
                        self.ativar_segundos = False
                    elif contagem_segundos < 10 and contagem_minutos < 10 and contagem_horas > 9:
                        msg_info_time = str(f'{contagem_horas}:0{contagem_minutos}:0{contagem_segundos}')
                        self.ativar_horas = True
                        self.ativar_minutos = False
                        self.ativar_segundos = False
                    elif contagem_segundos > 9 and contagem_minutos < 10 and contagem_horas > 9:
                        msg_info_time = str(f'{contagem_horas}:0{contagem_minutos}:{contagem_segundos}')
                        self.ativar_horas = True
                        self.ativar_minutos = False
                        self.ativar_segundos = False
                    elif contagem_segundos > 9 and contagem_minutos > 9 and contagem_horas > 9:
                        msg_info_time = str(f'{contagem_horas}:{contagem_minutos}:{contagem_segundos}')
                        self.ativar_horas = True
                        self.ativar_minutos = False
                        self.ativar_segundos = False

                    if contagem_segundos == 59:
                        if contagem_minutos == 59:
                            contagem_segundos = 0
                            contagem_minutos = 0
                            contagem_horas += 1
                        else:
                            contagem_segundos = 0
                            contagem_minutos += 1
                if self.ativar_segundos:
                    self.lbl_tempo_busca['text'] = f"{msg_info_time} Segundo's"
                elif self.ativar_minutos:
                    self.lbl_tempo_busca['text'] = f"{msg_info_time} Minuto's"
                elif self.ativar_horas:
                    self.lbl_tempo_busca['text'] = f"{msg_info_time} HORA'S"

                self.tempo_gasto_da_busca = msg_info_time
                contagem_segundos += 1
                sleep(1)

    def botao_pasta_destino(self):
        print(f'botao_pasta_destino sendo ativado')
        self.ativar_selecionar_pasta_destino = True
        self.diretorio_home = Path(askdirectory())
        self.lbl_pts_dest.config(text=f'Pasta de busca: [{self.diretorio_home}]', bg='#C0C0C0')

    def func_botao_duplicidade(self):
        from shutil import move
        from hashlib import md5
        arquivo_repetido = dict()
        lista_dados = list()

        def thread_lista_duplicado():
            Thread(target=processo_arquivo_duplicados).start()

        """##########################################################################################################"""
        """##########################################################################################################"""
        """##########################################################################################################"""
        """##########################################################################################################"""
        """# Proceddo de verificação das informaçoes"""

        def processo_arquivo_duplicados():
            for valor in self.dados_do_processo_busca:
                valor_item = str(valor).split('|')[1]

                if valor_item in arquivo_repetido:
                    arquivo_repetido[valor_item] += 1
                else:
                    arquivo_repetido[valor_item] = 1

            for k, v in arquivo_repetido.items():
                if v > 1:
                    print(f'Arquivo Repetido: {k} - Quantidade: {v}')
                    lista_result_duplicidade.insert('end', f'File: [ {k} ] - QTDS: [ {v} ]')

        """##########################################################################################################"""
        """##########################################################################################################"""
        """##########################################################################################################"""
        """##########################################################################################################"""
        """##########################################################################################################"""
        """##########################################################################################################"""

        """#### Janela de opções duplicados; só interno """
        janela_opc_duplicidade = tk.Tk()
        janela_opc_duplicidade.geometry('1000x600+200+50')
        janela_opc_duplicidade.resizable(0, 0)
        janela_opc_duplicidade.title('Verificando duplicidade!')
        # -=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
        """# Frame Principal DUPLICIDADE"""
        frame_label_duplicidade = tk.LabelFrame(janela_opc_duplicidade, text='Verificando duplicidade!')
        frame_label_duplicidade.config(width=900, height=580)
        frame_label_duplicidade.pack(fill=tk.BOTH, pady=5, padx=5)
        # -=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
        """# Lista de resultado dos arquivos duplicados"""
        var_result_duplicidade = tk.StringVar()
        lista_result_duplicidade = tk.Listbox(frame_label_duplicidade)
        lista_result_duplicidade.config(selectmode=tk.SINGLE, width=160, height=15)
        lista_result_duplicidade.place(y=3, x=3)
        # ______________________________________________________________________________________________________________
        """# Criando a barra de rolagem para lista de resultado"""
        barra_rolagem_lista_resultado_ducplicados = Scrollbar(janela_opc_duplicidade)
        barra_rolagem_lista_resultado_ducplicados.config(orient='vertical')
        barra_rolagem_lista_resultado_ducplicados.place(in_=lista_result_duplicidade)
        barra_rolagem_lista_resultado_ducplicados.place(relx=1.0, relheight=1.0)
        barra_rolagem_lista_resultado_ducplicados.place(bordermode='outside')
        barra_rolagem_lista_resultado_ducplicados.config(command=lista_result_duplicidade.yview)
        lista_result_duplicidade.config(yscrollcommand=barra_rolagem_lista_resultado_ducplicados.set)
        # -=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
        """Frame Superior duplicidade"""
        frame_superior_dupli = tk.Frame(frame_label_duplicidade, bg='#C0C0C0', width=980, height=150)
        frame_superior_dupli.place(y=250, x=3)
        # ______________________________________________________________________________________________________________
        # ______________________________________________________________________________________________________________
        frame_inferior_dupli = tk.Frame(frame_label_duplicidade, bg='#C0C0C0', width=980, height=150)
        frame_inferior_dupli.place(y=407, x=3)
        # ______________________________________________________________________________________________________________
        # ______________________________________________________________________________________________________________

        # -=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
        """# Chamada da função que vai processar as informações dos aquivos."""
        thread_lista_duplicado()

        """ Responsável por manter a janela de duplicidade ativa (padrão do tkinter)"""
        janela_opc_duplicidade.mainloop()

    def botao_inicio_da_busca_principal(self):
        """

        :return:
        """
        extensoes = list()
        contador_de_arquivos = 0
        contador_de_pastas = 0
        contador_inicio = 1
        contador_itens = 1
        valor_da_extensao_busca = None
        valor_de_busca = None

        print(f'Combo ativado: {self.ativar_combo}')

        if self.ativar_combo:

            """# As informações das extensão chegou no loop abaixo"""
            try:
                for valor_var in range(len(self.lista_var)):
                    if self.lista_var[valor_var].get() == 1:
                        extensoes.append(self.botoes_chek[valor_var]["text"])
                self.lbl_ext_selec.config(text=f'Você selecionou a extensão {extensoes} para busca.')
            except AttributeError:
                showwarning("AVISO", 'Você não selecionou nenhuma extensão')

            """# Valida se extensão possui mais de um valor"""
            if len(extensoes) == 1:
                self.ativar_uma_extensao = True
            elif len(extensoes) == 0:
                showwarning("AVISO", 'Você não selecionou nenhuma extensão, selecione uma')

            """# Prepara o valor para que a função re.search possa identificar """
            for valor_item_extensao in extensoes:
                valor_da_extensao_busca = str(valor_item_extensao).lower().strip()
            print(f'Valor da busca selecionado: {valor_da_extensao_busca}')

            if self.ativar_uma_extensao:
                """# Desativando todos os botãoes"""
                self.botao_inicio_processo.config(state=tk.DISABLED)
                self.botao_limpar_checkbuttun.config(state=tk.DISABLED)
                self.botao_destino_busca.config(state=tk.DISABLED)
                self.combo_box_cat.config(state=tk.DISABLED)

                self.lista_de_result_busca.delete(0, 'end')

                """# Inicio da barra de progresso"""
                self.barra_progresso_busca.start()

                """# Iniciando tempo de busca"""
                self.ativo_time_busca = True
                self.thread_tempo_processo_busca()

                """###### Inicio do processo de busca"""
                for raiz, subpasta, arquivo in walk(self.diretorio_home):

                    """# O contador de inicio ser para verificar se é a primeira pasta. Ja que o 'os.walk' mostra
                    todas as pastas, devido ao loop. Então essa condição evita que mostre todos as pastas descenecess"""
                    if contador_inicio == 1:
                        print()
                        print(f'DIRETORIO RAIZ: {raiz}')

                        """# Os dados são inseridos dentro da lista, para que possoa aparecer na janela de busca"""
                        self.lista_de_result_busca.insert('end', '')
                        self.lista_de_result_busca.insert('end', f'>>>>>>>{raiz.upper()}<<<<<<<')
                        self.lista_de_result_busca.insert('end', f'{"===" * 40}')

                    contador_inicio += 1

                    """# Por padrão, o contador_itens, começa com 1 no valor, após encontrar todos os arquivos dentros de 
                    uma pasta, o programa vai passar para próxima pasta e o contador chega no valor padrão. """
                    contador_itens = 1

                    """# Loop responsável por mostrar os arquivos """
                    for valor_file in arquivo:

                        """#### As linhas abaixo são responsáveis por buscar os arquivos especificados pelo usuário
                        São vários filtros para não jogar todos os arquivos"""
                        if search(valor_da_extensao_busca, valor_file):

                            self.lbl_qtd_arquivos.config(text=f'Quantidade de arquivos encontrados: '
                                                              f'[{contador_de_arquivos}]')

                            """# Realiza o filtro; o modulo 're.search' busca qualquer arquivo com uma string 'txt'.
                            Esse programa eu quero que pegue apenas os valores da extensão, e não valores que passa
                            esta contidos em testos como 'txt01.txt'"""
                            valor_ext_comparacao = str(valor_file).split('.')[-1]
                            try:
                                if valor_da_extensao_busca == valor_ext_comparacao:
                                    valor_of_file = str(f'{valor_file}').strip().lower()
                            except:
                                valor_of_file = valor_file

                            """# As 4 variaveis são responsaveis por dividir as informações, para dar mais destaque"""

                            caminho_completo = os.path.join(raiz, valor_of_file)
                            extensao_destaque = str(caminho_completo).split('\\')[-1].upper()
                            resultado_destaque = f'{raiz} ==> [ {extensao_destaque} ]'

                            """# Mostra a pasta que foram encontrado algum arquivo"""
                            if contador_itens == 1:
                                """# Conta quantas pastas foram encontrados os itens da busca"""
                                contador_de_pastas += 1
                                self.lbl_qtd_pasta.config(text=f'Quantidade de pastas verificadas:'
                                                               f' [{contador_de_pastas}]')
                                self.dados_do_processo_busca.append(f'{raiz}|{extensao_destaque}')
                                """ #Mostra o resultado da busca no prompt"""
                                print(f'\n{raiz}')
                                print('===' * 20)
                                print(f'[{resultado_destaque}]')

                                """# Mostra o resultado na lista de busca"""
                                self.lista_de_result_busca.insert('end', '')
                                self.lista_de_result_busca.insert('end', '')
                                self.lista_de_result_busca.insert('end', f'{raiz}')
                                self.lista_de_result_busca.insert('end', '===' * 40)
                                self.lista_de_result_busca.insert('end', f'[ {extensao_destaque} ]')
                            else:
                                """# Na lista abaixo, são inseridos todos os dados da busca para que possa ser 
                                realizado qualquer tipo de analise"""
                                self.dados_do_processo_busca.append(f'{raiz}|{extensao_destaque}')

                                """# Mostra os resultados no prompt e na lista de busca"""
                                print(f'[{resultado_destaque}]')
                                self.lbl_info_real_time.config(text=f'Arquivos encontrados: [ {valor_de_busca} ]')
                                self.lista_de_result_busca.insert('end', f'[ {extensao_destaque} ]')

                            """# Por padrão, o valor começa com 1, antes é anlisado se possui um arquivo que correponda
                             ao valor de extensão, caso seja, mostra a pasta que foi encontrado, mas depois passa a mostrar
                             apenas os arquivos dentro dessa pasta.
                              - Após mostrar a pasta, o contador passa a soma o valor para cada item."""
                            contador_itens += 1

                            """# Contador que é responsável pela quantidade de arquivos encontrados."""
                            contador_de_arquivos += 1

                """###### Fim do processo de busca"""
                """# Desliga a barra de progresso, ao final da busca"""
                self.barra_progresso_busca.stop()
                self.barra_progresso_busca.config(value=100)

                """# Após as buscas finalizarem, os botões serão ativados"""
                self.botao_inicio_processo.config(state=tk.NORMAL)
                self.botao_limpar_checkbuttun.config(state=tk.NORMAL)
                self.botao_destino_busca.config(state=tk.NORMAL)
                self.botao_duplicidade.config(state=tk.NORMAL)

                """# Número de itens encontrados"""
                self.lbl_info_real_time.config(text=f'Fim da BUSCA!')
                print(f'\nItens encontrados: [ {contador_de_arquivos} ]')

                """# Desativa o validador de tempo de busca"""
                print(f'\nDesativando "time_busca"')
                sleep(1)
                self.ativo_time_busca = False
                self.lbl_tempo_busca['text'] = f"A busca levou {self.tempo_gasto_da_busca} (H/M/S)"

                """# Desativa os valores importantes"""
                self.ativar_horas = False
                self.ativar_minutos = False
                self.ativar_segundos = False
                self.ativar_uma_extensao = False

                """# Desativa o validador de arquivos encontrados"""
                print(f'\nDesativando "arquivo_encontrado"')
                sleep(1)
                self.ativar_arquivo_encontrado = False

                self.lista_de_result_busca.insert('end', '')
                self.lista_de_result_busca.insert('end', '')
                self.lista_de_result_busca.insert('end', '===' * 40)
                self.lista_de_result_busca.insert('end', f'Busca finalizada!')

                print(f'\nBusca Finalizada')
                print(f'\nForam encontrados {contador_de_arquivos} arquivos, dentro de {contador_de_pastas} pastas')
            else:
                showwarning('AVISO', 'Escolha apenas um extensão')
        else:
            showwarning("IMPORTANTE AVISO!", 'Escolha uma categora e uma única extensão '
                                             'para realizar a busca.')


iniciando_obj = ProgramaPrincipal()
