import tkinter as tk
from tkinter.ttk import *
from pathlib import Path
from datetime import datetime
from tkinter.simpledialog import askstring
from tkinter.filedialog import askdirectory, asksaveasfile
from tkinter.messagebox import showinfo

valor_hora = datetime.now()
data_certa = valor_hora.strftime('%d/%m%Y')
hora_certa = valor_hora.strftime('%H:%M')


class ListagemPastas:
    def __init__(self):

        # Variaveis Global
        self.pasta_home = Path.home()
        self.pastas_arquivos_extensao = Path(self.pasta_home, 'AppData', 'LocalLow', 'extensoes')
        self.lista_salves_busca = list()

        # Variaveis de confirmação
        self.lista_ativa_imagem = False
        self.lista_ativa_videos = False
        self.lista_ativa_textos = False
        self.lista_ativa_execus = False
        self.lista_ativa_compre = False
        self.lista_ativa_especi = False

        self.lista_tipos_extensoes = ('Todos', 'Arquivos de Vídeo', 'Arquivo Imagem', 'Arquivos de Leitura',
                                      'Arquivos execução', 'Arquivos compreesão')
        self.extensoes_imagem = (
            'JPG', 'PNG', 'GIF', 'BMP', 'Bitmap', 'TIFF', 'RAW', 'EXIF', 'PPM', 'PGM', 'PBM', 'PNM',
            'SVG', 'WebP',)
        self.extensoes_videos = ('MP4', 'AVI', 'MKV', 'MOV', 'WMV', 'FLV', 'AVCHD', 'F4V', 'SWF', 'WEBM', 'HTML5',
                                 'WEBM')
        self.extensoes_arq_txt = (
            'TXT', 'PDF', 'DOCX', 'DOC', 'HTML', 'HTM', 'ODT', 'XLS', 'XLSX', 'ODS', 'PPT', 'PPTX')
        self.extensoes_de_app = ('EXE', 'DLL', 'IN', 'BAT')
        self.extensoes_compreensao = ('ZIP', '')

        # Janela principa
        self.janela_principal = tk.Tk()
        self.janela_principal.geometry('300x380')
        self.janela_principal.title('V_007')
        self.janela_principal.resizable(False, False)
        self.janela_principal.config(border=3, bg='#A9A9A9')

        # Label Frame

        self.frame_hora = Frame(self.janela_principal)
        self.frame_hora.pack(anchor='n')
        self.label_data_hora = Label(self.frame_hora, text=f'{data_certa} - {hora_certa}')
        self.label_data_hora.pack()

        self.label_frame_001 = LabelFrame(self.janela_principal, border=2, text='Iniciando o programa')
        self.label_frame_001.pack(anchor='n', fill='both')

        self.label_frame_002 = Frame(self.janela_principal)
        self.label_frame_002.pack(anchor='center', fill='both')

        self.label_frame_003 = LabelFrame(self.janela_principal, text='Escolha uma opção!')
        self.label_frame_003.pack(fill=tk.BOTH)

        self.label_frame_004 = Frame(self.janela_principal)
        self.label_frame_004.pack()

        self.frame_hora = Frame(self.janela_principal)
        self.frame_hora.pack(anchor='n')

        # Lista Combo principal
        self.var_combo = tk.StringVar()
        self.combo_tipo_arquivo_principal = Combobox(self.label_frame_001, textvariable=self.var_combo,
                                                     justify='center')
        self.combo_tipo_arquivo_principal['values'] = self.lista_tipos_extensoes
        self.combo_tipo_arquivo_principal.set('Escolha uma categoria de arquivo')
        self.combo_tipo_arquivo_principal.pack(side='top', fill='both', ipady=3, ipadx=3)
        self.combo_tipo_arquivo_principal.current()
        self.var_combo.trace('w', self.tipos_extensao)

        # Barra ralagem
        self.rolagem_principal_vertical = tk.Scrollbar(self.label_frame_002, border=3, borderwidth=3)
        self.rolagem_principal_vertical.pack(side='right', fill=tk.Y)

        # Lista de exntesão
        self.lista_extensao = tk.Listbox(self.label_frame_002, justify='center', border=3, bg='#D3D3D3',
                                         relief='groove')
        self.lista_extensao.config(yscrollcommand=self.rolagem_principal_vertical.set)
        self.rolagem_principal_vertical.config(command=self.lista_extensao.yview)
        self.lista_extensao.pack(side='top', fill='both', padx=5, pady=5)

        # botões
        self.botao_iniciar_busca = tk.Button(self.label_frame_003, text='Iniciar Busca', bg='#DAA520', border=3,
                                             borderwidth=2, font=13, command=self.janela_inicio_busca)

        self.botao_iniciar_busca.pack(fill='both', padx=3, pady=3)

        self.botao_adicionar_extensao = tk.Button(self.label_frame_003, text='Buscar especifica', bg='#A9A9A9',
                                                  width=20, height=1, justify='center', border=3, borderwidth=3,
                                                  relief='groove', command=self.add_extensao)
        self.botao_adicionar_extensao.pack(anchor='s', ipadx=3, ipady=3)

        self.botao_sair_programa = tk.Button(self.label_frame_003, text='Sair do programa', width=20, height=1,
                                             relief='groove', border=3, bg='#A9A9A9',
                                             command=self.janela_principal.destroy, )
        self.botao_sair_programa.pack(anchor='s', ipady=3, ipadx=3)

        # Looping janela
        self.janela_principal.mainloop()

    def add_extensao(self):
        self.lista_ativa_especi = True
        self.janela_inicio_busca()

    def tipos_extensao(self, *args):
        """
        Essa função está sendo destinada para escolhar uma categoria de arquivos, que o programa ira buscar.
        :param args: Quando se escolhe uma categoria, o programa vai listar as extensões dessa categoria em um ListBox
        e mostrar ao usuário, quando escolha uma categoria, as várias ativas irão retornar o valor "Verdadeiro"
        :return: self.lista_ativa_imagem
        :return: self.lista_ativa_videos
        :return: self.lista_ativa_textos
        """

        valor_categoria_busca = self.var_combo.get()
        self.lista_extensao.delete('0', 'end')
        if valor_categoria_busca == 'Arquivos de Vídeo':
            for valor_lista_video in self.extensoes_videos:
                self.lista_extensao.insert('end', valor_lista_video)
            self.lista_ativa_videos = True

        elif valor_categoria_busca == 'Arquivo Imagem':
            for valor_lista_imgem in self.extensoes_imagem:
                self.lista_extensao.insert('end', valor_lista_imgem)
            self.lista_ativa_imagem = True

        elif valor_categoria_busca == 'Arquivos de Leitura':
            for valor_lista_texto in self.extensoes_arq_txt:
                self.lista_extensao.insert('end', valor_lista_texto)
            self.lista_ativa_textos = True

        elif valor_categoria_busca == 'Arquivos execução':
            for valor_lista_app in self.extensoes_de_app:
                self.lista_extensao.insert('end', valor_lista_app)
            self.lista_ativa_execus = True

        elif valor_categoria_busca == 'Arquivos compreesão':
            for valor_lista_compre in self.extensoes_compreensao:
                self.lista_extensao.insert('end', valor_lista_compre)
            self.lista_ativa_compre = True

        elif valor_categoria_busca == 'Todos':
            tk.messagebox.showinfo('AVISO IMPORTANTE', 'Para buscar por todos os arquivos, aperte o botão'
                                                       '\n">> Busca especifica <<"')
            self.lista_ativa_especi = True

    def janela_inicio_busca(self):
        self.lista_salves_busca = list()
        global valor_opc_extensao, valor_extensao_busca, contagem_arquivos
        contagem_arquivos = 0
        contagem_geral = 1

        # Processo da função
        valor_lista_extensao = self.lista_extensao.curselection()
        for valor_opc_extensao in valor_lista_extensao:
            pass

        if self.lista_ativa_imagem:
            valor_extensao_busca = self.extensoes_imagem[valor_opc_extensao]
            print(f'{valor_extensao_busca}')

        elif self.lista_ativa_videos:
            valor_extensao_busca = self.extensoes_videos[valor_opc_extensao]
            print(f'{valor_extensao_busca}')

        elif self.lista_ativa_textos:
            valor_extensao_busca = self.extensoes_arq_txt[valor_opc_extensao]
            print(f'{valor_extensao_busca}')

        elif self.lista_ativa_execus:
            valor_extensao_busca = self.extensoes_de_app[valor_opc_extensao]
            print(f'{valor_extensao_busca}')

        elif self.lista_ativa_compre:
            valor_extensao_busca = self.extensoes_compreensao[valor_opc_extensao]
            print(f'{valor_extensao_busca}')

        elif self.lista_ativa_especi:
            tk.messagebox.showinfo('AVISO', 'Basta deixar o campo em branco para realizar uma busca '
                                            'completa!')
            valor_extensao_busca = askstring('Bem vindo', 'Digite uma extenão desejada')

        # janela busca
        self.janela_busca = tk.Tk()
        self.janela_busca.grid()
        self.janela_busca.geometry('800x300')
        if len(valor_extensao_busca) != 0:
            self.janela_busca.title(f'Buscando por arquivos [{valor_extensao_busca}]')
        else:
            self.janela_busca.title('Buscando por QUAISQUER arquivo')

        # label frame busca
        self.label_frame_busca = LabelFrame(self.janela_busca, text='Resultado da busca', )
        self.label_frame_busca.pack(fill='both', ipady=5, ipadx=5)
        self.frame_busca_01 = Label(self.janela_busca)
        self.frame_busca_01.pack(anchor='s')

        # botao
        self.botao_voltar_menu = Button(self.frame_busca_01, text='Salvar', command=lambda: self.save_busca())
        self.botao_voltar_menu.pack(anchor='s')
        self.botao_busca_sair = Button(self.frame_busca_01, text='Fechar Janela', command=self.janela_busca.destroy)
        self.botao_busca_sair.pack(anchor='w')

        # Barra rolatem
        self.rolagem_busca_vert = tk.Scrollbar(self.label_frame_busca)
        self.rolagem_busca_vert.pack(side='right', fill=tk.Y)
        self.rolagem_busca_orin = tk.Scrollbar(self.label_frame_busca, orient='horizontal')
        self.rolagem_busca_orin.pack(side='bottom', fill=tk.X)

        # Lista da busca
        self.var_busca = tk.Variable()
        self.lista_da_busca = tk.Listbox(self.label_frame_busca, justify='left')
        self.lista_da_busca.config(yscrollcommand=self.rolagem_busca_vert.set)
        self.rolagem_busca_vert.config(command=self.lista_da_busca.yview)
        self.lista_da_busca.config(xscrollcommand=self.rolagem_busca_orin.set)
        self.rolagem_busca_orin.config(command=self.lista_da_busca.xview)
        self.lista_da_busca.pack(fill='both', ipadx=3, ipady=5)
        pasta_destino_busca = Path(askdirectory())
        for valor_da_busca in pasta_destino_busca.glob('**/*' + valor_extensao_busca):
            if valor_da_busca.is_file():
                self.lista_da_busca.insert('end', f'{contagem_geral}° - {valor_da_busca}')
                self.lista_salves_busca.append(f'{contagem_geral} - {valor_da_busca}')
                contagem_geral += 1
            elif valor_da_busca.is_dir():
                self.lista_da_busca.insert('end', f'{contagem_geral}° - {valor_da_busca}')
                contagem_geral += 1
        contagem_arquivos = len(self.lista_salves_busca)
        if len(self.lista_salves_busca) == 0:
            tk.messagebox.showwarning('AVISO', f'Não foi encontrado nenhum item com a extensão '
                                               f'\n[{valor_extensao_busca}]')
        else:
            if len(valor_extensao_busca) != 0:
                tk.messagebox.showinfo('AVISO!', 'Busca finalizada!'
                                                 f'\nForam encontrados {contagem_arquivos} arquivos com a '
                                                 f'extensão [{valor_extensao_busca}]')
            else:
                valor_var_ext = set()
                for valor in self.lista_salves_busca:
                    lista = str(valor).split('\\')
                    arquivos = str(lista[-1])
                    extensao = arquivos.split('.')
                    tipo_arq = extensao[-1]
                    valor_var_ext.add(tipo_arq)
                    print(valor_var_ext)

                tk.messagebox.showinfo('Finalizado!', f'\nForam encontrados {contagem_arquivos}'
                                                      f' arquivos com as extensões [{valor_var_ext}]')

    def save_busca(self):
        arquivos = [('Arquivo de texto (.txt)', '*.txt')]
        arquivo_save = asksaveasfile(filetypes=arquivos, defaultextension=arquivos)
        for leitura_dados in self.lista_salves_busca:
            arquivo_save.write(f'{leitura_dados}\n')
        arquivo_save.close()


obj_principal = ListagemPastas()
