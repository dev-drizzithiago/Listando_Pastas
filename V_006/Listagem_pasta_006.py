import tkinter as tk
from tkinter import ttk

class JanelaTeste:
    def __init__(self):
        self.janela_principal = tk.Tk
        self.janela_principal.geometry('300x300')
        self.tipo_midia = ('Vídes', 'Imagem')

# Caixa de combinação
        self.current_var = tk.StringVar()
        self.current_var.get()
        self.current_var.set(value=self.tipo_midia)
        self.lista_de_midias = ttk.Combobox(self.janela_principal, textvariable=self.current_var, justify='center')
        self.lista_de_midias['values'] = self.tipo_midia
        self.lista_de_midias.set('Tipos de arquivos disponível')
        self.lista_de_midias.pack(fill='both', side='top')
        self.lista_de_midias.current()