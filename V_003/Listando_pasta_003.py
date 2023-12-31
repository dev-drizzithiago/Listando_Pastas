from pathlib import Path
import tkinter as tk
from tkinter.messagebox import showinfo, showerror, showwarning

home = Path.home()

pasta_busca = Path(home)


class JanelaTK:
    def __init__(self):
        self.extensoes = ['all', 'jpg', 'mp4', 'txt']
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

        self.botao_entrar = tk.Button(self.frame_botao_001, text='Entrar', command=self.item_selecionado)
        self.botao_entrar.pack(anchor='s')

        self.var_extersao = tk.Variable(value=self.extensoes)

        self.lista_arqs = tk.Listbox(self.frame_txt_02, listvariable=self.var_extersao, selectmode=tk.EXTENDED)
        self.lista_arqs.pack(anchor='s')

        self.janela_principal.mainloop()

    def item_selecionado(self):
        selecao = self.lista_arqs.curselection()
        print(len(selecao))
        print(selecao)
        if selecao == 0:
            tk.messagebox.showinfo('AVISO!!', f'{self.extensoes[0]}')
        elif selecao == 1:
            tk.messagebox.showinfo('AVISO!!', f'{self.extensoes[1]}')
        elif selecao == 2:
            tk.messagebox.showinfo('AVISO!!', f'{self.extensoes[2]}')
        elif selecao == 3:
            tk.messagebox.showinfo('AVISO!!', f'{self.extensoes[3]}')

        self.janela_principal.mainloop()


obj_janela_busca = JanelaTK()


def busca_pasta():
    for listagem in pasta_busca.glob('**/*'):
        # print(listagem)
        if listagem.is_file():
            print(listagem)
