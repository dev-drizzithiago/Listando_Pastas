import tkinter as tk
from tkinter.ttk import *

from winsound import PlaySound, SND_ASYNC
from time import sleep
from pathlib import Path
from threading import Thread
from datetime import datetime
from tkinter.messagebox import showerror, showwarning
from tkinter.simpledialog import askstring
from tkinter.filedialog import askdirectory, asksaveasfile

"""Modulo criado para salvar um documento em PDF"""
from lib_pdf import *

"""# Modulo para criar um grafico em diversos formatos"""
from lib_grafico import grafico_pizza, grafico_barras

valor_pasta_destino = Path().home()
pasta_arq_registro_extensao = str(Path(valor_pasta_destino, 'AppData', 'LocalLow', 'extensoes'))

# SONS
som_abrindo_programa = 'D:\Estudos\Python\GitHub\Listando_Pastas\V_009\sons\\abrindo_programa.wav'
som_botao = 'D:\Estudos\Python\GitHub\Listando_Pastas\V_009\sons\\apertando_botao.wav'
som_inicio_busca = 'D:\Estudos\Python\GitHub\Listando_Pastas\V_009\sons\inicio_busca.wav'
som_fim_processo = 'D:\Estudos\Python\GitHub\Listando_Pastas\V_009\sons\\final_busca.wav'


