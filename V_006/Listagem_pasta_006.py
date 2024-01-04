import tkinter as tk
from tkinter import ttk


class JanelaTeste:
    def __init__(self):
        self.janela_principal = tk.Tk()
        self.janela_principal.geometry('300x300')
        self.tipo_midia = ('Vídeos', 'Imagem')

        # Caixa de combinação
        self.current_var = tk.StringVar()
        self.lista_de_midias = ttk.Combobox(self.janela_principal, textvariable=self.current_var, justify='center')
        self.lista_de_midias['values'] = self.tipo_midia
        self.lista_de_midias.set('Tipos de arquivos disponível')
        self.lista_de_midias.pack(fill='both', side='top')
        self.lista_de_midias.current()

        self.current_var.trace('w', self.item_selecionado)

        self.botao_limpar = tk.Button(self.janela_principal, text='Limpar', command=self.limpeza)
        self.botao_limpar.pack(side='bottom', padx=5, pady=5)

        self.janela_principal.mainloop()

    def limpeza(self):
        self.lista_de_midias.set('')

    def item_selecionado(self, *args):
        print(self.current_var.get())


iniciando_programa = JanelaTeste()
