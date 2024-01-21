import tkinter as tk

janela_princial = tk.Tk()
janela_princial.geometry('300x300')
frame_001 = tk.Frame(janela_princial)
frame_001.pack(fill='both')
var_label = tk.StringVar
label_001 = tk.Label(frame_001, textvariable=var_label.get, border=5)
label_001.pack(fill='both')

botao_atualizacao = tk.Button(frame_001, text='Atualizar')
botao_atualizacao.pack()


janela_princial.mainloop()
