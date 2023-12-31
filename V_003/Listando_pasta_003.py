from pathlib import Path
import tkinter as tk
from tkinter.messagebox import showinfo, showerror, showwarning

home = Path.home()

pasta_busca = Path(home)


class JanelaTK:
    def __init__(self):
        self.extensoes = ['TUDO', 'JPG', 'MP4', 'TXT']
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
        selecao = self.lista_arqs.curselection()  # Tupla
        for extensao in selecao:
            if len(extensao) == 0:
                self.opcao_arquivo = ''
            else:
                self.opcao_arquivo = self.extensoes[extensao]
            tk.messagebox.showinfo('AVISO!!', self.opcao_arquivo)
            self.busca_pasta()

    def busca_pasta(self):
        print('inciando busca...')
        print('Buscando arquivos ', self.opcao_arquivo)
        for listagem in pasta_busca.glob('**/*' + self.opcao_arquivo):
            # print(listagem)
            if listagem.is_file():
                print(listagem)
        print('\nBusca finalizada!')


obj_janela_busca = JanelaTK()
