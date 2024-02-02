from tkinter import *
from tkinter.ttk import *

contagem = -1
running = False

janela_principal = Tk()
janela_principal.geometry('500x450+400+300')
janela_principal.title('Cronometro')
janela_principal.config(bg='#299617')
janela_principal.resizable(0, 0)

start_botao = Button(janela_principal, text='Start', width=15, command=lambda: iniciando_cronometro())
start_botao.place(x=30, y=390)


def iniciando_cronometro():
    pass


def contagem_label():
    def contagem():
        if running:
            global contagem
            if contagem == -1:
                display = '00'
            else:
                display = str(contagem)
            lbl['text'] = display
            lbl.after(1000, contagem)
            contagem += 1
    contagem()
    

janela_principal.mainloop()
