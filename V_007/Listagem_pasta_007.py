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

        self.label_titulo_principal = Label(self.janela_principal, text='MERCURTY TI', justify='center')
        self.label_titulo_principal.pack(side='top', fill='both')

        # Lista Combo
        self.var_cambo = StringVar()
        self.combo_tipo_arquivo = Combobox(self.janela_principal, textvariable=self.var_cambo, justify='center')
        self.combo_tipo_arquivo['values'] = self.lista_tipos_extensoes
        self.combo_tipo_arquivo.set('Escolha um tipo de Mídia')
        self.combo_tipo_arquivo.pack(side='top', fill='both')
        self.combo_tipo_arquivo.current()
        self.var_cambo.trace('w', self.opcao_midia)

        self.janela_principal.mainloop()

    def opcao_midia(self, *args):
        print(self.combo_tipo_arquivo.get())

obj_principal = ListagemPastas()
