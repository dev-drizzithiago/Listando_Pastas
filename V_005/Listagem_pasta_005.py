import tkinter as tk


class ListagemPasta:
    def __init__(self):
        self.janela_principal = tk.Tk()
        self.janela_principal.geometry('600x300')
        self.janela_principal.title('Versão 5')

        self.label_principal_01 = tk.LabelFrame(self.janela_principal, text='Escolha um tipo de extensão')
        self.label_principal_02 = tk.LabelFrame(self.janela_principal)
        self.label_principal_01.pack()
        self.label_principal_02.pack()

        self.botao_adicionar_01 = tk.Button(self.label_principal_02, text='Adicionar ')

        self.janela_principal.mainloop()


inicio_obj = ListagemPasta()
