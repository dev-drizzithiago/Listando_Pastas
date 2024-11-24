"""#### Declaração de Modulos"""
import os
import tkinter.simpledialog
from tkinter.messagebox import showwarning, showinfo, showerror
from tkinter.simpledialog import askstring, askinteger, askfloat
from tkinter.filedialog import askdirectory
from tkinter.ttk import *
import tkinter as tk
import shutil

"""#### Modulos do sistema"""
from os import walk, startfile, rename, path
from re import search

"""### Modulos básicos"""
from time import sleep
from pathlib import Path
from datetime import datetime

"""# Modulo THREAD"""
from threading import Thread


class ProgramaPrincipal:
    """__init__ fica a janela principal"""
    def __init__(self):

        """##### Declarações de variaveis"""
        tipos_categorias = ['ARQUIVOS', 'IMAGEM', 'VIDEOS', 'AUDIO', 'POWERPOINT', 'EXCEL', 'TEXTOS', 'PROGRAMACAO',
                            'ACCESS', 'WORD', 'HTML']
        tipos_categorias.sort()

        self.lista_para_renomear = list()
        self.dados_do_processo_busca = list()
        self.dados_para_duplicidade = list()
        self.tempo_gasto_da_busca = None

        # ______________________________________________________________________________________________________________
        """ Declarações para tooltip"""
        self.texto = 'Entrou com o mouse'
        self.tooltip = None
        # ______________________________________________________________________________________________________________
        """# Pasta padrão da busca; sempre tento usar a pasta do usuário"""
        self.func_pasta_destino_padrao()
        # ______________________________________________________________________________________________________________
        """#### Declaraçõas de ativações"""
        self.ativar_selecionar_pasta_destino = False
        self.ativar_arquivo_encontrado = False
        self.ativar_uma_extensao = False
        self.ativar_time_busca = False
        self.ativar_time_proce = False
        self.ativar_combo = False

        self.ativar_segundos = False
        self.ativar_minutos = False
        self.ativar_horas = False

        self.ativar_opcao_mover = False
        self.ativar_opcao_delete = False
        self.ativar_opcao_renomear = False

        # -=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
        """# Janela principal"""
        self.janela_principal = tk.Tk()
        self.janela_principal.title('V_010')
        self.janela_principal.geometry('1100x680+100+50')
        self.janela_principal.resizable(0, 0)
        self.janela_principal.wm_overrideredirect(False)
        self.janela_principal.protocol("WM_DELETE_WINDOW", self.fechar_janela)
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
        self.lbl_qtd_arquivos.config(text='Quantidade de arquivos encontrados: ', bg='#D3D3D3')
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
        self.lbl_tempo_busca.config(text='Tempo de busca: ', bg="#D3D3D3")
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
        self.lbl_ext_selec.config(text=f'Escolha uma extensão para busca: ', bg='#D3D3D3')
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
        self.frame_label_diretorio = tk.LabelFrame(self.frames_inferior, text='Pasta de busca')
        self.frame_label_diretorio.config(bg='#DCDCDC', pady=5, padx=5)
        self.frame_label_diretorio.place(y=5, x=140)
        # ______________________________________________________________________________________________________________
        """# Frame Botão de Manipular arquivos"""
        self.frame_lbl_botao_renomear = tk.LabelFrame(self.frames_inferior, text='Manipular arquivos')
        self.frame_lbl_botao_renomear.config(bg="#DCDCDC", pady=5, padx=5)
        self.frame_lbl_botao_renomear.place(y=5, x=280)
        # ______________________________________________________________________________________________________________
        """# Frame Label para botão adiconar indices nos arquivos"""
        self.frame_label_adiconar_indice = tk.LabelFrame(self.frames_inferior, text='Adiconar indices')
        self.frame_label_adiconar_indice.config(bg='#DCDCDC', pady=5, padx=5)
        self.frame_label_adiconar_indice.place(y=5, x=420)
        # ______________________________________________________________________________________________________________
        """# Frame Label para botão de limpeza da lista de extensões"""
        self.frame_label_limpeza_chk = tk.LabelFrame(self.frames_inferior, text='Limpar listas')
        self.frame_label_limpeza_chk.config(bg='#DCDCDC', pady=5, padx=5)
        self.frame_label_limpeza_chk.place(y=5, x=785)
        # ______________________________________________________________________________________________________________
        """# Frame Label para botão de encontrar duplicidade"""
        self.frame_label_duplicidade = tk.LabelFrame(self.frames_inferior, text='Analisar duplicidade')
        self.frame_label_duplicidade.config(bg='#DCDCDC', pady=5, padx=5)
        self.frame_label_duplicidade.place(y=5, x=925)
        # ______________________________________________________________________________________________________________
        """# Frame Label para botão de encontrar duplicidade"""
        self.frame_label_abrir_arquivos = tk.LabelFrame(self.frames_inferior, text='Abrir selecionado')
        self.frame_label_abrir_arquivos.config(bg='#DCDCDC', pady=5, padx=5)
        self.frame_label_abrir_arquivos.place(y=5, x=645)
        # ______________________________________________________________________________________________________________

        # ==============================================================================================================
        # ______________________________________________________________________________________________________________
        """#### BOTÕES """

        """# Botão INICIAR PROCESSO"""
        self.botao_inicio_processo = tk.Button(self.frame_label_inicio, text='Aplicar')
        self.botao_inicio_processo.config(width=15, pady=5, padx=5, bg='#00FA9A')
        self.botao_inicio_processo.config(command=lambda: Thread(target=self.botao_inicio_da_busca_principal).start())
        self.botao_inicio_processo.pack(anchor='n', fill='both')
        self.botao_inicio_processo.bind('<Enter>', self.evento_mostrar)
        self.botao_inicio_processo.bind('<Leave>', self.evento_esconder)
        # ______________________________________________________________________________________________________________
        """# Botao Pasta destino"""
        self.botao_destino_busca = tk.Button(self.frame_label_diretorio, text='Aplicar')
        self.botao_destino_busca.config(width=15, pady=5, padx=5, bg='#D3D3D3')
        self.botao_destino_busca.config(command=lambda: Thread(target=self.botao_pasta_destino).start())
        self.botao_destino_busca.pack(anchor='n', fill='both')
        # ______________________________________________________________________________________________________________
        """# Botão para renomear arquivos """
        self.botao_aplica_opcao_renomar = tk.Button(self.frame_lbl_botao_renomear, text='Aplicar')
        self.botao_aplica_opcao_renomar.config(width=15, pady=5, padx=5, bg='#D3D3D3')
        self.botao_aplica_opcao_renomar.config(command=lambda: Thread(target=self.botao_renomear_arquivos).start())
        self.botao_aplica_opcao_renomar.pack(anchor='n', fill='both')
        # ______________________________________________________________________________________________________________
        """# Botão para adicionar um indice no inicio do arquivos """
        self.botao_aplica_opcao_indice = tk.Button(self.frame_label_adiconar_indice, text='Add Indice')
        self.botao_aplica_opcao_indice.config(width=15, pady=5, padx=5, bg='#D3D3D3')
        self.botao_aplica_opcao_indice.config(command=lambda: Thread(target=self.renomear_e_adicionar_indice).start())
        self.botao_aplica_opcao_indice.pack(anchor='n', fill='both')
        # ______________________________________________________________________________________________________________
        """# Botão limpeza lista de extensão"""
        self.botao_limpar_checkbuttun = tk.Button(self.frame_label_limpeza_chk, text='Aplicar')
        self.botao_limpar_checkbuttun.config(width=15, pady=5, padx=5, bg='#D3D3D3')
        self.botao_limpar_checkbuttun.config(
            command=lambda: Thread(target=self.botao_limpeza_checkbutton_destroy).start()
        )
        self.botao_limpar_checkbuttun.pack(anchor='n', fill='both')
        # ______________________________________________________________________________________________________________
        """# Botão verificar duplicidade"""
        self.botao_duplicidade = tk.Button(self.frame_label_duplicidade, text='Aplicar')
        self.botao_duplicidade.config(width=15, pady=5, padx=5, bg='#D3D3D3')
        self.botao_duplicidade.config(command=lambda: Thread(target=self.botao_modulo_duplicidade).start())
        self.botao_duplicidade.config(state=tk.DISABLED)
        self.botao_duplicidade.pack(anchor='n', fill='both')
        # ______________________________________________________________________________________________________________
        """# Botão abrir aquivos selecionado"""
        self.botao_abrir_arquivo = tk.Button(self.frame_label_abrir_arquivos, text='Abrir um arquivo')
        self.botao_abrir_arquivo.config(width=15, pady=5, padx=5, bg='#D3D3D3')
        self.botao_abrir_arquivo.config(command=lambda: Thread(target=self.abrir_arquivos).start())
        self.botao_abrir_arquivo.config(state=tk.DISABLED)
        self.botao_abrir_arquivo.pack(anchor='center', fill='both')
        # ______________________________________________________________________________________________________________

        # ______________________________________________________________________________________________________________
        """# Frame Label Listas de buscas"""
        self.frame_label_lista_resultado = tk.LabelFrame(self.label_frame_principal, text='Resultado das buscas')
        self.frame_label_lista_resultado.config(width=983)
        self.frame_label_lista_resultado.place(y=430, x=1)
        # ______________________________________________________________________________________________________________
        """
        # Lista de busca
        Aqui você vai encontrar todas as informações da busca, conforme a extensão selecionar. 
        """
        self.var_lista_result_busca = tk.StringVar()
        self.lista_de_result_busca = tk.Listbox(self.label_frame_principal, width=87, height=7, bg='#DCDCDC')
        self.lista_de_result_busca.config(listvariable=self.var_lista_result_busca)
        self.lista_de_result_busca.config(font='Arial', justify='left', selectmode=tk.SINGLE)
        self.lista_de_result_busca.place(y=450, x=2)
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

        # -=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
        """#### Iniciando o relogio"""
        self.data_hora_certa()

        # -=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
        """###### LOOP DA JANELA ######"""
        try:
            self.janela_principal.mainloop()
        except RuntimeError:
            pass
        except KeyboardInterrupt:
            ...

    def janela_duplicidade(self):
        print('Iniciando a janela "janela_duplicidade"')
        """#### Janela de opções duplicados; só interno """
        self.janela_opc_duplicidade = tk.Toplevel()
        self.janela_opc_duplicidade.geometry('1000x620+200+20')
        self.janela_opc_duplicidade.resizable(0, 0)
        self.janela_opc_duplicidade.title('Verificando duplicidade!')

        # ______________________________________________________________________________________________________________
        """# Frame Principal DUPLICIDADE"""
        self.frame_label_duplicidade = tk.LabelFrame(self.janela_opc_duplicidade, text='Verificando duplicidade!')
        self.frame_label_duplicidade.config(width=900, height=600)
        self.frame_label_duplicidade.pack(fill=tk.BOTH, pady=5, padx=5)

        # ______________________________________________________________________________________________________________
        """# Lista de resultado dos arquivos duplicados"""
        self.var_result_duplicidade = tk.StringVar()
        self.lista_result_duplicidade = tk.Listbox(self.frame_label_duplicidade)
        self.lista_result_duplicidade.config(selectmode=tk.SINGLE, width=160, height=15)
        self.lista_result_duplicidade.place(y=3, x=3)

        # ______________________________________________________________________________________________________________
        """# Criando a barra de rolagem para lista de resultado"""
        self.barra_rolagem_lista_resultado_ducplicados = Scrollbar(self.janela_opc_duplicidade)
        self.barra_rolagem_lista_resultado_ducplicados.config(orient='vertical')
        self.barra_rolagem_lista_resultado_ducplicados.place(in_=self.lista_result_duplicidade)
        self.barra_rolagem_lista_resultado_ducplicados.place(relx=1.0, relheight=1.0)
        self.barra_rolagem_lista_resultado_ducplicados.place(bordermode='outside')
        self.barra_rolagem_lista_resultado_ducplicados.config(command=self.lista_result_duplicidade.yview)
        self.lista_result_duplicidade.config(yscrollcommand=self.barra_rolagem_lista_resultado_ducplicados.set)

        # ______________________________________________________________________________________________________________
        """Frame Superior duplicidade"""
        self.frame_superior_dupli = tk.Frame(self.frame_label_duplicidade, bg='#C0C0C0', width=980, height=90)
        self.frame_superior_dupli.place(y=250, x=3)

        # ______________________________________________________________________________________________________________
        """######## ckeck button"""
        """# Opcao check movendo os arquivos duplicados"""
        # 1
        self.var_opcao_radio = tk.IntVar()
        self.opcao_move = tk.Radiobutton(self.frame_superior_dupli)
        self.opcao_move.config(text='Mover arquivos duplicados', bg='#C0C0C0', value=1)
        self.opcao_move.config(variable=self.var_opcao_radio, pady=5, padx=5, bd=2)
        self.opcao_move.place(y=1, x=5)

        # ______________________________________________________________________________________________________________
        """# Opção Deletar arquivos duplicados"""
        # 2
        self.var_opcao_delete = tk.IntVar()
        self.opcao_delete = tk.Radiobutton(self.frame_superior_dupli)
        self.opcao_delete.config(text='Deletar arquivos duplicados', bg='#C0C0C0', value=2)
        self.opcao_delete.config(variable=self.var_opcao_radio, pady=5, padx=5, bd=2)
        self.opcao_delete.place(y=1, x=180)
        # ______________________________________________________________________________________________________________
        """# Opção Renomear arquivos selecionados"""
        # 3
        self.var_opcao_renomear = tk.BooleanVar()
        self.opcao_renomear = tk.Radiobutton(self.frame_superior_dupli)
        self.opcao_renomear.config(text='Renomear arquivos duplicados', bg='#C0C0C0', value=3)
        self.opcao_renomear.config(variable=self.var_opcao_radio, pady=5, padx=5, bd=2)
        self.opcao_renomear.place(y=1, x=360)

        # ______________________________________________________________________________________________________________
        """#### Barra de progresso"""
        self.barra_progresso_processo_duplicidade = Progressbar(self.frame_superior_dupli, orient=tk.HORIZONTAL)
        self.barra_progresso_processo_duplicidade.config(mode='determinate', length=165)
        self.barra_progresso_processo_duplicidade.place(y=65, x=800)

        # ______________________________________________________________________________________________________________
        """# Label barra de progresso"""
        self.var_lbl_barra_progresso = tk.StringVar()
        self.lbl_barra_progresso = tk.Label(self.frame_superior_dupli, text=self.var_lbl_barra_progresso)
        self.lbl_barra_progresso.config(text='Ocioso...', bg='#C0C0C0')
        self.lbl_barra_progresso.place(y=65, x=720)
        # ______________________________________________________________________________________________________________
        """# Label Informação do processo final"""
        self.var_lbl_info_process_fim = tk.StringVar()
        self.lbl_info_process_fim = tk.Label(self.frame_superior_dupli, text=self.var_lbl_info_process_fim)
        self.lbl_info_process_fim.config(text='Ocioso...', bg='#C0C0C0')
        self.lbl_info_process_fim.place(y=30, x=5)
        # ______________________________________________________________________________________________________________
        """# Label Informação tempo que vai levar para finalizar o processo."""
        self.var_lbl_info_tempo_processo = tk.StringVar()
        self.lbl_info_tempo_processo = tk.Label(self.frame_superior_dupli, text=self.var_lbl_info_tempo_processo)
        self.lbl_info_tempo_processo.config(text=f'Time search: 00:00:00', bg='#C0C0C0')
        self.lbl_info_tempo_processo.place(y=1, x=720)

        # ______________________________________________________________________________________________________________
        # ______________________________________________________________________________________________________________
        """#### Frame Inferio para botões"""
        self.frame_inferior_dupli = tk.Frame(self.frame_label_duplicidade, bg='#DCDCDC', width=980, height=233)
        self.frame_inferior_dupli.place(y=345, x=3)

        # ______________________________________________________________________________________________________________
        """#### Frame botao """
        """# Frame Botão de processar"""
        self.frame_lbl_botao_proc_dados = tk.LabelFrame(self.frame_inferior_dupli, text='Processar dados')
        self.frame_lbl_botao_proc_dados.config(bg="#DCDCDC", pady=5, padx=5)
        self.frame_lbl_botao_proc_dados.place(y=7, x=5)
        # ______________________________________________________________________________________________________________
        """# Frame Botão de limpar"""
        self.frame_lbl_botao_limpar = tk.LabelFrame(self.frame_inferior_dupli, text='Limpar lista')
        self.frame_lbl_botao_limpar.config(bg="#DCDCDC", pady=5, padx=5)
        self.frame_lbl_botao_limpar.place(y=80, x=5)
        # ______________________________________________________________________________________________________________
        """# Frame Botão de Voltar a janela principal"""
        self.frame_lbl_botao_voltar = tk.LabelFrame(self.frame_inferior_dupli, text='Limpar lista')
        self.frame_lbl_botao_voltar.config(bg="#DCDCDC", pady=5, padx=5)
        self.frame_lbl_botao_voltar.place(y=150, x=5)
        # ______________________________________________________________________________________________________________
        """#### Botoes de opcao"""
        self.botao_aplica_opcao_check = tk.Button(self.frame_lbl_botao_proc_dados)
        self.botao_aplica_opcao_check.config(text='Aplicar', bg='#DCDCDC', width=133)
        self.botao_aplica_opcao_check.config(command=self.thread_opcao_check_botao)
        self.botao_aplica_opcao_check.pack(anchor='center', pady=5, padx=5)
        # ______________________________________________________________________________________________________________
        """# Botão para limpar as lista e os checklist"""
        self.botao_aplica_opcao_limpar = tk.Button(self.frame_lbl_botao_limpar)
        self.botao_aplica_opcao_limpar.config(text='Aplicar', bg='#DCDCDC', width=133)
        self.botao_aplica_opcao_limpar.config(command=self.thread_opcao_check_botao)
        self.botao_aplica_opcao_limpar.pack(anchor='center', pady=5, padx=5)
        # ______________________________________________________________________________________________________________
        """# Botão para fechar a janela secundaria e voltar para janela principal """
        self.botao_aplica_opcao_voltar = tk.Button(self.frame_lbl_botao_voltar)
        self.botao_aplica_opcao_voltar.config(text='Aplicar', bg='#DCDCDC', width=133)
        self.botao_aplica_opcao_voltar.config(command=self.thread_opcao_check_botao)
        self.botao_aplica_opcao_voltar.pack(anchor='center', pady=5, padx=5)
        # ______________________________________________________________________________________________________________

        """ Responsável por manter a janela de duplicidade ativa (padrão do tkinter)"""
        self.janela_opc_duplicidade.update_idletasks()

    def janela_renomar_varios_arquivos(self):
        print('Iniciando a janela "janela_renomar_varios_arquivos"')
        self.janela_renomar_arquivos = tk.Toplevel()
        self.janela_renomar_arquivos.geometry('900x300')
        self.janela_renomar_arquivos.title('Manipulando arquivos.')
        self.janela_renomar_arquivos.resizable(0, 0)
        # ______________________________________________________________________________________________________________
        """ Label frame da janela principal. """
        self.frame_lbl_janela_renomar = tk.LabelFrame(self.janela_renomar_arquivos, text='Manipulando arquivos')
        self.frame_lbl_janela_renomar.config(width=850, height=290)
        self.frame_lbl_janela_renomar.pack(fill=tk.BOTH, pady=5, padx=5)
        # ______________________________________________________________________________________________________________
        """ Label Frame das opções de renomear """
        self.frame_lbl_opcao_rename = tk.LabelFrame(self.frame_lbl_janela_renomar, text='Escolha uma opcação')
        self.frame_lbl_opcao_rename.config(width=875, height=75)
        self.frame_lbl_opcao_rename.place(y=5, x=5)
        # ______________________________________________________________________________________________________________
        """ Oções para manipular o nome dos arquivos. """

        radio_rename = tk.IntVar()
        self.opcao_01 = Radiobutton(self.frame_lbl_opcao_rename, variable=radio_rename)
        self.opcao_01.config(text='Remover Caracteres', value=1)
        self.opcao_01.place(y=5, x=5)

        self.opcao_02 = Radiobutton(self.frame_lbl_opcao_rename, variable=radio_rename)
        self.opcao_02.config(text='Acrescentar Caracteres', value=2)
        self.opcao_02.place(y=30, x=5)

        self.opcao_03 = Radiobutton(self.frame_lbl_opcao_rename, variable=radio_rename)
        self.opcao_03.config(text='Renomear arquivo', value=3)
        self.opcao_03.place(y=30, x=150)

        self.opcao_03 = Radiobutton(self.frame_lbl_opcao_rename, variable=radio_rename)
        self.opcao_03.config(text='Adicionar indice', value=4)
        self.opcao_03.place(y=5, x=150)

        self.var_lista_manipular = tk.StringVar()
        self.lista_arquivos_listados = tk.Listbox(self.frame_lbl_janela_renomar, listvariable=self.var_lista_manipular)
        self.lista_arquivos_listados.config(width=145, height=10)
        self.lista_arquivos_listados.place(y=90, x=5)
        # ______________________________________________________________________________________________________________

    """##### THREADS DOS BOTÕES"""
    def thread_opcao_check_botao(self):
        print('Iniciando a thread "thread_opcao_check_botao"')
        Thread(target=self.opcao_check_botao).start()

    def thread_processo_hashlib_duplicados(self):
        print('Iniciando a thread "thread_processo_hashlib_duplicados"')
        Thread(target=self.acao_arquivos_duplicidades).start()

    def thread_limpeza_lista_dupli(self):
        print('Iniciando a thread "thread_limpeza_lista_dupli"')
        Thread(target=self.botao_limpa_list_dupli).start()

    def thread_tempo__busca(self):
        Thread(target=self.tempo_processo_busca).start()

    """#### Sistema de combo e criaçãodo checkbutton"""
    def selecao_combo_extensao(self, *args):
        print('Iniciando função "selecao_combo_extensao" ')
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

            TEXTOS=['pdf', 'rtf', 'wbk', 'wpd', 'wp5', 'txt', 'log', 'xml', 'parquet'],

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
                # print(f'{contador}-linhas{linhas}-colunas{colunas}')  # Primeira linha dos codigos de linhas
                for valor_extensao in valor:
                    self.lista_var.append(tk.IntVar())
                    self.botoes_chek.append(tk.Checkbutton(
                        self.frames_superior, text=valor_extensao.upper(),
                        variable=self.lista_var[contador],
                        bg='#C0C0C0')
                    )
                    # calcula as posições de cada check box
                    self.botoes_chek[-1].place(y=linhas, x=colunas)
                    if linhas == 195:
                        linhas = 25
                        colunas += 120
                    else:
                        linhas += 17
                    contador += 1

                    """### Mapeamento das coordenadas de criação das opções do checkbutton"""
                    # print(f'{contador}-linhas[{linhas}]-colunas[{colunas}]')

    """ Processos de eventos simples"""
    def evento_mouse(self, event=None):
        print(event)
        print('Funciona')

    def evento_mostrar(self, event=None):

        """ Verifica se já existe um tooltip
        ou se o texto está vazio; se qualquer
        uma dessas condições for verdadeira,
        a função retorna imediatamente."""
        if self.tooltip or not self.texto:
            return

        """Calcula a posição onde o tooltip deve aparecer, 
        ajustando a posição do botão na janela."""
        x, y, _, _ = self.botao_inicio_processo.bbox('insert')
        x += self.botao_inicio_processo.winfo_rootx() + 25
        y += self.botao_inicio_processo.winfo_rooty() + 25

        """Cria uma nova janela de topo (Toplevel), remove as 
        bordas padrão (wm_overrideredirect(True)), e posiciona a 
        janela de acordo com os cálculos anteriores."""
        self.tooltip = tk.Toplevel(self.janela_principal)
        self.tooltip.wm_overrideredirect(True)
        self.tooltip.wm_geometry(f'+{x}+{y}')

        """Adiciona um rótulo (Label) à janela do tooltip com o 
        texto apropriado e estilo visual, e imprime "Entrou" no console."""
        msg_label = Label(self.tooltip, text=self.texto, background='yellow')
        msg_label.pack()

    def evento_esconder(self, event=None):
        """Se um tooltip está presente, destrói a
        janela do tooltip e define o atributo tooltip como None."""
        if self.tooltip:
            self.tooltip.destroy()
            self.tooltip = None

    """#### Processos simples"""
    def data_hora_certa(self):
        print('Iniciando função "data_hora_certa"')

        valor_data = datetime.now()
        self.data_certa = valor_data.strftime('%d/%m/%Y')
        self.hora_certa = valor_data.strftime("%H:%M")
        self.lbl_hora_certa.config(text=f'Inicio do programa:[{self.hora_certa}-{self.data_certa}]')

    # Responsavel por manter uma pasta de busca padrão
    def func_pasta_destino_padrao(self):
        print('Iniciando função "func_pasta_destino"')
        # ______________________________________________________________________________________________________________
        """# Pasta padrão da busca; sempre tento usar a pasta do usuário"""
        self.diretorio_home = Path.home()

    def botao_limpeza_checkbutton_destroy(self):
        print('Iniciando funçao "botao_limpeza_checkbutton_destroy"')
        print(f'\nRemovendo os botões check\n')
        if self.ativar_combo:
            for valor_destroy in self.botoes_chek:
                valor_destroy.destroy()
            """# Tambem limpa a lista de busca"""
            self.lista_de_result_busca.delete('0', 'end')
            self.func_pasta_destino_padrao()
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

    def botao_limpa_list_dupli(self):
        self.lista_result_duplicidade.destroy()

    def fechar_janela(self):
        print('Janela fechou')
        self.janela_principal.destroy()

    def abrir_arquivos(self):
        open_arquivo = self.lista_de_result_busca.get(self.lista_de_result_busca.curselection())
        print(f'Abrindo arquivo: {open_arquivo}')
        try:
            Thread(target=startfile(open_arquivo))
        except FileNotFoundError:
            showwarning('AVISO', 'Não foi possível abrir o arquivo selecionado!')
        print()
        print('Arquivo em execusão!!')

    """#### Inicio dos processos de busca """
    def tempo_processo_busca(self):
        print('Iniciando função "tempo_processo_busca"')
        """
        Função vai se responsavel em contar o tempo que a busca foi realizada.
        :return:
        """
        print('\nIniciando time da busca')
        msg_info_time = str
        contagem_segundos = 0
        contagem_minutos = 0
        contagem_horas = 0
        if self.ativar_time_busca:
            while self.ativar_time_busca:
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

                """#### Utilizo o mesmo ativar para o processo de duplicidade para ativar o cronometro"""
                if self.ativar_time_proce:
                    if self.ativar_segundos:
                        self.lbl_info_tempo_processo['text'] = f"{msg_info_time} Segundo's"
                    elif self.ativar_minutos:
                        self.lbl_info_tempo_processo['text'] = f"{msg_info_time} Minuto's"
                    elif self.ativar_horas:
                        self.lbl_info_tempo_processo['text'] = f"{msg_info_time} HORA'S"
                else:
                    if self.ativar_segundos:
                        self.lbl_tempo_busca['text'] = f"{msg_info_time} Segundo's"
                    elif self.ativar_minutos:
                        self.lbl_tempo_busca['text'] = f"{msg_info_time} Minuto's"
                    elif self.ativar_horas:
                        self.lbl_tempo_busca['text'] = f"{msg_info_time} HORA'S"

                """# Guarda as informações para colocar no relatório"""
                self.tempo_gasto_da_busca = msg_info_time
                contagem_segundos += 1
                sleep(1)

    def botao_pasta_destino(self):
        print(f'botao_pasta_destino sendo ativado')
        self.ativar_selecionar_pasta_destino = True
        self.diretorio_home = Path(askdirectory())
        self.lbl_pts_dest.config(text=f'Pasta de busca: [{self.diretorio_home}]', bg='#C0C0C0')

    """ Processo para adicionar um indice em cada arquivo """
    def renomear_e_adicionar_indice(self):

        showinfo('IMPORTANTE', 'Útilize apenas com arquivos da mesma pasta.')
        from os import path
        from time import ctime
        lista_arquivos_com_data = []

        indice = 1  # declaração em número interiro

        # Verifica se a lista possui algum item para adicionar o indice.
        if len(self.lista_para_renomear) > 0:

            for arquivos_por_data in self.lista_para_renomear:
                data_criacao = path.getctime(arquivos_por_data)
                data_fomatada = ctime(data_criacao)
                lista_arquivos_com_data.append(f'{arquivos_por_data} <--> {data_fomatada}')

            arquivos_ordenados = sorted(lista_arquivos_com_data, key=lambda x: x[1])

            for valor_completo_arquivo in arquivos_ordenados:

                # Valor compledo dos dados que esta chegando.
                # G:\Meu Drive\Fotos\Privado\IMG_20241120_212541871_AE.jpg - Sat Nov 23 12:42:59 2024

                # Calcula a quantidade de elementos que possui dentro da lista.
                indice_lista = int(len(str(valor_completo_arquivo).split('\\')))

                # Separa o arquivo do diretório
                separacao_diretorio_arquivo = str(valor_completo_arquivo).split('\\')[indice_lista - 1]
                # IMG_20241120_212541871_AE.jpg - Sat Nov 23 12:42:59 2024

                # Removendo a data imbutida
                indice_do_arquivo = len(str(separacao_diretorio_arquivo).split('<-->'))
                arquivo_sem_data = str(separacao_diretorio_arquivo).split('<-->')[indice_do_arquivo - 2].strip()

                # IMG_20241120_212541871_AE.jpg

                # O arquivo sera renomeado adicionando apenas o indice.
                # rename(
                #     f'{self.diretorio_home}\\{arquivo_sem_data}',
                #     f'{self.diretorio_home}\\{indice}°|{arquivo_sem_data}'
                # )

                # G:\Meu Drive\Fotos\Privado\63.IMG_20241120_212541871_AE.jpg - Sat Nov 23 12:42:59 2024
                indice += 1

                print(f'{self.diretorio_home}\\{indice}°|{arquivo_sem_data}')
        else:
            showinfo('Aviso', 'Não existe arquivos para inserir os indices')

    """ Processo para renomar os arquivo único. Selecione um arquivo, após a busca e renomei """
    def botao_renomear_arquivos(self):

        valor_arq_selecionado = self.lista_de_result_busca.get(self.lista_de_result_busca.curselection())

        separacao_pasta_arq = str(valor_arq_selecionado).split('\\')
        nome_arquivo_renomear = separacao_pasta_arq[-1]
        extensao_arquivo = nome_arquivo_renomear.split('.')[-1]
        caminho_do_arquivo = separacao_pasta_arq[:-1]
        caminho_formtado = '\\'.join(caminho_do_arquivo)

        novo_nome = askstring('...', 'Digite um novo nome: ')

        print('-------------')
        print(f'Arquivo original: {caminho_formtado}\\{nome_arquivo_renomear}')
        arquivo_original = str(f'{caminho_formtado}\\{nome_arquivo_renomear}')

        print('-------------')
        print(f'Arquivo novo: {caminho_formtado}\\{novo_nome}.{extensao_arquivo}')
        arquivo_novo = str(f'{caminho_formtado}\\{novo_nome}.jpg')

        print('-------------')
        try:
            rename(f'{arquivo_original}', f'{arquivo_novo}')
            print('Nome modificado')
        except Exception as e:
            print(f'Erro: {e}')

    """#### Modulo de processo de duplicidade"""
    def botao_modulo_duplicidade(self):
        print('Iniciando função "botao_modulo_duplicidade"')

        """# Declarações de varial local"""
        dict_duplicado = dict()

        """# Abre a janela de duplicidade. Nela contém todas as opções para tratar os dados duplicados"""
        self.janela_duplicidade()

        """ Identificando os valores repetidos"""
        try:
            for valor_lista_busca in self.dados_do_processo_busca:
                cortando_valores_da_busca = str(valor_lista_busca).split('|')
                valor_caminho_da_busca = cortando_valores_da_busca[0]
                valor_arquivo_da_busca = cortando_valores_da_busca[1]

                """# Calcula os dados duplicados"""
                if valor_arquivo_da_busca in dict_duplicado:
                    dict_duplicado[valor_arquivo_da_busca] += 1
                else:
                    dict_duplicado[valor_arquivo_da_busca] = 1

            """# Abre o dicionario e mostras as informações para o usuário"""
            try:
                for k, v in dict_duplicado.items():
                    if v > 1:
                        self.lista_result_duplicidade.insert('end', f'[{k}]  ===>  [{v}]')
            except UnboundLocalError:
                showerror("ERROR", "Não existem dados para serem apresentados na lista de duplicados!")
        except:
            showwarning("AVISO", "Não possui dados na lista 'self.dados_do_processo_busca'")

    def acao_arquivos_duplicidades(self):
        print('Iniciando processo de "processo_hashlib_duplicados"')

        """chamada de modulo local"""
        from hashlib import md5
        from shutil import move

        """# Declaração de variavel"""
        unico_arquivo = dict()
        indice = 1

        """#### Caso escolha mover os arquivos para outra pasta, abre-se uma janela para escolha qual pasta"""
        if self.ativar_opcao_mover:
            caminho_destino = Path(askdirectory(title="Escolha uma Pasta"))

        """# Mudando o status do lbl na barra de progresso"""
        self.lbl_barra_progresso.config(text='Processando...', bg='#C0C0C0')

        """# Valor de cara RADIO Button"""
        print(f'Status mover: {self.ativar_opcao_mover}\n'
              f'Status deletar: {self.ativar_opcao_delete}\n'
              f'status renomear: {self.ativar_opcao_renomear}')

        """# Iniciando barra de progresso na janela de duplicidade """
        print('Iniciando barra de progresso na janela duplicidade')
        self.barra_progresso_processo_duplicidade.start()

        """# Ativando tempo do processo """
        self.ativar_time_busca = True
        self.ativar_time_proce = True
        lambda: Thread(target=self.tempo_processo_busca).start()

        """# Processo para verificar os arquivos ducplicados usando o hashlib """
        for valor in self.dados_para_duplicidade:

            """#### Declarando o valor de hashlib"""
            caminho_arquivo = Path(valor)
            hash_file = md5(open(caminho_arquivo, 'rb').read()).hexdigest()

            """#### opcao mover"""
            if self.ativar_opcao_mover:
                if hash_file in unico_arquivo:
                    print(f'Movendo {indice}º {caminho_arquivo} para {caminho_destino}')
                    self.lbl_info_process_fim.config(text=f'Movendo {indice}-{caminho_arquivo} para {caminho_destino}')
                    try:
                        move(caminho_arquivo, caminho_destino)
                        print(f'Arquivos {caminho_arquivo} movidos com sucesso! \n'
                              f'Pasta de destino: {caminho_destino}\n')
                    except shutil.Error:
                        move(caminho_arquivo, caminho_destino)
                        showerror('AVISO', f'Arquivo {caminho_arquivo} já existe nessa pasta')
                else:
                    unico_arquivo[hash_file] = caminho_arquivo
                    indice += 1

            elif self.ativar_opcao_delete:
                """#### opcao delete"""
                if hash_file in unico_arquivo:
                    pass
                else:
                    unico_arquivo[hash_file] = caminho_arquivo
                    indice += 1

            elif self.ativar_opcao_renomear:
                """#### opcao renomear"""
                if hash_file in unico_arquivo:
                    pass
                else:
                    unico_arquivo[hash_file] = caminho_arquivo
                    indice += 1

        """# Finalizando a barro de progresso na janela duplicidade"""
        self.barra_progresso_processo_duplicidade.stop()
        self.barra_progresso_processo_duplicidade.config(value=100)
        print('Finalizando barra de progresso na janela duplicidade')

        if self.ativar_opcao_mover:
            funcao_realizada = f'Arquivo movimentao para {caminho_destino}'
        elif self.ativar_opcao_delete:
            funcao_realizada = 'Todos os arquivos duplicados foram deletados'
        elif self.ativar_opcao_renomear:
            funcao_realizada = 'Nome do arquivo renomeado para {}'
        self.lbl_info_process_fim.config(text=f'{funcao_realizada}')

        """#### Desativando tempo do processo"""
        self.ativar_time_busca = False
        self.ativar_time_proce = False
        self.lbl_info_tempo_processo['text'] = f"O processo levou {self.tempo_gasto_da_busca} (H/M/S)"
        """# Limpando lista de dados"""
        del self.dados_para_duplicidade[:]

    def opcao_check_botao(self):
        print('Iniciando "opcao_check_botao"')
        resposta_radio = self.var_opcao_radio.get()
        if resposta_radio == 1:
            self.ativar_opcao_mover = True
            self.ativar_opcao_delete = False
            self.ativar_opcao_renomear = False

        if resposta_radio == 2:
            print('teste delete')
            self.ativar_opcao_mover = False
            self.ativar_opcao_delete = True
            self.ativar_opcao_renomear = False

        if resposta_radio == 3:
            print('teste renomear')
            self.ativar_opcao_mover = False
            self.ativar_opcao_delete = False
            self.ativar_opcao_renomear = True

        """# chama a função para realizar o processo dos arquivos duplicados"""
        self.thread_processo_hashlib_duplicados()

    """#### Processo de Busca"""
    def botao_inicio_da_busca_principal(self):
        print('Iniciando função "botao_inicio_da_busca_principal"')
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

        """# A busca apenas começa quando se escolhe uma extensão"""
        if self.ativar_combo:

            """#### Limpando as listas de buscas"""
            del self.dados_do_processo_busca[:]
            del self.dados_para_duplicidade[:]

            """# As informações das extensão chegou no loop abaixo"""
            try:
                for valor_var in range(len(self.lista_var)):
                    if self.lista_var[valor_var].get() == 1:
                        extensoes.append(self.botoes_chek[valor_var]["text"])
                self.lbl_ext_selec.config(text=f'Selecionado extensão: [{extensoes}] para o processo de busca.')
            except AttributeError:
                showwarning("AVISO", 'Nenhuma extensão selecionada')

            """# Valida se extensão possui mais de um valor"""
            if len(extensoes) == 1:
                self.ativar_uma_extensao = True
            elif len(extensoes) == 0:
                showwarning("AVISO", 'É preciso selecionar uma extensão')

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
                self.ativar_time_busca = True
                self.thread_tempo__busca()

                """###### Inicio do processo de busca"""
                for raiz, subpasta, arquivo in walk(self.diretorio_home):

                    """# O contador de inicio ser para verificar se é a primeira pasta. Ja que o 'os.walk' mostra
                    todas as pastas, devido ao loop. Então essa condição evita que mostre todos as pastas descenecess"""
                    if contador_inicio == 1:
                        print()
                        print(f'DIRETORIO RAIZ: [{raiz}]')

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
                            try:

                                # Processo para indices

                                self.lista_para_renomear.append(path.join(raiz, valor_file))

                                # Adiciona os arquivos na lista, para processar arq duplicados
                                self.dados_para_duplicidade.append(path.join(raiz, valor_file))
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

                                """# As 4 variaveis são responsaveis por dividir as informações, para dar mais 
                                destaque"""

                                caminho_completo = path.join(raiz, valor_of_file)

                                extensao_destaque = str(caminho_completo).split('\\')[-1]
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
                                    print(f'{resultado_destaque}')

                                    """# Mostra o resultado na lista de busca"""
                                    self.lista_de_result_busca.insert('end', '')
                                    self.lista_de_result_busca.insert('end', '')
                                    self.lista_de_result_busca.insert('end', f'{raiz}')
                                    self.lista_de_result_busca.insert('end', '===' * 40)
                                    self.lista_de_result_busca.insert('end',
                                                                      f'{raiz}\\{extensao_destaque}')
                                else:
                                    """# Na lista abaixo, são inseridos todos os dados da busca para que possa ser 
                                    realizado qualquer tipo de analise"""
                                    self.dados_do_processo_busca.append(f'{raiz}|{extensao_destaque}')

                                    """# Mostra os resultados no prompt e na lista de busca"""
                                    print(f'[{resultado_destaque}]')
                                    self.lbl_info_real_time.config(text=f'Arquivos encontrados: [{valor_de_busca}]')
                                    self.lista_de_result_busca.insert(
                                        'end', f'{raiz}\\{extensao_destaque}'
                                    )

                                """# Por padrão, o valor começa com 1, antes é anlisado se possui um arquivo que 
                                correponda ao valor de extensão, caso seja, mostra a pasta que foi encontrado, 
                                mas depois passa a mostrar apenas os arquivos dentro dessa pasta.
                                  - Após mostrar a pasta, o contador passa a soma o valor para cada item."""
                                contador_itens += 1

                                """# Contador que é responsável pela quantidade de arquivos encontrados."""
                                contador_de_arquivos += 1
                            except UnboundLocalError:
                                pass

                """###### Fim do processo de busca"""
                """# Desliga a barra de progresso, ao final da busca"""
                self.barra_progresso_busca.stop()
                self.barra_progresso_busca.config(value=100)

                """# Após as buscas finalizarem, os botões serão ativados"""
                self.botao_inicio_processo.config(state=tk.NORMAL)
                self.botao_limpar_checkbuttun.config(state=tk.NORMAL)
                self.botao_destino_busca.config(state=tk.NORMAL)
                self.botao_duplicidade.config(state=tk.NORMAL)
                self.botao_abrir_arquivo.config(state=tk.NORMAL)

                """# Número de itens encontrados"""
                self.lbl_info_real_time.config(text=f'Fim da BUSCA!')
                print(f'\nItens encontrados: [ {contador_de_arquivos} ]')

                """# Desativa o validador de tempo de busca"""
                print(f'\nDesativando "time_busca"')
                sleep(1)
                self.ativar_time_busca = False
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
                print(f'\nForam encontrados [{contador_de_arquivos}] arquivos, dentro de [{contador_de_pastas}] pastas')
            else:
                showwarning('AVISO', 'Escolha apenas um extensão')
        else:
            showwarning("IMPORTANTE AVISO!", 'Escolha uma categora e uma única extensão '
                                             'para realizar a busca.')


iniciando_obj = ProgramaPrincipal()
