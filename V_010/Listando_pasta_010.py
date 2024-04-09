"""#### Declaração de Modulos"""
from tkinter.ttk import *
import tkinter as tk

"""# Modeulo THREAD"""
from threading import Thread


class ProgramaPrincipal:
    def __init__(self):
        """# Janela principal"""
        self.janela_principal = tk.Tk()
        self.janela_principal.title('V_010')
        self.janela_principal.config(bg='#DCDCDC')
        self.janela_principal.geometry('1000x680+150+5')
        self.janela_principal.resizable(0, 0)

        """#### LabelFrame Principal"""
        self.label_frame_principal = tk.LabelFrame(self.janela_principal)
        self.label_frame_principal.config(text='Bem vindo ao buscador de arquivos!')
        self.label_frame_principal.config(bg='#DCDCDC')
        self.label_frame_principal.config(width=910, height=650)
        self.label_frame_principal.place(y=5, x=45)
        # -=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
        """#### frames"""
        """# Frame SUPERIOR: Responsavel por mostrar as opções de buscas"""
        self.frames_superior = tk.Frame(self.janela_principal, bg='#A9A9A9')
        self.frames_superior.config(width=900, height=200)
        self.frames_superior.config(bd=2)
        self.frames_superior.place(y=20, x=50)
        # ______________________________________________________________________________________________________________
        """COMBO BOX"""
        self.var_combo_box_categoria = tk.StringVar()
        self.combo_box_cat = Combobox(self.frames_superior)
        self.combo_box_cat.place(y=3, x=10)
        self.combo_box_cat.config(textvariable=self.var_combo_box_categoria.get)
        self.combo_box_cat.config(values=['teste1', 'teste2'])
        self.combo_box_cat.set('Escolha uma categoria')
        self.var_combo_box_categoria.trace('w', self.selecao_combo_extensao)

        # -=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
        """# Frame Central: Reposanvel por mostrar o resultado da busca"""
        self.frames_central = tk.Frame(self.janela_principal, bg='#C0C0C0')
        self.frames_central.config(width=900, height=200)
        self.frames_central.config(bd=2)
        self.frames_central.place(y=230, x=50)

        # -=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
        """# Frame Inferior: Responsável por registro das informações de busca"""
        self.frames_inferior = tk.Frame(self.janela_principal, bg='#D3D3D3')
        self.frames_inferior.config(width=900, height=200)
        self.frames_inferior.config(bd=2)
        self.frames_inferior.place(y=440, x=50)

        self.janela_principal.mainloop()

    def selecao_combo_extensao(self, *args):
        valor_categoria_extensao = self.var_combo_box_categoria.get()
        print(valor_categoria_extensao)


iniciando_obj = ProgramaPrincipal()
