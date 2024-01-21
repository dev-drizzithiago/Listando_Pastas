import tkinter as tk


class Teste_002:
    def __init__(self):
        self.janela_princial = tk.Tk()
        self.janela_princial.geometry('300x300')
        self.frame_001 = tk.Frame(self.janela_princial)
        self.frame_001.pack(fill='both')
        self.var_label = tk.StringVar()
        self.label_001 = tk.Label(self.frame_001, textvariable=self.var_label.get(), border=5)
        self.label_001.pack(fill='both')

        botao_atualizacao = tk.Button(self.frame_001, text='Atualizar', command=self.atualizar)
        botao_atualizacao.pack()

        self.janela_princial.mainloop()

    def atualizar(self):
        self.var_label.set('teste')


obj_iniciar = Teste_002()
