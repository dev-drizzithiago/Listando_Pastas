from tkinter import *
from tkinter.ttk import *

contagem = -1
running = False


class JanelaTeste:
    def __init__(self):

        def contagem_label():
            def contagem():
                if running:
                    global contagem
                    if contagem == -1:
                        display = '00'
                    else:
                        display = str(contagem)
                    self.lbl['text'] = display
                    self.lbl.after(1000, contagem)
                    contagem += 1
            contagem()

        self.janela_principal = Tk()
        self.janela_principal.geometry('500x500+400+300')
        self.janela_principal.title('Cronometro')
        self.janela_principal.config(bg='#299617')
        self.janela_principal.resizable(0, 0)

        self.lbl = Label(self.janela_principal, text='00')
        self.lbl.place(x=250, y=250)

        self.start_botao = Button(self.janela_principal, text='Start', width=15, command=lambda: self.start)
        self.start_botao.place(x=30, y=330)
        self.stop_botao = Button(self.janela_principal, text='stop', width=15, command='')
        self.stop_botao.place(x=30, y=360)
        self.reset_botao = Button(self.janela_principal, text='Reset', width=15, command='')
        self.reset_botao.place(x=30, y=390)

        self.janela_principal.mainloop()

    def start(self):
        global running
        running = True
        self.contagem_label()
        self.start_botao['state'] = 'disabled'
        self.stop_botao['state'] = 'normal'
        self.reset_botao['state'] = 'normal'

    def stop(self):
        global running
        self.contagem_label()
        self.start_botao['state'] = 'normal'
        self.stop_botao['state'] = 'disabled'
        self.reset_botao['state'] = 'normal'
        running = True

    def reset(self):
        global contagem
        contagem = -1
        if not running:
            self.reset_botao['state'] = 'disabled'
            self.lbl['text'] = '00'
        else:
            self.lbl['text'] = ''


iniciando = JanelaTeste()
