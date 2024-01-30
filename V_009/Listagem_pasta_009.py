from tkinter import *
from tkinter.ttk import *
from time import sleep
from threading import Thread
from pathlib import Path
from tkinter.simpledialog import askstring

pasta_destino = Path().home()


class ListandoArquivos:
    def __init__(self):
        self.janela_principal = Tk()
        self.janela_principal.title('Versão 009')
        self.janela_principal.geometry('1000x400')

        self.label_frame_geral = LabelFrame(self.janela_principal, text='Janela Principal')
        self.label_frame_geral.pack(fill=BOTH, ipadx=5, ipady=5)

        self.var_label_status_geral = StringVar()
        self.label_status = Label(self.label_frame_geral, text=self.var_label_status_geral.get())
        self.label_status.pack(side='bottom')

        self.label_frame_combo_categora = LabelFrame(self.label_frame_geral)
        self.label_frame_combo_categora.pack(side='top', fill=BOTH)
        self.combo_extensao_categoria = Combobox(self.label_frame_combo_categora)
        self.combo_extensao_categoria.pack(anchor='center', fill='both')

        # Busca Geral
        self.var_lista_busca = StringVar()
        self.label_frame_lista_busca = LabelFrame(self.label_frame_geral, text='Resultado da BUSCA')
        self.label_frame_lista_busca.pack(anchor='center', fill='both')

        self.barra_rolagem_lista_busca_Y = Scrollbar(self.label_frame_lista_busca, orient=VERTICAL)
        self.barra_rolagem_lista_busca_Y.pack(side='right', fill=Y)
        self.barra_rolagem_lista_busca_X = Scrollbar(self.label_frame_lista_busca, orient=HORIZONTAL)
        self.barra_rolagem_lista_busca_X.pack(side='bottom', fill=X)

        self.lista_result_busca = Listbox(self.label_frame_lista_busca, listvariable=self.var_lista_busca.get())
        self.lista_result_busca.pack(anchor='center', fill=BOTH)

        self.barra_rolagem_lista_busca_Y.config(command=self.lista_result_busca.yview)
        self.lista_result_busca.config(yscrollcommand=self.barra_rolagem_lista_busca_Y.set)

        self.barra_rolagem_lista_busca_X.config(command=self.lista_result_busca.yview)
        self.lista_result_busca.config(xscrollcommand=self.barra_rolagem_lista_busca_X.set)

        # Botoes
        self.label_frame_botoes_opcoes = LabelFrame(self.label_frame_geral, text='Escolha um opção')
        self.label_frame_botoes_opcoes.pack(side='bottom', fill='both')

        self.botao_iniciar_busca = Button(self.label_frame_botoes_opcoes, text='Iniciar Busca', command=self.thread_botao_iniciar)
        self.botao_iniciar_busca.pack(anchor='center')
        self.botao_escolha_extensao = Button(self.label_frame_botoes_opcoes, text='Escolha um arquivo', command=self.thread_botao_extensao)
        self.botao_escolha_extensao.pack(anchor='sw', ipady=5, ipadx=5)

        # Barro de progresso
        self.label_frame_progresso = LabelFrame(self.label_frame_geral, text='Progresso da busca...!')
        self.label_frame_progresso.pack(side='bottom', fill='both')
        self.barra_progresso_busca = Progressbar(self.label_frame_progresso, orient=HORIZONTAL)
        self.barra_progresso_busca.pack(anchor='center', fill='both', pady=3, padx=3)

        self.janela_principal.mainloop()

    def thread_botao_iniciar(self):
        Thread(target=self.iniciar_busca).start()

    def thread_botao_extensao(self):
        Thread(target=self.digitar_extensao()).start()

    def digitar_extensao(self):
        self.extensao_selecao = askstring('AVISO', 'Digite um Extensão')
        self.thread_botao_iniciar()

    def iniciar_busca(self):
        self.label_status['text'] = 'Iniciando busca'
        sleep(1)
        self.barra_progresso_busca.start()
        valor_da_busca = self.extensao_selecao
        for busca in pasta_destino.glob('**/*' + valor_da_busca):
            self.label_status.config(text='Processando, aguarde...!')
            self.lista_result_busca.insert('end', busca)
        self.barra_progresso_busca.stop()
        self.label_status['text'] = 'Busca Finalizada!'


obj_start = ListandoArquivos()
