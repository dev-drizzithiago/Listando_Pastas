from pathlib import Path
import tkinter as tk
from tkinter.messagebox import showinfo, showerror, showwarning

home = Path.home()

pasta_busca = Path(home)


class JanelaTK:
    def __init__(self):
        self.janela_principal = tk.Tk()
        self.janela_principal.geometry('600x400')

        self.frame_txt_01 = tk.Frame(self.janela_principal)
        self.frame_txt_01.pack()
        self.frame_txt_02 = tk.Frame(self.janela_principal)
        self.frame_txt_02.pack()
        self.frame_botao_001 = tk.Frame(self.janela_principal)
        self.frame_botao_001.pack()

        caixa_entrada = tk.Label(self.janela_principal, text="Escolha uma extensão de arquivo")
        caixa_entrada.pack(anchor='n')

        self.botao_entrar = tk.Button(self.frame_botao_001, text='Entrar', command=self.mensagem)
        self.botao_entrar.pack(anchor='s')

        self.lista_arqs = tk.Listbox(self.frame_txt_02)
        self.lista_arqs.insert(1, 'JPG')
        self.lista_arqs.insert(2, 'MP4')
        self.lista_arqs.insert(3, 'TXT')
        self.lista_arqs.pack(anchor='center')
        self.janela_principal.mainloop()

    def mensagem(self):
        msg = self.lista_arqs.get(1, 3)
        tk.messagebox.showinfo('AVISO!', msg)


obj_janela = JanelaTK()

for listagem in pasta_busca.glob('**/*.in'):
    # print(listagem)
    if listagem.is_file():
        print(listagem)
