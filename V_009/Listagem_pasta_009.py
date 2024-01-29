from tkinter import *
from tkinter.ttk import *
from time import sleep
from threading import Thread


class ListandoArquivos:
    def __init__(self):
        self.janela_principal = Tk()
        self.janela_principal.title('Versão 009')
        self.janela_principal.geometry('400x400')

        self.label_frame_geral = LabelFrame(self.janela_principal, text='Janela Principal')
        self.label_frame_geral.pack(fill=BOTH, ipadx=5, ipady=5)

        self.botao_iniciar_busca = Button(self.label_frame_geral, text='Iniciar Busca', command=self.iniciar_busca)
        self.botao_iniciar_busca.pack(anchor='center')

        self.janela_principal.mainloop()

    def thread_botao_iniciar(self):
        Thread(target=self.iniciar_busca()).start()

    def iniciar_busca(self):
        print('iniciando a busca')
        for valor in range(1, 10):
            print(valor)
            sleep(1)
        print('Busca fincalizada')


obj_start = ListandoArquivos()