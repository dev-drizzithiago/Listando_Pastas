"""#### Declaração de Modulos"""
import os.path
from tkinter.messagebox import showwarning
from tkinter.filedialog import askdirectory
from tkinter.ttk import *
import tkinter as tk

"""#### Modulos do sistema"""
from os import walk
from re import search

"""### Modulos básicos"""
from time import sleep
from pathlib import Path
from datetime import datetime

"""# Modulo THREAD"""
from threading import Thread


class ProgramaPrincipal:
    def __init__(self):
        """##### Declarações de variaveis"""
        tipos_categorias = ['AUDIO', 'VIDEOS', 'TEXTOS', 'IMAGEM', 'ARQUIVOS', 'ACCESS', 'WORD', 'POWERPOINT', 'HTML',
                            'POWERPOINT', 'EXCEL']
        self.tempo_gasto_da_busca = None
        # ______________________________________________________________________________________________________________
        """# Pasta padrão da busca; sempre tento usar a pasta do usuário"""
        self.diretorio_home = Path.home()
        # ______________________________________________________________________________________________________________
        """#### Declaraçõas de ativações"""
        self.ativar_combo = False
        self.ativo_time_busca = False
        self.ativar_selecionar_pasta_destino = False
        self.ativar_arquivo_encontrado = False

        # -=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
        """# Janela principal"""
        self.janela_principal = tk.Tk()
        self.janela_principal.title('V_010')
        self.janela_principal.config(bg='#DCDCDC')
        self.janela_principal.geometry('1000x680+150+5')
        self.janela_principal.resizable(0, 0)

        # -=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
        """#### LabelFrame Principal"""
        self.label_frame_principal = tk.LabelFrame(self.janela_principal)
        self.label_frame_principal.config(text='Bem vindo ao buscador de arquivos!')
        self.label_frame_principal.config(bg='#DCDCDC')
        self.label_frame_principal.config(width=910, height=650)
        self.label_frame_principal.place(y=5, x=45)
        # -=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
        # ______________________________________________________________________________________________________________
        # -=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
        """#### FRAMES"""

        """# Frame SUPERIOR: Responsavel por mostrar as opções de buscas"""
        self.frames_superior = tk.Frame(self.janela_principal, bg='#A9A9A9')
        self.frames_superior.config(width=900, height=200)
        self.frames_superior.place(y=20, x=50)
        # ______________________________________________________________________________________________________________
        """COMBO BOX"""
        self.var_combo_box_categoria = tk.StringVar()
        self.combo_box_cat = Combobox(self.frames_superior)
        self.combo_box_cat.place(y=3, x=10)
        self.combo_box_cat.config(textvariable=self.var_combo_box_categoria, width=143)
        self.combo_box_cat.config(values=tipos_categorias, justify='center')
        self.combo_box_cat.set('Escolha uma categoria')
        self.var_combo_box_categoria.trace('w', self.selecao_combo_extensao)
        # ______________________________________________________________________________________________________________

        # -=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
        """# Frame Central: Reposanvel por mostrar as informações da busca"""
        self.frames_central = tk.Frame(self.janela_principal, bg='#C0C0C0')
        self.frames_central.config(width=900, height=120)
        self.frames_central.config(bd=2)
        self.frames_central.place(y=225, x=50)
        # ______________________________________________________________________________________________________________
        """#### Labels"""

        """# Label INFO categoria combo"""
        self.var_lbl_ext_cat = tk.StringVar()
        self.label_ext_cat = tk.Label(self.frames_central, text=self.var_lbl_ext_cat)
        self.label_ext_cat.config(text='Aguardado informações de Categoria', bg='#C0C0C0')
        self.label_ext_cat.place(y=1, x=1)
        # ______________________________________________________________________________________________________________
        """# Label INFO quantidade de arquivos encontrados"""
        self.var_lbl_qtd_arquivos = tk.StringVar()
        self.lbl_qtd_arquivos = tk.Label(self.frames_central, text=self.var_lbl_qtd_arquivos)
        self.lbl_qtd_arquivos.config(text='Quantidade de arquivos encontrados', bg='#C0C0C0')
        self.lbl_qtd_arquivos.place(y=1, x=225)
        # ______________________________________________________________________________________________________________
        """# Label INFO hora certa"""
        self.var_lbl_hora_certa = tk.StringVar()
        self.lbl_hora_certa = tk.Label(self.frames_central, text=self.var_lbl_hora_certa)
        self.lbl_hora_certa.config(bg='#C0C0C0')
        self.lbl_hora_certa.place(y=1, x=680)
        # ______________________________________________________________________________________________________________
        """# Label INFO pasta destino"""
        self.var_lbl_pts_dest = tk.StringVar()
        self.lbl_pts_dest = tk.Label(self.frames_central, text=self.var_lbl_pts_dest)
        self.lbl_pts_dest.config(text=f'Pasta padrão de busca: [{self.diretorio_home}]', bg='#C0C0C0')
        self.lbl_pts_dest.place(y=20, x=1)
        # ______________________________________________________________________________________________________________
        """# Label INFO tempo da busca"""
        self.var_lbl_tempo_busca = tk.StringVar()
        self.lbl_tempo_busca = tk.Label(self.frames_central, text=self.var_lbl_tempo_busca)
        self.lbl_tempo_busca.config(text='Tempo de busca', bg="#C0C0C0")
        self.lbl_tempo_busca.place(y=20, x=680)
        # ______________________________________________________________________________________________________________
        """# Label INFO extensões selecionadas"""
        self.var_lbl_ext_selec = tk.StringVar()
        self.lbl_ext_selec = tk.Label(self.frames_central, text=self.var_lbl_ext_selec)
        self.lbl_ext_selec.config(text=f'Aguardando informações', bg='#C0C0C0')
        self.lbl_ext_selec.place(y=40, x=1)
        # ______________________________________________________________________________________________________________
        """# Label INFO arquivos encontrados em real time"""
        self.var_lbl_info_real_time = tk.StringVar()
        self.lbl_info_real_time = tk.Label(self.frames_central, text=self.var_lbl_info_real_time)
        self.lbl_info_real_time.config(text='Arquivos encontrados em real time', bg='#C0C0C0')
        self.lbl_info_real_time.place(y=40, x=1)
        # ______________________________________________________________________________________________________________
        """# Barra progresso"""
        self.barra_progresso_busca = Progressbar(self.frames_central, orient=tk.HORIZONTAL)
        self.barra_progresso_busca.config(mode='determinate', length=886)
        self.barra_progresso_busca.config()
        self.barra_progresso_busca.place(y=90, x=5)
        # ______________________________________________________________________________________________________________
        """#### Frame Centro 2"""

        """# Frame Central 2: Reposanvel por mostrar o resultado da busca"""
        self.frames_central_2 = tk.Frame(self.janela_principal)
        self.frames_central_2.config(width=900, height=100, bg='#C0C0C0')
        # self.frames_central_2.place(y=350, x=50)
        # ______________________________________________________________________________________________________________
        """# Lista de busca"""
        self.var_lista_result_busca = tk.IntVar()
        self.lista_de_result_busca = tk.Listbox(self.janela_principal, width=99, height=5, bg='#C0C0C0')
        self.lista_de_result_busca.config(font='Arial', justify='left', selectmode=tk.SINGLE)
        self.lista_de_result_busca.place(y=350, x=52)
        # ______________________________________________________________________________________________________________
        """# Barra de Rolagem Y """
        self.barra_rolagem_lista_busca_y = Scrollbar(self.lista_de_result_busca, orient=tk.VERTICAL)
        self.barra_rolagem_lista_busca_y.place(y=20, x=870)
        self.barra_rolagem_lista_busca_y.config(command=self.lista_de_result_busca.yview)
        self.lista_de_result_busca.config(yscrollcommand=self.barra_rolagem_lista_busca_y.set)
        # ______________________________________________________________________________________________________________
        """# Barrade de Rolagem X """
        self.barra_rolagem_lista_busca_x = Scrollbar(self.lista_de_result_busca, orient=tk.HORIZONTAL)
        self.barra_rolagem_lista_busca_x.place(y=75, x=400)
        self.barra_rolagem_lista_busca_x.config(command=self.lista_de_result_busca.xview)
        self.lista_de_result_busca.config(yscrollcommand=self.barra_rolagem_lista_busca_x.set)
        # ______________________________________________________________________________________________________________

        # -=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
        """# Frame Inferior: Responsável por registro das informações de busca"""
        self.frames_inferior = tk.Frame(self.janela_principal, bg='#D3D3D3')
        self.frames_inferior.config(width=900, height=200, bd=2)
        self.frames_inferior.place(y=450, x=50)
        # ______________________________________________________________________________________________________________
        """# Label Frames dos botões"""

        """# Label Frame INICIO"""
        self.frame_label_inicio = tk.LabelFrame(self.frames_inferior, text='Inicio')
        self.frame_label_inicio.config(bg='#D3D3D3', pady=5, padx=5)
        self.frame_label_inicio.place(y=0, x=1)
        # ______________________________________________________________________________________________________________
        """# Label Frame Diretorio"""
        self.frame_label_diretorio = tk.LabelFrame(self.frames_inferior, text='Destino')
        self.frame_label_diretorio.config(bg='#D3D3D3', pady=5, padx=5)
        self.frame_label_diretorio.place(y=65, x=1)
        # ______________________________________________________________________________________________________________
        """# Frame Label para botão de limpeza da lista de extensões"""
        self.frame_label_limpeza_chk = tk.LabelFrame(self.frames_inferior, text='Destino')
        self.frame_label_limpeza_chk.config(bg='#D3D3D3', pady=5, padx=5)
        self.frame_label_limpeza_chk.place(y=130, x=1)
        # ______________________________________________________________________________________________________________
        """### BOTÕES """

        """# Botão INICIAR PROCESSO"""
        self.botao_inicio_processo = tk.Button(self.frame_label_inicio, text='Iniciar Processo')
        self.botao_inicio_processo.config(width=15, pady=5, padx=5, bg='#D3D3D3')
        self.botao_inicio_processo.config(command=self.thread_botao_inicio_da_busca)
        self.botao_inicio_processo.pack(anchor='n', fill='both')
        # ______________________________________________________________________________________________________________
        """# Botao Pasta destino"""
        self.botao_destino_busca = tk.Button(self.frame_label_diretorio, text='Pasta Destino')
        self.botao_destino_busca.config(width=15, pady=5, padx=5, bg='#D3D3D3')
        self.botao_destino_busca.config(command=self.thread_botao_pasta_destino)
        self.botao_destino_busca.pack(anchor='n', fill='both')
        # ______________________________________________________________________________________________________________
        """# Botão limpeza lista de extensão"""
        self.botao_limpar_checkbuttun = tk.Button(self.frame_label_limpeza_chk, text='Limpar Lista Extensão')
        self.botao_limpar_checkbuttun.config(width=15, pady=5, padx=5, bg='#D3D3D3')
        self.botao_limpar_checkbuttun.config(command=self.thread_botao_limpeza_checkbutton)
        self.botao_limpar_checkbuttun.pack(anchor='n', fill='both')

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
        lista_de_extensoes = dict(
            AUDIO=['aac', 'adt', 'adts', 'cda', 'm4a', 'mp3', 'wav', 'aif', 'aifc', 'aiff', 'mid', 'midi'],
            VIDEOS=['flv', 'mov', 'mp4', 'mpeg', 'mpg', 'vob', 'wmv', 'IFF'   'AVI'  'ASF', 'DVR-MS', 'MOV', 'MPEG-2',
                    'Ogg', 'OGM', 'RealMedia', 'Matroska', 'MKV', '3gp', 'VOB'],
            TEXTOS=['pdf', 'rtf', 'wbk', 'wpd', 'wp5', 'txt', 'log', 'xml'],
            IMAGEM=['ai', 'art', 'blend', 'bmp', 'cdr', 'cgm', 'cin', 'cpt', 'dpx', 'dxf', 'dwg', 'eps', 'emf', 'exr',
                    'fla', 'swf', 'fpx', 'gif', 'iff', 'ilbm', 'jpeg', 'jpg', 'jpg2', 'jp2', 'mng', 'pbm', 'pcd', 'pdf',
                    'pgm', 'pict', 'png', 'ppm', 'ps', 'psd', 'psp', 'svg', 'svgz', 'skp', 'skb', 'swf', 'tiff', 'tif',
                    'wbmp', 'wmf', 'xar', 'xcf', 'xpm'],
            ARQUIVOS=['exe', 'dll', 'ini', 'in', 'bat', 'bin', 'cab', 'csv', 'dif', 'dll', 'iso', 'jar', 'msi', 'mui',
                      'rar', 'sys', 'tmp', 'wmd', 'py', 'lua', 'java', 'pas', 'r', 'rar', 'dmg', '7z', 'tar', 'aspx',
                      'php', 'css', 'ico', 'modell-usb', 'modell', 'version', 'gitattributes', 'awk', 'inc', 'lib',
                      'sdb', 'dat', 'bfc', 'data', 'properties', 'jar', 'src', 'cpx', 'tlb', 'rs', 'vbs', 'ax', 'acm',
                      'com', 'mof', 'nls', 'rsp', 'sdi', 'sep', 'tbl', 'tsp', 'uce', 'ocx', 'msc', 'rtf', 'drv', 'scr',
                      'cmd', 'conf', 'wsf', 'config', 'json', 'dtd', 'iec', 'ime', 'nsl'],
            ACCESS=['accdb', 'accde', 'accdr', 'accdt', 'mdb'],
            WORD=['doc', 'docm', 'docx', 'dot', 'dotx'],
            POWERPOINT=['pot', 'potm', 'potx', 'ppam', 'pps', 'ppsm', 'ppsx', 'ppt', 'pptm', 'pptx'],
            EXCEL=['xla', 'xlam', 'xll', 'xlm', 'xls', 'xlsm', 'xlsx', 'xlt', 'xltm', 'xltx'],
            HTML=['xps', 'htm', 'html'])

        valor_categoria_extensao = self.var_combo_box_categoria.get()
        print(f'\n Categoria selecionada: [{valor_categoria_extensao}]')
        self.combo_box_cat.config(state=tk.DISABLED)
        for chave, valor in lista_de_extensoes.items():
            if chave == valor_categoria_extensao:

                """# Label que mostra qual categoria foi escolhida."""
                self.label_ext_cat.config(text=f'Categoria selecionada: [{valor_categoria_extensao}]')

                """### Loop de para separar as extensões e criar um checkbutton para cada extensao"""
                print(f'{contador}-linhas{linhas}-colunas{colunas}')
                for valor_extensao in valor:
                    self.lista_var.append(tk.IntVar())
                    self.botoes_chek.append(tk.Checkbutton(self.frames_superior, text=valor_extensao.upper(),
                                                           variable=self.lista_var[contador],
                                                           bg='#A9A9A9'))
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

    def data_hora_certa(self):
        """

        :return:
        """
        valor_data = datetime.now()
        self.data_certa = valor_data.strftime('%d/%m/%Y')
        self.hora_certa = valor_data.strftime("%H:%M")
        self.lbl_hora_certa.config(text=f'Inicio do programa:[{self.hora_certa}-{self.data_certa}]')

    def botao_limpeza_checkbutton_destroy(self):
        print(f'\nRemovendo os botões check\n')
        if self.ativar_combo:
            for valor_destroy in self.botoes_chek:
                valor_destroy.destroy()

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

                self.lbl_tempo_busca['text'] = msg_info_time
                self.tempo_gasto_da_busca = msg_info_time
                contagem_segundos += 1
                sleep(1)

    def botao_pasta_destino(self):
        print(f'botao_pasta_destino sendo ativado')
        self.ativar_selecionar_pasta_destino = True
        self.diretorio_home = Path(askdirectory())
        self.lbl_pts_dest.config(text=f'Pasta de busca: [{self.diretorio_home}]', bg='#C0C0C0')

    def botao_inicio_da_busca_principal(self):
        """

        :return:
        """
        extensoes = list()
        contador_de_arquivos = 0
        contador_de_pastas = 0
        contador_inicio = 1
        contador_itens = 1

        print(f'Combo ativado: {self.ativar_combo}')
        if self.ativar_combo:
            """# Desativando todos os botãoes"""
            self.botao_inicio_processo.config(state=tk.DISABLED)
            self.botao_limpar_checkbuttun.config(state=tk.DISABLED)
            self.botao_destino_busca.config(state=tk.DISABLED)
            self.combo_box_cat.config(state=tk.DISABLED)

            """# Inicio da barra de progresso"""
            self.barra_progresso_busca.start()

            """# Iniciando tempo de busca"""
            self.ativo_time_busca = True
            self.thread_tempo_processo_busca()

            """# As informações das extensão chegou no loop abaixo"""
            for valor_var in range(len(self.lista_var)):
                if self.lista_var[valor_var].get() == 1:
                    print(f'Valor selecionado: {self.botoes_chek[valor_var]["text"]}')
                    extensoes.append(self.botoes_chek[valor_var]["text"])
            self.lbl_ext_selec.config(text=f'Extenções selecionadas para busca {extensoes}')

            """###### Inicio do processo de busca"""
            for raiz, subpasta, arquivo in walk(self.diretorio_home):

                """# Informa os valores dos contadores para analisar se esta tudo correto"""
                print(f'valor contador_inicio: {contador_inicio}')
                print(f'valor contador_itens: {contador_itens}')

                if contador_inicio == 1:
                    print(f'DIRETORIO RAIZ: {raiz}')

                    """# Os dados são inseridos dentro da lista, para que possoa aparecer na janela de busca"""
                    self.lista_de_result_busca.insert('end', '')
                    self.lista_de_result_busca.insert('end', f'>>>>>>>{raiz.upper()}<<<<<<<')
                    self.lista_de_result_busca.insert('end', f'{"===" * 20}\n')

                contador_inicio += 1
                contador_itens = 1

                for valor_itens in arquivo:

                    """# As 4 variaveis são responsaveis por dividir as informações, para dar mais destaque"""
                    caminho_completo = os.path.join(raiz, valor_itens)
                    diretorio_destaque = str(caminho_completo).split('.')[0].lower()
                    extensao_destaque = str(caminho_completo).split('.')[0].upper()
                    resultado_destaque = f'{diretorio_destaque} ==> [ {extensao_destaque} ]'

                    if search('txt', valor_itens):
                        print(f'Itens encontrados: [{contador_de_arquivos}]')
                        self.lbl_qtd_arquivos.config(text=f'Arquivos encontrados: [{contador_de_arquivos}]')

                        if contador_itens == 1:
                            print(f'\n{raiz}')
                            print('===' * 20, '\n')
                            self.lista_de_result_busca.insert('end', f'{raiz}\n')
                            self.lista_de_result_busca.insert('end', '===' * 10, '\n')
                        else:
                            print(f'{resultado_destaque}')
                            self.lbl_info_real_time.config(text=f'Arquivos encontrados: {resultado_destaque}')
                            self.lista_de_result_busca.insert('end', f'[ {resultado_destaque} ]')
                        contador_itens += 1
                        contador_de_arquivos += 1

            """###### Fim do processo de busca"""
            """# Desliga a barra de progresso, ao final da busca"""
            self.barra_progresso_busca.stop()
            self.barra_progresso_busca.config(value=100)

            """# Após as buscas finalizarem, os botões serão ativados"""
            self.thread_botao_limpeza_checkbutton()
            self.botao_inicio_processo.config(state=tk.NORMAL)
            self.botao_limpar_checkbuttun.config(state=tk.NORMAL)
            self.botao_destino_busca.config(state=tk.NORMAL)

            self.lbl_info_real_time.config(text=f'Todos arquivos encontrados!')

            """# Desativa o validador de arquivos encontrados"""
            self.ativar_arquivo_encontrado = False
        else:
            showwarning("IMPORTANTE AVISO!", 'Escolha uma categoria e posteriormente uma extensão')


iniciando_obj = ProgramaPrincipal()
