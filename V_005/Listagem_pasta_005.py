import tkinter as tk

class ListagemPasta:
    def __init__(self):
        self.janela_principal = tk.Tk()
        self.janela_principal.geometry('600x300')
        self.janela_principal.title('Versão 5')

        self.frame_principal_01 = tk.Frame(self.janela_principal)
        self.frame_principal_02 = tk.Frame(self.janela_principal)
        self.frame_principal_01.pack()
        self.frame_principal_02.pack()




        self.janela_principa.mainloop()