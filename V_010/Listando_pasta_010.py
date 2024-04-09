"""#### Declaração de Modulos"""
import tkinter.ttk
import tkinter as tk


class ProgramaPrincipal:
    def __init__(self):
        """# Janela principal"""
        self.janela_principal = tk.Tk()
        self.janela_principal.title('V_010')
        self.janela_principal.geometry('1000x680+150+5')
        self.janela_principal.resizable(0, 0)

        """#### frames"""
        self.frames_superior_01 = tk.Frame(self.janela_principal)
        self.frames_superior_01.pack(anchor='n')

        self.janela_principal.mainloop()


iniciando_obj = ProgramaPrincipal()