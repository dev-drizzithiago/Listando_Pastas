from tkinter import *
from tkinter.ttk import *
from datetime import datetime
from tkinter.simpledialog import *
from tkinter.messagebox import *

valor_hora = datetime.now()
data_certa = valor_hora.strftime('%D/%M/%Y')
hora_certa = valor_hora.strftime('%H:%M')


class ListandoPastas:
    def __init__(self):

        # janela princpal
        janela_principal = Tk()
        janela_principal.geometry('350x390')
        janela_principal.config(padx=5, pady=5)

        # Relogio
        label_frame_relogio = LabelFrame(janela_principal, text='Hora Certa')
        label_frame_relogio.pack(anchor='center')
        label_hora = Label(label_frame_relogio, text=f'{data_certa} - {hora_certa}')
        label_hora.pack(anchor='center')

        janela_principal.mainloop()


obj_principal = ListandoPastas()
