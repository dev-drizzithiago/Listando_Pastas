from tkinter import *

tk = Tk()

var = []
buttons = []
k = 0


def delHist():
    for i in range(len(var)):
        if var[i].get() == 1:
            print(buttons[i]['text'])


for i in 'abcde':
    var.append(IntVar())
    buttons.append(Checkbutton(tk, text=i[0], variable=var[k], wraplength=500))
    buttons[-1].pack()
    k += 1

Button(text='delHist', command=delHist).pack()
