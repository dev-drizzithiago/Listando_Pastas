from tkinter.ttk import *
from tkinter import *
import time

ws = Tk()
ws.title('PythonGuides')
ws.geometry('400x250+1000+300')


def step():
    for i in range(5):
        ws.update_idletasks()
        pb1['value'] += 20

        time.sleep(1)


pb1 = Progressbar(ws, orient=HORIZONTAL, length=100, mode='indeterminate')
pb1.pack(expand=True)

Button(ws, text='Start', command=step).pack()

ws.mainloop()