import tkinter as tk
from pathlib import Path
from tkinter.filedialog import askdirectory
from tkinter.messagebox import showinfo
from tkinter.simpledialog import askstring, askinteger, askfloat


class ListagemPasta:
    def __init__(self):
        self.extensoes = ['JPG', 'MP4', 'MP3']
        pasta_home = Path.home()
        self.pasta_destino = Path(pasta_home, 'AppData', 'LocalLow', 'extensoes', 'extensoes.txt')
        self.janela_principal = tk.Tk()
        self.janela_principal.geometry('600x300')
        self.janela_principal.title('Versão 5')

        self.label_principal_01 = tk.LabelFrame(self.janela_principal, text='Escolha um tipo de extensão', pady=3,
                                                padx=3)
        self.label_principal_02 = tk.LabelFrame(self.janela_principal)
        self.label_principal_01.pack()
        self.label_principal_02.pack()

        valor_extensoes = tk.Variable(value=self.extensoes)
        self.lista_extensoes_dispo = tk.Listbox(self.label_principal_01, listvariable=valor_extensoes, justify='center')
        self.lista_extensoes_dispo.pack(anchor='center')

        self.botao_adicionar_01 = tk.Button(self.label_principal_02, text='Adicionar extensões',
                                            command=self.registrar_extensao)
        self.botao_adicionar_01.pack(side='left')
        self.botao_iniciar_programa = tk.Button(self.label_principal_02, text='Iniciar programa')
        self.botao_iniciar_programa.pack(side='right')

        self.janela_principal.mainloop()

    def registrar_extensao(self, valor_registro):
        valor_dados_add = tk.simpledialog.askstring('Bem vindo!', 'Adicione uma extensão')
        pasta_destino = self.pasta_destino
        try:
            obj_registro = open(pasta_destino, 'a')
            obj_registro.write(f'{valor_registro}\n')
            tk.messagebox.showinfo('AVISO', 'Extensão {} foi adicionada com sucesso!')
        except:
            tk.messagebox.showerror('AVISO!', 'Não foi possível registrar nos arquivo')


inicio_obj = ListagemPasta()
