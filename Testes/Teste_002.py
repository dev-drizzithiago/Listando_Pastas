import tkinter as tk


class Teste_002:
    def __init__(self):
        self.janela_princial = tk.Tk()

        self.janela_princial.geometry('300x300')
        self.frame_001 = tk.Frame(self.janela_princial, bg='green')
        self.frame_001.pack(fill='both')
        self.frame_002 = tk.Frame(self.janela_princial, bg='blue')
        self.frame_002.pack(fill=tk.BOTH)

        self.var_label = tk.StringVar()
        self.var_label.set('teste')
        self.label_001 = tk.Label(self.frame_001, text=self.var_label.get(), border=1, bd=5)
        self.label_001.pack(fill='both', pady=5, padx=5)

        botao_atualizacao = tk.Button(self.frame_002, text='Atualizar', command=self.atualizar)
        botao_atualizacao.pack()

        self.janela_princial.mainloop()

    def atualizar(self):
        self.var_label.set('teste1')


obj_iniciar = Teste_002()
