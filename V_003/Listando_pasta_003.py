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

        self.botao_entrar = tk.Button(self.frame_botao_001, text='Entrar', command=self.mensagem)
        self.botao_entrar.pack(anchor='s')

        self.lista_arqs = tk.Listbox(self.frame_txt_02)
        self.lista_arqs.insert(1, 'JPG')
        self.lista_arqs.insert(2, 'MP4')
        self.lista_arqs.insert(3, 'TXT')
        self.lista_arqs.insert(0, 'ALL')
        self.lista_arqs.pack(anchor='center')
        self.janela_principal.mainloop()

    def mensagem(self):
        msg = self.lista_arqs.curselection()
        print(len(msg))
        if msg == 0:
            self.lista_arqs = ''
            tk.messagebox.showinfo('AVISO!', f'Você escolhei a extesão: {msg}')
            return self.lista_arqs
        elif msg == 1:
            self.arq_busca = '.jpg'
            tk.messagebox.showinfo('AVISO!', f'Você escolhei a extesão: {msg}')
            return self.lista_arqs
        elif msg == 2:
            self.arq_busca = '.mp4'
            tk.messagebox.showinfo('AVISO!', f'Você escolhei a extesão: {msg}')
            return self.lista_arqs
        elif msg == 3:
            self.arq_busca = '.txt'
            tk.messagebox.showinfo('AVISO!', f'Você escolhei a extesão: {msg}')
            return self.lista_arqs
        self.janela_principal.destroy()

    def busca_pasta(self):
        for listagem in pasta_busca.glob('**/*' + self.mensagem):
            # print(listagem)
            if listagem.is_file():
                print(listagem)


obj_janela_busca = JanelaTK()


