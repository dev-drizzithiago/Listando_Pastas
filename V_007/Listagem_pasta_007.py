from tkinter import *
from tkinter.ttk import *


class ListagemPastas:
    def __init__(self):
        # Varias Global
        self.lista_tipos_extensoes = ('VÍDEOS', 'IMAGENS', 'ARQUIVOS_TXT')

        # Janela principa
        self.janela_principal = Tk()
        self.janela_principal.geometry('300x390')
        self.janela_principal.title('V_007')
        self.janela_principal.resizable(False, False)

        # Label Frame
        self.label_frame_001 = Frame(self.janela_principal)
        self.label_frame_002 = Frame(self.janela_principal)
        self.label_frame_003 = Frame(self.janela_principal)
        self.label_frame_004 = Frame(self.janela_principal)
        self.label_frame_001.pack()
        self.label_frame_002.pack()

        # Lista Combo
        self.var_cambo = StringVar()
        self.combo_tipo_arquivo = Combobox(self.janela_principal)
        self.combo_tipo_arquivo.pack(side='top', fill='both')

        self.janela_principal.mainloop()


obj_principal = ListagemPastas()
