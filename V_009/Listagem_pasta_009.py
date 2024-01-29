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

        self.botao_iniciar_busca = Button(self.label_frame_geral, text='Iniciar Busca', command=self.thread_botao_iniciar)
        self.botao_iniciar_busca.pack(anchor='center')

        self.var_label_status_geral = StringVar()
        self.label_status = Label(self.label_frame_geral, text=self.var_label_status_geral.get())
        self.label_status.pack(side='bottom')

        self.janela_principal.mainloop()

    def thread_botao_iniciar(self):
        Thread(target=self.iniciar_busca).start()

    def iniciar_busca(self):
        self.label_status['text'] = 'Iniciando busca'
        sleep(1)
        for valor in range(1, 10):
            self.label_status['text'] = valor
            sleep(1)
        self.label_status['text'] = 'Busca Finalizada!'


obj_start = ListandoArquivos()
