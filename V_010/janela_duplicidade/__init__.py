import tkinter as tk
from tkinter.ttk import *
from threading import Thread

dados_do_processo_busca = list()
arquivo_repetido = dict()

lista_teste_1 = ['SCREENSHOT_20220725-085708.PNG',
                 'SCREENSHOT_20220725-224021.PNG',
                 'SCREENSHOT_20220727-080238.PNG',
                 'SCREENSHOT_20220728-120141.PNG',
                 'SCREENSHOT_20220729-123824.PNG',
                 'SCREENSHOT_20220731-111027.PNG',
                 'SCREENSHOT_20220725-085708.PNG',
                 'SCREENSHOT_20220725-224021.PNG',
                 'SCREENSHOT_20220727-080238.PNG',
                 'SCREENSHOT_20220728-120141.PNG',
                 'SCREENSHOT_20220729-123824.PNG',
                 'SCREENSHOT_20220731-111027.PNG'
                 ]

class JanelaDuplicados:
    def __init__(self):
        # -=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
        # -=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
        """#### Janela de opções duplicados; só interno """
        self.janela_opc_duplicidade = tk.Tk()
        self.janela_opc_duplicidade.geometry('1000x600+200+50')
        self.janela_opc_duplicidade.resizable(0, 0)
        self.janela_opc_duplicidade.title('Verificando duplicidade!')

        # ______________________________________________________________________________________________________________
        """# Frame Principal DUPLICIDADE"""
        self.frame_label_duplicidade = tk.LabelFrame(self.janela_opc_duplicidade, text='Verificando duplicidade!')
        self.frame_label_duplicidade.config(width=900, height=580)
        self.frame_label_duplicidade.pack(fill=tk.BOTH, pady=5, padx=5)

        # ______________________________________________________________________________________________________________
        """# Lista de resultado dos arquivos duplicados"""
        self.var_result_duplicidade = tk.StringVar()
        self.lista_result_duplicidade = tk.Listbox(self.frame_label_duplicidade)
        self.lista_result_duplicidade.config(selectmode=tk.SINGLE, width=160, height=15)
        self.lista_result_duplicidade.place(y=3, x=3)

        # ______________________________________________________________________________________________________________
        """# Criando a barra de rolagem para lista de resultado"""
        self.barra_rolagem_lista_resultado_ducplicados = Scrollbar(self.janela_opc_duplicidade)
        self.barra_rolagem_lista_resultado_ducplicados.config(orient='vertical')
        self.barra_rolagem_lista_resultado_ducplicados.place(in_=self.lista_result_duplicidade)
        self.barra_rolagem_lista_resultado_ducplicados.place(relx=1.0, relheight=1.0)
        self.barra_rolagem_lista_resultado_ducplicados.place(bordermode='outside')
        self.barra_rolagem_lista_resultado_ducplicados.config(command=self.lista_result_duplicidade.yview)
        self.lista_result_duplicidade.config(yscrollcommand=self.barra_rolagem_lista_resultado_ducplicados.set)

        # ______________________________________________________________________________________________________________
        """Frame Superior duplicidade"""
        self.frame_superior_dupli = tk.Frame(self.frame_label_duplicidade, bg='#C0C0C0', width=980, height=150)
        self.frame_superior_dupli.place(y=250, x=3)

        # ______________________________________________________________________________________________________________
        """# Opcao check movendo os arquivos duplicados"""
        self.var_opcao_move = tk.BooleanVar()
        self.opcao_move = tk.Checkbutton(self.frame_superior_dupli, text='Mover arquivos duplicados', bg='#C0C0C0')
        self.opcao_move.config(variable=self.var_opcao_move, pady=5, padx=5, bd=2)
        self.opcao_move.place(y=5, x=5)

        # ______________________________________________________________________________________________________________
        """# Opção Deletar arquivos duplicados"""
        self.var_opcao_delete = tk.BooleanVar()
        self.opcao_delete = tk.Checkbutton(self.frame_superior_dupli, text='Deletar arquivos duplicados', bg='#C0C0C0')
        self.opcao_delete.config(variable=self.var_opcao_delete, pady=5, padx=5, bd=2)
        self.opcao_delete.place(y=30, x=5)

        # ______________________________________________________________________________________________________________
        self.frame_inferior_dupli = tk.Frame(self.frame_label_duplicidade, bg='#C0C0C0', width=980, height=150)
        self.frame_inferior_dupli.place(y=407, x=3)

        # ______________________________________________________________________________________________________________
        """#### Frame botao """
        self.frame_lbl_botao = tk.LabelFrame(self.frame_inferior_dupli, text='Processar', bg="#C0C0C0", pady=5, padx=5)
        self.frame_lbl_botao.place(y=7, x=5)

        # ______________________________________________________________________________________________________________
        """#### Botoes de opcao"""
        self.botao_aplica_opcao_check = tk.Button(self.frame_lbl_botao, text='Aplicar', bg='#C0C0C0', width=133)
        self.botao_aplica_opcao_check.config(command=self.thread_opcao_check_botao)
        self.botao_aplica_opcao_check.pack(anchor='center', pady=5, padx=5)

        # ______________________________________________________________________________________________________________

        """ Responsável por manter a janela de duplicidade ativa (padrão do tkinter)"""
        self.janela_opc_duplicidade.mainloop()
        # ______________________________________________________________________________________________________________
        # ______________________________________________________________________________________________________________
    """#### Valor entra direto na função abaixo"""
    def valor_dados_da_busca(self, valor_busca):
        print(valor_busca)
        for item_lista_busca in valor_busca:
            dados_do_processo_busca.insert(item_lista_busca)
        print(dados_do_processo_busca)
    # ______________________________________________________________________________________________________________

    """#### Threads do modulo"""
    def thread_opcao_check_botao(self):
        print('Iniciando thread "opcao_check_botao"')
        Thread(target=self.opcao_check_botao).start()
    # ______________________________________________________________________________________________________________

    """#### Funçao responsável por mostra os dados para o usuário"""
    def verificaaoo_duplicidade(self):
        for valor in dados_do_processo_busca:
            valor_item = str(valor).split('|')[1]

            if valor_item in arquivo_repetido:
                arquivo_repetido[valor_item] += 1
            else:
                arquivo_repetido[valor_item] = 1

        for k, v in arquivo_repetido.items():
            if v > 1:
                print(f'Arquivo Repetido: {k} - Quantidade: {v}')
                self.lista_result_duplicidade.insert('end', f'File: [ {k} ] - QTDS: [ {v} ]')

    # ______________________________________________________________________________________________________________
    """#### Opções para serem realizar alguns processos. """
    def opcao_check_botao(self):
        resposta_move = self.var_opcao_move.get()
        if resposta_move:
            print('teste mover')

        resposta_delete = self.var_opcao_delete.get()
        if resposta_delete:
            print('teste delete')

obj_inicio = JanelaDuplicados()