# _+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+
class ListandoArquivos:
    PlaySound(som_abrindo_programa, SND_ASYNC)

    def __init__(self):
        self.categorias_busca = ('Arquivo Imagem', 'Arquivos de Vídeos/Audios', 'Arquivos de Leitura',
                                 'Arquivos execução', 'Arquivos compreesão')

        self.lista_analise_arq_busca = list()
        self.lista_analise_pasta_busca = list()

        # _+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+
        self.ativo_add_ext_especifica = False
        self.ativo_finalizacao_busca = False
        self.ativo_itens_encontrados = False
        self.ativo_status_extensao = False
        self.ativo_status_destinos = False
        self.ativo_analise_dados = False
        self.ativo_inicio_busca = False
        self.ativo_busca_imagem = False
        self.ativo_busca_videos = False
        self.ativo_busca_textos = False
        self.ativo_busca_execul = False
        self.ativo_busca_arqzip = False
        self.ativo_time_busca = False
        self.ativo_true_busca = True

        # _+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+
        # Janela Principal
        self.janela_principal = tk.Tk()
        self.janela_principal.title('Versão 009')
        self.janela_principal.geometry('1000x800+150+5')
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
        """# Label FRAME PRINCIPAL"""
        self.label_frame_geral = LabelFrame(self.janela_principal, text='Janela Principal')
        self.label_frame_geral.pack(fill=tk.BOTH, pady=5, padx=5)

        # _+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+
        """# COMBO DE EXTENSÃO"""
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
        """# INFORMAÇÕES SOBRE EXTENSÃO"""
        self.label_lista_extensao = LabelFrame(self.label_frame_geral, text='Escolha uma extensão')
        self.label_lista_extensao.pack(side='top', fill='both', pady=2, padx=2)
        # BARRA DE ROLAGEM
        self.barra_rolagem_extensao = Scrollbar(self.label_lista_extensao, orient=tk.VERTICAL)
        self.barra_rolagem_extensao.pack(side='right', fill=tk.Y)

        """#### LISTA EXTENSAO"""
        self.lista_de_extensoes = tk.Listbox(self.label_lista_extensao, selectmode=tk.SINGLE, justify='center')
        self.lista_de_extensoes.config(height=2)
        self.lista_de_extensoes.config(selectforeground='#000000')
        self.lista_de_extensoes.config(selectbackground='#A9A9A9')
        self.lista_de_extensoes.config(selectborderwidth=5)
        self.lista_de_extensoes.pack(anchor='center', fill='both')

        """# BARRA ROLAGEM"""
        self.barra_rolagem_extensao.config(command=self.lista_de_extensoes.yview)
        self.lista_de_extensoes.config(yscrollcommand=self.barra_rolagem_extensao.set)

        """# LABEL DE INFORMAÇÕES"""
        self.label_frame_info_ext = LabelFrame(self.label_frame_geral, text='Extensão selecionada..!')
        self.label_frame_info_ext.pack(anchor='n')
        self.var_label_info_extensao = tk.StringVar()
        self.var_label_info_extensao.set(' Aguardando escolha da extensão ')
        self.label_info_extensao = Label(self.label_frame_info_ext, text=f'[{self.var_label_info_extensao.get()}]')
        self.label_info_extensao.pack(anchor='center')

        """# LABEL TIME DA BUSCA"""
        self.var_label_time_busca = tk.StringVar()
        self.var_label_time_busca.set('00:00:00')
        self.label_time_busca = Label(self.label_frame_geral, text=self.var_label_time_busca.get())
        self.label_time_busca.pack(anchor='center', pady=2, padx=2)

        # _+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+
        """# Busca Geral"""
        self.var_lista_busca = tk.StringVar()
        self.label_frame_lista_busca = LabelFrame(self.label_frame_geral, text='Resultado da BUSCA')
        self.label_frame_lista_busca.pack(anchor='center', fill='both', pady=2, padx=2)

        """# BARRA ROLAGEM CONFIGURAÇÃO"""
        self.barra_rolagem_lista_busca_Y = Scrollbar(self.label_frame_lista_busca, orient=tk.VERTICAL)
        self.barra_rolagem_lista_busca_Y.pack(side='right', fill=tk.Y)
        self.barra_rolagem_lista_busca_X = Scrollbar(self.label_frame_lista_busca, orient=tk.HORIZONTAL)
        self.barra_rolagem_lista_busca_X.pack(side='bottom', fill=tk.X)

        """# LISTA DO RESULTADO DA BUSCA"""
        self.lista_result_busca = tk.Listbox(self.label_frame_lista_busca, listvariable=self.var_lista_busca.get())
        self.lista_result_busca.config(height=8)
        self.lista_result_busca.config(selectmode=tk.SINGLE)
        self.lista_result_busca.pack(anchor='center', fill=tk.BOTH, padx=2, pady=2)

        """# BARRA ROLAGEM APLICAÇÃO"""
        self.barra_rolagem_lista_busca_Y.config(command=self.lista_result_busca.yview)
        self.lista_result_busca.config(yscrollcommand=self.barra_rolagem_lista_busca_Y.set)
        self.barra_rolagem_lista_busca_X.config(command=self.lista_result_busca.xview)
        self.lista_result_busca.config(xscrollcommand=self.barra_rolagem_lista_busca_X.set)

        # _+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+
        """#### Barra de progresso da busca"""
        self.label_frame_progresso = LabelFrame(self.label_frame_geral, text='Progresso da busca...!')
        self.label_frame_progresso.pack(anchor='s', fill='both', pady=2, padx=2)
        self.barra_progresso_busca = Progressbar(self.label_frame_progresso)
        self.barra_progresso_busca.config(orient=tk.HORIZONTAL)
        self.barra_progresso_busca.config(mode='determinate')
        self.barra_progresso_busca.config(style='red.Horizontal.TProgressbar')
        self.barra_progresso_busca.pack(anchor='s', fill='both', pady=2, padx=2)

        # _+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+
        """#### BOTÕES"""
        self.label_frame_botoes_opcoes = LabelFrame(self.label_frame_geral, text='Escolha um opção')
        self.label_frame_botoes_opcoes.pack(side='bottom', fill='both', pady=2, padx=2)

        """# BOTÃO Iniciar Busca"""
        self.botao_iniciar_busca = Button(self.label_frame_botoes_opcoes, text='Iniciar Busca')
        self.botao_iniciar_busca.config(width=30)
        self.botao_iniciar_busca.config(command=self.thread_botao_iniciar)
        self.botao_iniciar_busca.pack(anchor='center', pady=2, padx=2)

        """# BOTÃO Selecionar extensão"""
        self.botao_escolha_extensao = Button(self.label_frame_botoes_opcoes, text='Selecione/Digite uma extensão')
        self.botao_escolha_extensao.config(width=30)
        self.botao_escolha_extensao.config(command=self.thread_botao_extensao)
        self.botao_escolha_extensao.place(y=1)

        """# BOTÃO Adicionar extensão"""
        self.botao_adicionar_extensao = Button(self.label_frame_botoes_opcoes, text='Adicionar Extensões')
        self.botao_adicionar_extensao.config(width=30)
        self.botao_adicionar_extensao.config(state=tk.DISABLED)
        self.botao_adicionar_extensao.config(command=self.janela_add_ext_arq_txt)
        self.botao_adicionar_extensao.place(y=50)
        self.botao_adicionar_extensao.pack(anchor='w')

        """# BOTÃO DESTINO DA BUSCA"""
        self.botao_destino_busca = Button(self.label_frame_botoes_opcoes, text='Selecionar Pasta para Busca')
        self.botao_destino_busca.config(width=30)
        self.botao_destino_busca.config(command=self.thread_selecionar_destino_busca)
        self.botao_destino_busca.place(y=1, x=785)

        # _+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+
        """#### Radio Botão"""
        self.label_frame_radio = LabelFrame(self.label_frame_geral, text='Selecione uma opção para Salvar da busca')
        self.label_frame_radio.pack(fill=tk.BOTH, side='top')
        self.var_radio = tk.StringVar()

        """# Botão radio valor TXT"""
        self.radio_txt = Radiobutton(self.label_frame_radio, text="TXT", value='TXT', variable=self.var_radio)
        self.radio_txt.config(state=tk.DISABLED)
        self.radio_txt.pack(anchor='center')

        """# Botão radio valor PDF"""
        self.radio_pdf = Radiobutton(self.label_frame_radio, text='PDF', value='PDF', variable=self.var_radio)
        self.radio_pdf.config(state=tk.DISABLED)
        self.radio_pdf.pack(anchor='center')

        """# Radio Grafico Pizza"""
        self.radio_pizza = Radiobutton(self.label_frame_radio, text='Grafico Pizza', value='PIZZA',
                                       variable=self.var_radio)
        self.radio_pizza.config(state=tk.DISABLED)
        self.radio_pizza.place(y=1, x=360)

        """# Radio Grafico Barras"""
        self.radio_barras = Radiobutton(self.label_frame_radio, text='Grafico Barras', value='BARRAS',
                                        variable=self.var_radio)
        self.radio_barras.config(state=tk.DISABLED)
        self.radio_barras.place(y=20, x=360)

        '''# BOTÃO SAVE BUSCA'''
        self.botao_save_busca = Button(self.label_frame_radio, text='Salvar Busca')
        self.botao_save_busca.config(width=30)
        self.botao_save_busca.config(state=tk.DISABLED)
        self.botao_save_busca.config(command=self.opcao_radio)
        self.botao_save_busca.place(y=1, x=785)

        # _+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+
        """#### Separador"""
        separador_linha = Separator(self.janela_principal, orient=tk.HORIZONTAL)
        separador_linha.place(relx=600, rely=0.47, relwidth=1, relheight=1)

        # _+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+
        """#### LABEM FRAME INFO BUSCA"""
        self.label_frame_geral_info = LabelFrame(self.janela_principal, text='Informações da busca...!')
        self.label_frame_geral_info.config(relief=tk.RIDGE)
        self.label_frame_geral_info.pack(anchor='center', fill='both', pady=2, padx=2)

        """# LABEL STATUS GERAL"""
        self.var_label_status_geral = tk.StringVar()
        self.var_label_status_geral.set('Bem vindo!')
        self.label_status = Label(self.janela_principal, text=self.var_label_status_geral.get())
        self.label_status.config(justify='center')
        self.label_status.place(y=600, x=10)

        """# LABEL CONTAGEM ARQUIVOS"""
        self.var_status_contagem_arquivos = tk.StringVar()
        self.var_status_contagem_arquivos.set('Total de arquivos encontrados')
        self.status_contagem_arquivos = Label(self.janela_principal)
        self.status_contagem_arquivos.config(text=self.var_status_contagem_arquivos.get())
        self.status_contagem_arquivos.config(justify='center')
        self.status_contagem_arquivos.place(y=620, x=10)

        """# LABEL PASTAS DISTINO DA BUSCA"""
        self.var_status_contagem_pastas = tk.StringVar()
        self.var_status_contagem_pastas.set('Buscando na pasta => Aguardando busca!')
        self.status_DISTINO_pastas = Label(self.janela_principal)
        self.status_DISTINO_pastas.config(text=self.var_status_contagem_pastas.get())
        self.status_DISTINO_pastas.config(justify='center')
        self.status_DISTINO_pastas.pack(anchor='s', pady=2, padx=2)
        self.status_DISTINO_pastas.place(y=640, x=10)

        """# LABEL ARQUIVOS ENCONTRADOS"""
        self.var_msg_tot_busca = tk.StringVar()
        self.var_msg_tot_busca.set('Aguardando pela busca de arquivos')
        self.status_arquivos = Label(self.janela_principal, text=self.var_msg_tot_busca.get())
        self.status_arquivos.config(justify='center')
        self.status_arquivos.pack(anchor='n', pady=2, padx=2)
        self.status_arquivos.place(y=660, x=10)

        """# Label pasta RAIZ"""
        self.var_pasta_raiz = tk.StringVar()
        self.var_pasta_raiz.set('Escolha um pasta para realizar a busca!')
        self.status_pasta_raiz = Label(self.janela_principal, text=self.var_pasta_raiz.get())
        self.status_pasta_raiz.config(justify='center')
        self.status_pasta_raiz.pack(anchor='center', pady=2, padx=2)
        self.status_pasta_raiz.place(y=680, x=10)

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

        """# Caixa de entrada"""
        label_frame_add_ext_geral = tk.LabelFrame(janela_add_extensao, text='Janele para adicionar extensão')
        label_frame_add_ext_geral.pack(anchor='center', fill='both', pady=5, padx=5)
        self.var_caixa_entrada_ext = tk.StringVar
        label_frame_caixa_entrada = tk.LabelFrame(label_frame_add_ext_geral, text='Digite uma extensão no campo abaixo')
        label_frame_caixa_entrada.pack(side='top', fill='both', pady=5, padx=5)
        self.caixa_entrada_extensao = tk.Entry(label_frame_caixa_entrada, justify='center')
        self.caixa_entrada_extensao['textvariable'] = self.var_caixa_entrada_ext
        self.caixa_entrada_extensao.pack(anchor='center', fill='both', pady=5, padx=5)

        """# Botões"""
        label_frame_botao_add_ext = tk.LabelFrame(label_frame_add_ext_geral, text='Escolha uma opção')
        label_frame_botao_add_ext.pack(anchor='center', fill='both', pady=5, padx=5)

        """# Botão ADICIONAR A EXTENSÃO"""
        botao_adicionar_ext = tk.Button(label_frame_botao_add_ext, text='Adicionar', width=20, height=1)
        botao_adicionar_ext['command'] = self.thread_adicionar_extensao
        botao_adicionar_ext.pack(anchor='center', pady=5, padx=5)

        """# botão responsavel em corrigir eventual ERROS. Apaga a caixa de texto"""
        botao_corrigir_caixa_entrada = tk.Button(label_frame_botao_add_ext, text='Corrigir Entrada', width=20)
        botao_corrigir_caixa_entrada.pack(side='left', pady=5, padx=5)

        """# Botão VOLTAR A JANELA PRINCIPAL"""
        botao_voltar_janela_principal = tk.Button(label_frame_botao_add_ext, text='Janela Principal', width=20)
        botao_voltar_janela_principal['command'] = janela_add_extensao.destroy
        botao_voltar_janela_principal.pack(side='right', pady=5, padx=5)

        """# informações"""
        label_frame_info_add = tk.LabelFrame(label_frame_add_ext_geral, text='Foi adicionado a extensão')
        label_frame_info_add.pack(side='bottom', pady=5, padx=5)
        self.var_label_info_add_extensao = tk.StringVar()
        self.label_info_add_extensao = tk.Label(label_frame_info_add, text=self.var_label_info_add_extensao.get())
        self.label_info_add_extensao.pack(anchor='center', pady=5, padx=5)

    """# Funções simples"""
    def hora_certa(self):
        valor_datatime = datetime.now()
        self.data_atual = valor_datatime.strftime('%d/%m/%Y')
        self.hora_atual = valor_datatime.strftime('%H:%M')

    def linha_aparencia(self):
        self.lista_result_busca.insert('end', '-=-' * 52)
        print('-=-' * 48)

    def tipos_extensoes(self):
        tipos_de_extensoes = dict(
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

    # _+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+
    """# INICIANDO AS THREADS"""
    def thread_botao_iniciar(self):
        print('Iniciando THREAD [INICIAR BUSCA]')
        self.ativo_inicio_busca = True
        PlaySound(som_botao, SND_ASYNC)
        print(f'Iniciando a busca principal do programa')
        sleep(1)
        if self.ativo_status_extensao:
            Thread(target=self.iniciar_busca).start()
        else:
            showerror('AVISO!', 'Voce não escolheu nenhuma extensão')

    def thread_botao_extensao(self):
        PlaySound(som_botao, SND_ASYNC)
        print('Iniciando THREAD [BUSCA ESPECIFICA POR EXTENSAO]')
        sleep(1)
        Thread(target=self.digitar_extensao()).start()

    def thread_adicionar_extensao(self):
        PlaySound(som_botao, SND_ASYNC)
        print('Iniciando THREAD [ADICIONAR EXTENSAO]')
        sleep(1)
        Thread(self.adicionado_extensao_arq_txt()).start()

    def thread_selecionar_destino_busca(self):
        PlaySound(som_botao, SND_ASYNC)
        print(f'Iniciando thread para seleção do destino que sera realizado a busca')
        sleep(1)
        Thread(target=self.pasta_destino_busca()).start()

    def thread_time_busca(self):
        print('Iniciando THREAD de time')
        sleep(1)
        Thread(target=self.time_busca()).start()

    """# Thread para opção de salvamento"""
    def thread_opcao_save_txt(self):
        print(f'Iniciando opcao para save em Texto')
        sleep(1)
        Thread(target=self.save_TXT()).start()

    def thread_opcao_save_PDF(self):
        print(f'Iniciando opcao para save em PDF')
        sleep(1)
        Thread(target=self.save_PDF()).start()

    def thread_opcao_save_PIZZA(self):
        print(f'Iniciando thread para save grafico em pizza')
        sleep(1)
        Thread(target=self.save_opcao_PIZZA()).start()

    def thread_opcao_save_BARRAS(self):
        print(f'Iniciando thread para save grafico em barras')
        sleep(1)
        Thread(target=self.save_opcao_BARRAS()).start()

    def thread_hora_certa(self):
        print('\nIniciando função "hora_certa"\n')
        Thread(target=self.hora_certa()).start()

    # _+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+
    # INICIO DAS FUNÇÕES DE BUSCA
    def time_busca(self):
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
                self.tempo_da_busca = msg_info_time
                contagem_segundos += 1
                sleep(1)

    def combo_categoria_busca(self, *args):
        """
        Função responsavel em deixar ativo cada categoria selecionada
        :param args:
        :return: Quando selecionar uma categoria, é carregada na lista de extensão, mostrando as extesões que
        foram adicionar. Caso não tenha, na função que carrega os arquivos vai mostrar o erro.
        """
        self.lista_de_extensoes.delete('0', 'end')

        arq_imagem = '\\extensao_imagem.log'
        arq_videos = '\\extensao_videos.log'
        arq_textos = '\\extensao_textos.log'
        arq_execul = '\\extensao_execul.log'
        arq_arqzip = '\\extensao_arqzip.log'

        valor_categoria_busca = self.var_combo_categoria.get()
        print(f'\nProcessando função combo_categoria_busca [{valor_categoria_busca}]')
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
        """
        Funções é responsavel em adicionar as extensões quando são adicionadas no sistema.
        :return: Salva os dados no bloco de notas, referente ao nome
        """
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
        """
        # Função responsavel em carregaras extensões que estão salvas nos arquivos de texto
        :return: Quando é escolhida a extensão, o arquivo é aberto sendo realizado a leitura das exentesões
        que estão salvas
        """

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
        """
        # Função responsavel em selecionar a pasta de busca
        :return: Quando digita uma extensão, vai ser enviado os dados para a função "iniciar_busca"
        """
        self.pasta_local_de_busca = tk.filedialog.askdirectory()
        self.ativo_status_destinos = True
        self.status_pasta_raiz.config(text=f'Destino da busca: [{self.pasta_local_de_busca}]')

    def iniciar_busca(self):
        """
        :param: contador_arquivos = 1 = Reponsavel pela contagem todos dos arquivos encontrados.
        :param: self.lista_busca_arquivos = list() = fica alocado os valores da busca.
        :param: self.lista_save_busca = list() = fica alocado as informações para salver em arquivo de texto.
        :return: Retorna varios valores, em várias funções. Seguindo mais abaixo, existemm explicações em cada evento
        """
        if self.ativo_inicio_busca:
            """# MODULOS RESPONSAVEL PELA BUSCA"""
            from os import walk, path
            from re import search

            """# LIMPEZA DA LISTA DE BUSCA"""
            del self.lista_analise_arq_busca[:]

            if len(self.extensao_selecao_busca) == 0:
                print('Não foi selecionado nenhuma extensão. Buscando por qualquer arquivo')
            else:
                print(f'\nExtensão selecionado para busca [{self.extensao_selecao_busca}]')
            sleep(1)

            """# DECLARAÇÃO DE VARIAVEIS"""
            contador_arquivos = 1
            contador_de_raiz = 1

            """# Lista responsavel para receber os dados; vai ser levado para suas respectivas funç"""
            self.lista_busca_arquivos = list()
            self.lista_save_busca = list()

            """# Desativando os botões para o processo da busca
            A desativaç~çao é feita para evitar erros. Como o processo estão sendo realizado, clicar mais uma vezes em 
            iniciar, pode ocorre erros. Achei que desativando acaba deixando mais simples essa questao"""
            self.label_status.config(text='Desativando os botões')
            sleep(1)
            self.botao_iniciar_busca.config(state=tk.DISABLED)
            self.botao_save_busca['state'] = 'disabled'
            self.botao_destino_busca['state'] = 'disabled'
            self.botao_adicionar_extensao['state'] = 'disabled'
            self.botao_escolha_extensao['state'] = 'disabled'

            """# Os botões de Radio são desativas por padrão, sendo ativados apenas quando as buscas são finalizadas.
            Quando refaz a busca é preciso desativar para que não ocorra erros desnecessarios"""
            self.radio_txt.config(state=tk.DISABLED)
            self.radio_pdf.config(state=tk.DISABLED)
            self.radio_pizza.config(state=tk.DISABLED)
            self.radio_barras.config(state=tk.DISABLED)

            """# LIMPANDO LISTA DE BUSCA
            Função se aplica quando realiza a próxima listagem.
            Não deixo a lista com os arquivos pois na segunda listagem é acrescentando."""
            self.lista_result_busca.delete('0', 'end')

            """# Verifica se foi selecionado uma pasta, caso não tenha sido, a busca vai ficar na pasta home do usuário"""
            if self.ativo_status_destinos:
                valor_path_busca = Path(self.pasta_local_de_busca)
            else:
                valor_path_busca = Path(valor_pasta_destino)

            """# HORARIO DA BUSCAR
            Acrescendo a lista, a data e horario que a busca foi realizada"""
            self.thread_hora_certa()
            self.lista_result_busca.insert('end', f'[{self.data_atual}-{self.hora_atual}]')
            self.lista_result_busca.insert('end', self.linha_aparencia())

            """# INICIANDO O Contador"""
            self.ativo_time_busca = True
            Thread(target=self.time_busca).start()

            """# INICIANDO BARRA DE PROGRESSO"""
            PlaySound(som_inicio_busca, SND_ASYNC)
            sleep(2)
            self.barra_progresso_busca.start()

            """# INICIO DO PROCESSO DA BUSCA"""
            self.label_status.config(text='Realizando a busca de arquivos, aguarde...!')
            for raiz, subs, itens in walk(str(valor_path_busca)):

                """# O contador de raiz, vai servir para que a segunda pasta seja ativada e apareça para o usuário ver. 
                Como a pasta de buscar aparece antes de ser verificado os arquivos, é preciso de alguma forma mostrar
                """
                if contador_de_raiz == 2 and not self.ativo_true_busca:
                    self.ativo_true_busca = True

                """# Analise se o valor é verdadeiro, mostra a pasta que sera realizado a busca. Por padrão
                O primeiro valor é sempre 'verdadeiro', porém os demais vão variar conforme a busca."""
                if self.ativo_true_busca:
                    """# Listas reponsável em organizar o documento"""
                    self.lista_save_busca.append('')
                    self.lista_save_busca.append('')
                    self.lista_save_busca.append(f'>>>>>>>{raiz.upper()}<<<<<<<')
                    self.lista_save_busca.append(f'{"===" * 20}')

                    """# Os dados são insedireto para que seja analisado pela função de analise."""
                    self.lista_busca_arquivos.append(f'\n\n{raiz}\n{"===" * 20}')

                    """# Os dados são inseridos dentro da lista, para que possoa aparecer na janela de busca"""
                    self.lista_result_busca.insert('end', '')
                    self.lista_result_busca.insert('end', f'>>>>>>>{raiz.upper()}<<<<<<<')
                    self.lista_result_busca.insert('end', self.linha_aparencia())

                """# Indica ao usuário qual a pasta de busca."""
                self.status_DISTINO_pastas.config(text=f'Buscando na pasta => [{raiz}]')

                contador_de_raiz += 1

                """# Realiza um 'loop' do arquivos dentro das pastas. Porem o valor só vai aparece depois que passa
                pela '#Verificação de extensão#' """
                for valor_itens in itens:

                    """# Realiza a junção da pasta com o item encontrado. Logo abaixo ser realizado a monipulação
                    para que fique mais fácil a idenficação na hora de visualizar"""
                    caminho_files = path.join(raiz, valor_itens)

                    """# Separa alguns informações da busca. Deixando em destaque o arquivo, com letras maiusculas 
                    e as pasta em minusculos."""
                    valor_arquivo = caminho_files.split('\\')[-1]
                    destaque_arquivos_pasta = f'{raiz.lower()}\\ [>> {valor_arquivo.upper()} <<]'

                    """# Esse é o processo responsável em buscar os arquivos conforme a solicitação do usuário. 
                    Quando é solecionado uma extensão, ele busca e imprime na tela e na lista de busca"""
                    if search(self.extensao_selecao_busca.lower(), valor_itens):  # #Verificação de extensão#

                        """# Indica que a extensões foi encontrada"""
                        self.ativo_true_busca = True

                        """# Mostra o valor que esta sendo encontrado."""
                        self.status_arquivos.config(text=valor_itens)

                        """# Coloca as informações dentro da lista de busca, para mostra na janela """
                        self.lista_result_busca.insert('end', f'{destaque_arquivos_pasta}')

                        """# Os arquivos são colocados dentro da lista para serem analisados na proxima função"""
                        self.lista_analise_arq_busca.append(f'{destaque_arquivos_pasta}')

                        """# As informações são geralmente inseridas de forma para facilitar o salvamento no arquivo"""
                        self.lista_save_busca.append(f'{destaque_arquivos_pasta}')

                        """# Mostra na janela, a quantidade de arquivos encontrados no total"""
                        self.status_contagem_arquivos.config(text=f'Arquivos encontrados: [{contador_arquivos}]')
                        contador_arquivos += 1
                    else:
                        """# Quando não encontra a extensão, muda o valor para falso."""
                        self.ativo_true_busca = False

            """# Listas reponsável em organizar o documento"""
            self.lista_result_busca.insert('end', '')
            self.lista_result_busca.insert('end', 'Busca finalizada!!')
            self.label_status.config(text='Busca finalizada... \nAguarde... \nAtivando botoes')

            """# Finalizando TIME BUSCA"""
            self.ativo_time_busca = False

            """# FINALIZNANDO BARRA PROGRESSO"""
            self.barra_progresso_busca.stop()
            self.barra_progresso_busca.config(value=100)

            """# Abrindo função de analise de dados"""
            self.analise_e_processo_de_dados_da_busca()

            """# Emitindo som de finalização; O som ajuda o usuário quando a busca finaliza. Existem algumas buscas
            que podem levar um certo tempo, com um sinalizado sonoro pode ajuda-lo em voltar ao programa, caos tenho 
            deixando rodando em segundo plano"""
            PlaySound('Som WINDOWS', SND_ASYNC)

            """# REATIVANDO BOTÕES/Radios"""
            self.botao_iniciar_busca['state'] = 'normal'
            self.botao_save_busca['state'] = 'normal'
            self.botao_destino_busca['state'] = 'normal'
            self.botao_escolha_extensao['state'] = 'normal'

            self.radio_txt.config(state=tk.NORMAL)
            self.radio_pdf.config(state=tk.NORMAL)
            self.radio_pizza.config(state=tk.NORMAL)
            self.radio_barras.config(state=tk.NORMAL)

            self.label_status.config(text='Processo de busca finalizado')
        else:
            showwarning('ATENÇAO', 'Sua busca foi cancelada')

    def analise_e_processo_de_dados_da_busca(self):
        """
        # Declarações de variaveis:
        :param contagem_extensao: responsável em contar a quantidade de extensão que esão encontradas
        :param contagem_pastas: mostra a quantidade de arquivos em cada pasta
        :param lista_qtd_arq_pastas: insere as informações para serem enviados para criação do PDF
        :param lista_qtd_extensao: insere as informações para serem enviados para criação do PDF
        :param qts_extensao_grafico: insere as informações para serem enviados para criação do grafico
        :param lista_qtd_extensao: Lista que vai entrar dos dados de extensão.
        """
        self.contagem_demais_extensoes = {}
        self.contagem_extensao = {}
        self.contagem_pastas = {}
        self.lista_qtd_arq_pastas = []
        self.qts_extensao_grafico = []
        self.lista_qtd_extensao = []

        self.label_status.config(text='Aguarde!! Analisando os dados de busca')

        """# Pega o  Bruto da lista de mostra no console para analise do usuário"""
        print(f'Analise RAIZ\n{self.lista_analise_arq_busca}')

        """#### Realiza a analise dos valores da busca."""
        for valor_lista_busca in self.lista_analise_arq_busca:

            """# Na linha abaixo, realiza a separação da extensão com o restante do valor, que seria o caminha até
            a última pasta, que esta sendo realizado a busca. Nesse caso, como descrito mais abaixo, o valor segue 
            com o simbolo ']' onde é removido"""
            divisao_valor_extensao = str(valor_lista_busca).split('.')

            """# Na linha abaixo, separa os valores da pasta, transformando em uma lista"""
            divisao_valor_pastas = str(valor_lista_busca).split('\\')

            """# O valor da extensão chega com o simbolo ']' devido a formatação, mas é removido na linha abaixo"""
            valor_extensao = (str(divisao_valor_extensao[-1]).lower().strip().replace(']', '').
                              replace('<<', '')).replace(' ', '')

            """# Na linha abaixo é separa apenas a pasta que está sendo analisada. """
            valor_pasta = str(divisao_valor_pastas[-2]).strip()

            """# Caso a pasta não esteja no dicionário, é adicionado uma chave com o nome do valor, somando a quantidade
            de arquivos dentro de cada pasta"""
            if valor_pasta in self.contagem_pastas:
                self.contagem_pastas[valor_pasta] += 1
            else:
                self.contagem_pastas[valor_pasta] = 1

            """# Ocorre o mesmo problema com as extensões. Nessa caso ele somas a quantidade de extensão que foi 
            encontrado no total."""
            if 4 >= len(valor_extensao) >= 3:
                if valor_extensao in self.contagem_extensao:
                    self.contagem_extensao[valor_extensao] += 1
                else:
                    self.contagem_extensao[valor_extensao] = 1

        """#### QUANTIDADE DE EXTENSAO QUE POSSUI"""
        self.lista_result_busca.insert('end', '')
        self.lista_result_busca.insert('end', '-=-' * 20)
        self.lista_result_busca.insert('end', 'Total de extenões encontrados...')
        self.lista_result_busca.insert('end', '')
        self.lista_result_busca.insert('end', 'Extensão      -      Quantidade')

        print()
        print('Total de extenões encontrados...')
        print('-=-' * 22)
        print('Extensão      -      Quantidade')

        """# Adiciona na lista de busca a quantidade de extensões que foram encontradas no processo de busca."""
        for extensao, quantidade in self.contagem_extensao.items():
            valor_extensao_qtd = f' [ {extensao.upper():6} ] {"-":-^20} [{quantidade}]'
            self.qts_extensao_grafico.append(f'{extensao}={quantidade}')
            self.lista_qtd_extensao.append(valor_extensao_qtd)
            self.lista_result_busca.insert('end', f'[ {extensao.upper():6}] {"-":-^20} [{quantidade}]')

            """# Mostra o valor, dentro do console,  das quantidade de extensão encontradas"""
            print(f'{valor_extensao_qtd}')

        for chave, valor in self.contagem_demais_extensoes.items():
            print(f'{chave, valor}')

        self.lista_result_busca.insert('end', '-=-' * 20)
        self.lista_result_busca.insert('end', '')

        print(f'Analisando \n{self.qts_extensao_grafico}')

        """#### Quantidade de arquivos dentro das pastas """
        print()
        print('Total de arquivos encontrados...')
        print('-=-' * 20)

        self.lista_result_busca.insert('end', '')
        self.lista_result_busca.insert('end', 'Total de arquivos...')
        self.lista_result_busca.insert('end', '-=-' * 20)

        """# Adiciona na lista de busca, os contagem dos itens encontrados nas pastas"""
        for pastas, quantidade in self.contagem_pastas.items():
            qtd_arq_pastas = f'\\{pastas.upper():50} {"-":-^20} {quantidade}'
            self.lista_qtd_arq_pastas.append(qtd_arq_pastas)
            self.lista_result_busca.insert('end', f'\\{pastas.upper():100} {"-":-^20} {quantidade}')

            """# Mostra na tela do console a quantidade de arquivos dentro das pastas"""
            print(f'{qtd_arq_pastas}')

        print(f'\nFinalizado busca!\n Salve o resultado ou pode analisar pela lista acima!\n')
        self.lista_result_busca.insert('end', '')
        self.lista_result_busca.insert('end', '')
        self.lista_result_busca.insert('end', 'Analise finalizada!!')
        self.label_status.config(text='Analise finalizada!!')

    def opcao_radio(self):
        valor_opcao_radio = self.var_radio.get()
        if valor_opcao_radio == 'TXT':
            self.thread_opcao_save_txt()
        elif valor_opcao_radio == 'PDF':
            self.thread_opcao_save_PDF()
        elif valor_opcao_radio == "PIZZA":
            self.thread_opcao_save_PIZZA()
        elif valor_opcao_radio == 'BARRAS':
            self.thread_opcao_save_BARRAS()

    def save_PDF(self):
        """
        Essa função é responsável por criar um documento em PDF. Eu criei um módulo (para praticar) e todas as
        informações da busca é levada para o módulo PDF.
        :return:
        """
        self.label_status.config(text='Criando seu documento PDF, aguarde!')
        valor_nome_PDF = askstring('AVISO!', 'Dê um nome ao arquivo PDF')
        nome_PDF = f'{valor_nome_PDF}-{self.data_atual.replace("/", "")}-{self.hora_atual.replace(":", "")}'
        sleep(1)
        Thread(target=documento_PDF(self.lista_save_busca, nome_PDF, self.lista_qtd_extensao,
                                    self.lista_qtd_arq_pastas)).start()
        print('Documento criado com sucesso!')
        self.label_status.config(text='Documento criado com sucesso!')
        sleep(1)
        self.label_status.config(text='Fim da busca!')

    def save_TXT(self):
        """

        :return:
        """
        print(f'Processando função SAVE')
        tipo_de_arquivo = [('Texto(.txt)', '*.txt')]
        arquivo_save = asksaveasfile(filetypes=tipo_de_arquivo, defaultextension=tipo_de_arquivo)
        try:
            self.label_status.config(text='Aguarda, salvando os dados em arquivo de texto!!')

            """# Cabeçalho do salvamento"""
            arquivo_save.write(f'Data {self.data_atual} - Hora {self.hora_atual}\n')
            arquivo_save.write(f'{"===" * 10}\n')
            arquivo_save.write(f'Tempo da busca {self.tempo_da_busca}\n\n')

            arquivo_save.write(f'Pasta da busca\n')
            arquivo_save.write(f'{"===" * 10}\n')
            arquivo_save.write(f'[{self.pasta_local_de_busca}]\n')

            """Arquivos da busca"""
            arquivo_save.write(f'\n\n')
            arquivo_save.write(f'Dados da busca\n')
            arquivo_save.write(f'{"===" * 10}\n')
            for valor_busca in self.lista_save_busca:
                arquivo_save.write(f'{valor_busca}\n')
            arquivo_save.write('\n\n')
            arquivo_save.write(f"{'@@@' * 10}\n")

            """Quantidade da extensão"""
            arquivo_save.write('\n\n')
            arquivo_save.write(f'Extensão      -      Quantidade\n')
            for valor_dicionario_qtd_ext in self.lista_qtd_extensao:
                arquivo_save.write(f'{valor_dicionario_qtd_ext}\n')

            """Quantidade de arquivos dentro de cada pasta"""
            arquivo_save.write('\n\n')
            arquivo_save.write('Quantidades de arquivo dentro de cada pasta\n')
            arquivo_save.write(f"{'______' * 10}\n")
            for valor_lista_qtd_arq_pasta in self.lista_qtd_arq_pastas:
                arquivo_save.write(f'{valor_lista_qtd_arq_pasta}\n')
            arquivo_save.write('\n\n')
            arquivo_save.close()
            tk.messagebox.showinfo('AVISO', 'Sua busca foi salva com sucesso')
            self.label_status.config(text='Arquivo salvo com sucesso!')
        except:
            tk.messagebox.showwarning('AVISO', 'Busca não pode ser salva no sistema!')

    def save_opcao_PIZZA(self):
        print(f'Direcionando dados para função de criação do grafico de PIZZA')
        sleep(1)
        grafico_pizza(self.qts_extensao_grafico)

    def save_opcao_BARRAS(self):
        print(f'Direcionando dados para função de criação do grafico em BARRAS')
        sleep(1)
        grafico_barras(self.qts_extensao_grafico)


obj_start = ListandoArquivos()
