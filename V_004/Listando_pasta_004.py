from tkinter.filedialog import askopenfilename
from pathlib import Path
from time import sleep
import tkinter as tk


class ListandoPastas:
    def __init__(self):
        # Janela principal
        self.janela_principal = tk.Tk()
        self.janela_principal.geometry('300x300')
        self.janela_principal.title('Buscando arquivos em na pasta')

        # Frames
        self.frame_label_001 = tk.LabelFrame(self.janela_principal, text='Escolha uma opção')
        self.frame_label_001.pack(anchor='center', fill='both')

        self.janela_principal.mainloop()


obj_listando_pasta = ListandoPastas()