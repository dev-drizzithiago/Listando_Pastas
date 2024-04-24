import tkinter as tk
from tkinter.ttk import *

dados_do_processo_busca = list()
arquivo_repetido = dict()


def valor_dados_da_busca(valor_busca):
    for item_lista_busca in valor_busca:
        dados_do_processo_busca.insert(item_lista_busca)


def verificaaoo_duplicidade():
    for valor in dados_do_processo_busca:
        valor_item = str(valor).split('|')[1]

        if valor_item in arquivo_repetido:
            arquivo_repetido[valor_item] += 1
        else:
            arquivo_repetido[valor_item] = 1

    for k, v in arquivo_repetido.items():
        if v > 1:
            print(f'Arquivo Repetido: {k} - Quantidade: {v}')
            lista_result_duplicidade.insert('end', f'File: [ {k} ] - QTDS: [ {v} ]')


def opcao_check_botao():
    resposta_move = var_opcao_move.get()
    if resposta_move:
        print('teste mover')

    resposta_delete = var_opcao_delete.get()
    if resposta_delete:
        print('teste delete')


"""#### Janela de opções duplicados; só interno """
janela_opc_duplicidade = tk.Tk()
janela_opc_duplicidade.geometry('1000x600+200+50')
janela_opc_duplicidade.resizable(0, 0)
janela_opc_duplicidade.title('Verificando duplicidade!')

# -=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
"""# Frame Principal DUPLICIDADE"""
frame_label_duplicidade = tk.LabelFrame(janela_opc_duplicidade, text='Verificando duplicidade!')
frame_label_duplicidade.config(width=900, height=580)
frame_label_duplicidade.pack(fill=tk.BOTH, pady=5, padx=5)

# -=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
"""# Lista de resultado dos arquivos duplicados"""
var_result_duplicidade = tk.StringVar()
lista_result_duplicidade = tk.Listbox(frame_label_duplicidade)
lista_result_duplicidade.config(selectmode=tk.SINGLE, width=160, height=15)
lista_result_duplicidade.place(y=3, x=3)

# ______________________________________________________________________________________________________________
"""# Criando a barra de rolagem para lista de resultado"""
barra_rolagem_lista_resultado_ducplicados = Scrollbar(janela_opc_duplicidade)
barra_rolagem_lista_resultado_ducplicados.config(orient='vertical')
barra_rolagem_lista_resultado_ducplicados.place(in_=lista_result_duplicidade)
barra_rolagem_lista_resultado_ducplicados.place(relx=1.0, relheight=1.0)
barra_rolagem_lista_resultado_ducplicados.place(bordermode='outside')
barra_rolagem_lista_resultado_ducplicados.config(command=lista_result_duplicidade.yview)
lista_result_duplicidade.config(yscrollcommand=barra_rolagem_lista_resultado_ducplicados.set)

# -=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
"""Frame Superior duplicidade"""
frame_superior_dupli = tk.Frame(frame_label_duplicidade, bg='#C0C0C0', width=980, height=150)
frame_superior_dupli.place(y=250, x=3)

# ______________________________________________________________________________________________________________
"""# Opcao check movendo os arquivos duplicados"""
var_opcao_move = tk.BooleanVar()
opcao_move = tk.Checkbutton(frame_superior_dupli, text='Mover arquivos duplicados', bg='#C0C0C0')
opcao_move.config(variable=var_opcao_move, pady=5, padx=5, bd=2)
opcao_move.place(y=5, x=5)

# ______________________________________________________________________________________________________________
"""# Opção Deletar arquivos duplicados"""
var_opcao_delete = tk.BooleanVar()
opcao_delete = tk.Checkbutton(frame_superior_dupli, text='Deletar arquivos duplicados', bg='#C0C0C0')
opcao_delete.config(variable=var_opcao_delete, pady=5, padx=5, bd=2)
opcao_delete.place(y=30, x=5)

# -=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
frame_inferior_dupli = tk.Frame(frame_label_duplicidade, bg='#C0C0C0', width=980, height=150)
frame_inferior_dupli.place(y=407, x=3)

# ______________________________________________________________________________________________________________
"""#### Frame botao """
frame_lbl_botao = tk.LabelFrame(frame_inferior_dupli, text='Processar', bg="#C0C0C0", pady=5, padx=5)
frame_lbl_botao.place(y=7, x=5)

# ______________________________________________________________________________________________________________
"""#### Botoes de opcao"""
botao_aplica_opcao_check = tk.Button(frame_lbl_botao, text='Aplicar', bg='#C0C0C0', width=133)
botao_aplica_opcao_check.config(command=opcao_check_botao)
botao_aplica_opcao_check.pack(anchor='center', pady=5, padx=5)

# ______________________________________________________________________________________________________________

""" Responsável por manter a janela de duplicidade ativa (padrão do tkinter)"""
janela_opc_duplicidade.mainloop()
