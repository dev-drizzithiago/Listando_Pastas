from tkinter.filedialog import askopenfilename
from pathlib import Path
from time import sleep
import tkinter as tk


class ListandoPastas:
    def __init__(self):
        # Janela principal
        self.janela_principal = tk.Tk()
        self.janela_principal.geometry('300x300')
        self.janela_principal.title('Buscando arquivos...')

        # Frames Label
        self.frame_label_001 = tk.LabelFrame(self.janela_principal, text='Arquivos Disponível')
        self.frame_label_002 = tk.LabelFrame(self.janela_principal, text='Botões')
        self.frame_label_001.pack(fill='both')
        self.frame_label_002.pack(fill='both')

        # Frames
        self.frame_txt_001 = tk.Frame(self.frame_label_001)
        self.frame_txt_002 = tk.Frame(self.frame_label_001)
        self.frame_txt_001.pack(side='top')
        self.frame_txt_002.pack(side='bottom')

        # Botoes
        self.botao_entrar = tk.Button(self.frame_label_002, text='Entrar')
        self.botao_entrar.pack(side='right')





        self.janela_principal.mainloop()


obj_listando_pasta = ListandoPastas()