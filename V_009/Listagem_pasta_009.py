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

        self.var_lista_busca = StringVar()
        self.label_frame_lista_busca = LabelFrame(self.janela_principal, text='Resultado da BUSCA')
        self.label_frame_lista_busca.pack(anchor='center')
        self.lista_result_busca = Listbox(self.label_frame_lista_busca, listvariable=self.var_lista_busca.get())
        self.lista_result_busca.pack(anchor='center')

        self.janela_principal.mainloop()

    def thread_botao_iniciar(self):
        Thread(target=self.iniciar_busca).start()

    def iniciar_busca(self):
        soma = 0
        self.label_status['text'] = 'Iniciando busca'
        sleep(2)
        for conta in range(1, 10):
            soma += 1
            self.lista_result_busca.insert('end', soma)
            sleep(1)
        self.label_status['text'] = 'Busca Finalizada!'


obj_start = ListandoArquivos()
