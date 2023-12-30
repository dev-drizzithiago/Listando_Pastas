from pathlib import Path
import tkinter as tk

home = Path.home()

pasta_busca = Path(home)


class JanelaTK:
    def __init__(self):
        janela_principal = tk.Tk()
        frame__01 = tk.Frame(janela_principal)
        janela_principal.mainloop()


obj_janela = JanelaTK()

for listagem in pasta_busca.glob('**/*'):
    # print(listagem)
    if listagem.is_file():
        print(listagem)
