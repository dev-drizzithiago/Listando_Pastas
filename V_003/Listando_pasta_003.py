from pathlib import Path
import tkinter as tk

home = Path.home()

pasta_busca = Path(home)


class JanelaTK:
    def __init__(self):
        janela_principal = tk.Tk()
        frame_txt_01 = tk.Frame(janela_principal)
        frame_txt_01.pack()
        frame_txt_02 = tk.Frame(janela_principal)
        frame_txt_02.pack()
        caixa_entrada = tk.Label(janela_principal, text="Escolha uma extensão de arquivo")
        caixa_entrada.pack()

        lista_arqs = tk.Listbox(frame_txt_02)
        lista_arqs.insert(1,'JPG')
        lista_arqs.insert(2, 'MP4')
        lista_arqs.insert(3,'TXT')
        lista_arqs.pack(side='topdw')
        janela_principal.mainloop()


obj_janela = JanelaTK()

for listagem in pasta_busca.glob('**/*'):
    # print(listagem)
    if listagem.is_file():
        print(listagem)
