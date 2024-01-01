from tkinter.filedialog import askopenfilename
import tkinter as tk
from time import sleep

class ListandoPastas:
    def __init__(self):
        # Janela principal
        self.janela_principal = tk.Tk()
        self.janela_principal.geometry('300x300')
        self.janela_principal.title(f'Buscando arquivos em na pasta {self.pasta_destino}')

