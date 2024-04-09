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
        """# Frame SUPERIOR: Responsavel por mostrar as opções de buscas"""
        self.frames_superior = tk.Frame(self.janela_principal, bg='green')
        self.frames_superior.config(width=900, height=200)
        self.frames_superior.place(y=20, x=50)

        """# Frame Central: Reposanvel por mostrar o resultado da busca"""
        self.frames_central = tk.Frame(self.janela_principal, bg='black')
        self.frames_central.config(width=900, height=200)
        self.frames_central.place(y=230, x=50)

        """# Frame Inferior: Responsável por registro das informações de busca"""
        self.frames_inferior = tk.Frame(self.janela_principal, bg='blue')
        self.frames_inferior.config(width=900, height=200)
        self.frames_inferior.place(y=450, x=50)


        self.janela_principal.mainloop()


iniciando_obj = ProgramaPrincipal()