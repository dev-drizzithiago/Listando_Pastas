import tkinter as tk
from os import mkdir
from tkinter import ttk
from pathlib import Path
from tkinter.filedialog import askdirectory
from tkinter.messagebox import showinfo
from tkinter.simpledialog import askstring, askinteger, askfloat


class ListagemPasta:
    def __init__(self):

        pasta_home = Path.home()
        self.exten_listadas = []
        self.tipos_midias = ['Videos', 'Imagens']
        self.pasta_destino = str(Path(pasta_home, 'AppData', 'LocalLow', 'extensoes'))
        self.arqui_txt = str('\\extensoes.txt')

        # Janela Principal
        self.janela_principal = tk.Tk()
        self.janela_principal.geometry('300x390')
        self.janela_principal.title('Versão 5')
        self.janela_principal.resizable(False, False)

        # LabelFrames
        self.label_principal_01 = tk.LabelFrame(self.janela_principal, text='Escolha um tipo de extensão')
        self.label_principal_02 = tk.LabelFrame(self.janela_principal)
        self.label_principal_03 = tk.LabelFrame(self.janela_principal)
        self.label_principal_03.pack(side='top', fill='both', pady=5, padx=5)
        self.label_principal_01.pack(anchor='center', fill='both', pady=5, padx=5)
        self.label_principal_02.pack(anchor='s', fill='both', pady=5, padx=5)



        # Iniciando algumas funções
        self.verif_arq_ext_txt()
        self.lista_extensoes_dispo = tk.Listbox(self.label_principal_01, justify='center', selectmode=tk.SINGLE, relief='sunken')
        self.lista_extensoes_dispo.pack(fill='both')
        self.extensoes_adicionadas()

        # Caixa de combinação
        self.current_var = tk.StringVar()
        self.lista_de_midias = ttk.Combobox(self.label_principal_03, textvariable=self.current_var, justify='center')
        self.lista_de_midias['values'] = self.tipos_midias
        self.lista_de_midias.set('Tipos de arquivos disponível')
        self.lista_de_midias.pack(fill='both', side='top')
        self.lista_de_midias.current()

        # Botoes
        self.botao_adicionar_01 = tk.Button(self.label_principal_02, text='Adicionar + extensões', command=self.registrar_extensao)
        self.botao_iniciar_programa = tk.Button(self.label_principal_02, text='Iniciar a busca', command=self.busca_principal)
        self.botao_atualizar_lista = tk.Button(self.label_principal_02, text='Atualizar Lista de extensões', command=self.atualizar_lista)
        self.botao_sair = tk.Button(self.label_principal_02, text='Fechar o Programa', command=self.janela_principal.destroy)

        self.botao_iniciar_programa.pack(side='top', padx=5, pady=5)
        self.botao_adicionar_01.pack(fill='both', padx=5, pady=5)
        self.botao_atualizar_lista.pack(fill='both', padx=5, pady=5)
        self.botao_sair.pack(pady=5, padx=5)
        # looping
        self.janela_principal.mainloop()
    
    def busca_principal(self):
        valor_busca = self.lista_extensoes_dispo.curselection()

        # Janele da busca
        self.janela_da_busca = tk.Tk()
        self.janela_da_busca.geometry('700x300')
        self.janela_da_busca.title('Busca V_5')

        self.label_frame_busca_01 = tk.LabelFrame(self.janela_da_busca)
        self.label_frame_busca_01.pack(side='bottom', fill='both')

        self.label_da_busca = tk.LabelFrame(self.janela_da_busca, text='Buscando arquivos', padx=5, pady=5)
        self.label_da_busca.pack(fill='both')

        self.lista_das_busca = tk.Listbox(self.label_da_busca, justify='left')
        self.lista_das_busca.pack(fill='both')

        self.botao_busca_sair = tk.Button(self.label_frame_busca_01, text='Sair')
        self.botao_busca_sair.pack(fill='both')

        if len(valor_busca) == 0:
            self.valor_ext = ''
            tk.messagebox.showinfo('Aviso', 'Você não escolheu nenhuma extensão,\n'
                                            'sera listado todos os arquivos!')
        else:
            for valor_extensao in valor_busca:
                self.valor_ext = str(self.exten_listadas[valor_extensao])

        caminho_da_busca = Path(askdirectory())
        for busca in caminho_da_busca.glob('**/*' + self.valor_ext):
            if busca.is_file():
                self.lista_das_busca.insert('0', busca)
            elif busca.is_dir():
                self.lista_das_busca.insert('0', busca)
        self.lista_das_busca.pack(anchor='center')

    def registrar_extensao(self):
        try:
            mkdir(self.pasta_destino)
        except FileExistsError:
            valor_dados_add = tk.simpledialog.askstring('Bem vindo!', 'Adicione uma extensão')
            try:
                obj_registro = open(self.pasta_destino + self.arqui_txt, 'a')
                obj_registro.write(f'{valor_dados_add.upper()}\n')
                tk.messagebox.showinfo('AVISO', f'Extensão [{valor_dados_add}] foi adicionada com sucesso!')
            except:
                tk.messagebox.showerror('AVISO!', 'Não foi possível registrar nos arquivo\n'
                                                  '{0037/registro}')

    def extensoes_adicionadas(self):
        try:
            valor_extensao = open(self.pasta_destino + self.arqui_txt, 'r')
            for valor_ext in valor_extensao:
                self.exten_listadas.append(valor_ext.replace('\n', ''))
                self.lista_extensoes_dispo.insert('end', valor_ext)
        except FileNotFoundError:
            tk.messagebox.showerror('AVISO!', f'Não foi encontrado o arquivo {self.arqui_txt}')


    def atualizar_lista(self):
        self.lista_extensoes_dispo.delete('0', 'end')
        self.extensoes_adicionadas()

    # Verificações
    def verif_arq_ext_txt(self):
        try:
            teste_arq = open(self.pasta_destino + self.arqui_txt, 'r')
            teste_arq.close()
        except FileNotFoundError:
            tk.messagebox.showwarning('Importante', f'O arquivos {self.arqui_txt} não existe!\n'
                                                    f'É preciso criar com pelo menos uma extensão...')
            self.registrar_extensao()


inicio_obj = ListagemPasta()
