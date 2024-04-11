from tkinter import *

tk = Tk()

var = []
buttons = []
k = 0

AUDIO = ['teste1', 'teste2', 'teste3', 'teste4', 'teste5',
         'teste6', 'teste7', 'teste8', 'teste9', 'teste10', 'Final']


def delHist():
    for i in range(len(var)):
        if var[i].get() == 1:
            print(buttons[i]['text'])


for i in AUDIO:
    var.append(IntVar())
    buttons.append(Checkbutton(tk, text=i, variable=var[k], wraplength=500))
    buttons[-1].pack()
    k += 1

Button(text='delHist', command=delHist).pack()

tk.mainloop()
