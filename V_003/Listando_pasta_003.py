from pathlib import Path
import tkinter as tk

home = Path.home()

pasta_busca = Path(home)


class JanelaTK:
    def __init__(self):
        janela_principal = tk.Tk()
        frame_txt_01 = tk.Frame(janela_principal)
        frame_txt_01.pack()
        caixa_entrada = tk.Label(janela_principal, text="Digita uma extensão de arquivo")
        caixa_entrada.pack()
        janela_principal.mainloop()


obj_janela = JanelaTK()

for listagem in pasta_busca.glob('**/*'):
    # print(listagem)
    if listagem.is_file():
        print(listagem)
