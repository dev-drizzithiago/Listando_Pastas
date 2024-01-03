import tkinter as tk
from os import mkdir
from pathlib import Path
from tkinter.filedialog import askdirectory
from tkinter.messagebox import showinfo
from tkinter.simpledialog import askstring, askinteger, askfloat


class ListagemPasta:
    def __init__(self):
        self.extensoes_adicionadas()
        # elf.extensoes = ['JPG', 'MP4', 'MP3']
        pasta_home = Path.home()
        self.pasta_destino = str(Path(pasta_home, 'AppData', 'LocalLow', 'extensoes'))
        self.arqui_txt = str('\\extensoes.txt')
        self.janela_principal = tk.Tk()
        self.janela_principal.geometry('600x300')
        self.janela_principal.title('Versão 5')

        self.label_principal_01 = tk.LabelFrame(self.janela_principal, text='Escolha um tipo de extensão', pady=3,
                                                padx=3)
        self.label_principal_02 = tk.LabelFrame(self.janela_principal)
        self.label_principal_01.pack()
        self.label_principal_02.pack()

        # valor_extensoes = tk.Variable(value=self.extensoes)
        valor_extensoes = tk.Variable(value=self.exten_listadas)
        self.lista_extensoes_dispo = tk.Listbox(self.label_principal_01, listvariable=valor_extensoes, justify='center')
        self.lista_extensoes_dispo.pack(anchor='center')

        self.botao_adicionar_01 = tk.Button(self.label_principal_02, text='Adicionar extensões',
                                            command=self.registrar_extensao)
        self.botao_adicionar_01.pack(side='left')
        self.botao_iniciar_programa = tk.Button(self.label_principal_02, text='Iniciar programa')
        self.botao_iniciar_programa.pack(side='right')

        self.janela_principal.mainloop()

    def registrar_extensao(self):
        try:
            mkdir(self.pasta_destino)
        except FileExistsError:
            valor_dados_add = tk.simpledialog.askstring('Bem vindo!', 'Adicione uma extensão')
            try:
                obj_registro = open(self.pasta_destino + self.arqui_txt, 'a')
                obj_registro.write(f'{valor_dados_add}\n')
                tk.messagebox.showinfo('AVISO', f'Extensão [{valor_dados_add}] foi adicionada com sucesso!')
            except:
                tk.messagebox.showerror('AVISO!', 'Não foi possível registrar nos arquivo\n'
                                                  '{0037/registro}')

    def extensoes_adicionadas(self):
        try:
            valor_extensao = open(self.pasta_destino + self.arqui_txt, 'r')
            for valor_ext in valor_extensao:
                self.exten_listadas = valor_ext
                print(self.exten_listadas)
        except FileNotFoundError:
            tk.messagebox.showerror('AVISO!', f'Não vou encontrado do arquivo {self.arqui_txt}')


inicio_obj = ListagemPasta()
