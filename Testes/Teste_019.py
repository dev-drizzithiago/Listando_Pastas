from tkinter import *

tk = Tk()
tk.geometry('400x400')

var = []
buttons = []
k = 0
colunas = 1
linhas = 25

AUDIO = ['teste1', 'teste2', 'teste3', 'teste4', 'teste5',
         'teste6', 'teste7', 'teste8', 'teste9', 'teste10', 'Final']


def delHist():
    for i in range(len(var)):
        if var[i].get() == 1:
            print(buttons[i]['text'])


for i in AUDIO:
    var.append(IntVar())
    buttons.append(Checkbutton(tk, text=i, variable=var[k], wraplength=500))
    buttons[-1].place(y=linhas, x=colunas)
    k += 1

    if linhas == 110:
        linhas = 25
        colunas += 85
    else:
        linhas += 17

Button(text='delHist', command=delHist).pack()

tk.mainloop()
