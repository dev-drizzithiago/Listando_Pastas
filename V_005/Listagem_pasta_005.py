import tkinter as tk
from tkinter.filedialog import askdirectory
from tkinter.messagebox import showinfo
from tkinter.simpledialog import askstring, askinteger, askfloat


class ListagemPasta:
    def __init__(self):
        self.extensoes = ['JPG', 'MP4', 'MP3']

        self.janela_principal = tk.Tk()
        self.janela_principal.geometry('600x300')
        self.janela_principal.title('Versão 5')

        self.label_principal_01 = tk.LabelFrame(self.janela_principal, text='Escolha um tipo de extensão')
        self.label_principal_02 = tk.LabelFrame(self.janela_principal)
        self.label_principal_01.pack()
        self.label_principal_02.pack()

        self.botao_adicionar_01 = tk.Button(self.label_principal_02, text='Adicionar', command=self.add_extensao)
        self.botao_adicionar_01.pack(side='left')
        self.botao_iniciar_programa = tk.Button(self.label_principal_02, text='Iniciar programa')
        self.botao_iniciar_programa.pack(side='right')

        self.janela_principal.mainloop()

    def add_extensao(self):
        try:
            valor_dados_add = tk.simpledialog.askstring('Bem vindo!', 'Adicione uma extensão')
            self.extensoes.append(valor_dados_add)
            tk.messagebox.showinfo('AVISO', 'Extensão adicionada com sucesso!')
        except:
            tk.messagebox.showerror('AVISO', 'Não foi possível adicionar a extensão')


inicio_obj = ListagemPasta()
