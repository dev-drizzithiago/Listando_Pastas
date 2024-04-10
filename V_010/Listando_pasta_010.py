"""#### Declaração de Modulos"""
from tkinter.ttk import *
import tkinter as tk

"""# Modeulo THREAD"""
from threading import Thread


class ProgramaPrincipal:
    def __init__(self):
        """##### Declarações de variaveis"""
        tipos_categorias = ['AUDIO', 'VIDEOS', 'TEXTOS', 'IMAGEM', 'ARQUIVOS', 'ACCESS', 'WORD', 'POWERPOINT',
                            'POWERPOINT', 'EXCEL', 'HTML']

        """# Janela principal"""
        self.janela_principal = tk.Tk()
        self.janela_principal.title('V_010')
        self.janela_principal.config(bg='#DCDCDC')
        self.janela_principal.geometry('1000x680+150+5')
        self.janela_principal.resizable(0, 0)

        """#### LabelFrame Principal"""
        self.label_frame_principal = tk.LabelFrame(self.janela_principal)
        self.label_frame_principal.config(text='Bem vindo ao buscador de arquivos!')
        self.label_frame_principal.config(bg='#DCDCDC')
        self.label_frame_principal.config(width=910, height=650)
        self.label_frame_principal.place(y=5, x=45)
        # -=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
        """#### frames"""
        """# Frame SUPERIOR: Responsavel por mostrar as opções de buscas"""
        self.frames_superior = tk.Frame(self.janela_principal, bg='#696969')
        self.frames_superior.config(width=900, height=200)
        self.frames_superior.place(y=20, x=50)
        # ______________________________________________________________________________________________________________
        """COMBO BOX"""
        self.var_combo_box_categoria = tk.StringVar()
        self.combo_box_cat = Combobox(self.frames_superior)
        self.combo_box_cat.pack(anchor='n')
        self.combo_box_cat.config(textvariable=self.var_combo_box_categoria, width=145)
        self.combo_box_cat.config(values=tipos_categorias, justify='center')
        self.combo_box_cat.set('Escolha uma categoria')
        self.var_combo_box_categoria.trace('w', self.selecao_combo_extensao)

        # -=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
        """# Frame Central: Reposanvel por mostrar o resultado da busca"""
        self.frames_central = tk.Frame(self.janela_principal, bg='#C0C0C0')
        self.frames_central.config(width=900, height=200)
        self.frames_central.config(bd=2)
        self.frames_central.place(y=230, x=50)
        # ______________________________________________________________________________________________________________
        """#### Labels"""
        """# Label teste"""
        self.var_lbl_ext_cat = tk.StringVar()
        self.label_ext_cat = tk.Label(self.frames_central, text=self.var_lbl_ext_cat)
        self.label_ext_cat.config(text='Aguardado informações', bg='#C0C0C0')
        self.label_ext_cat.place(y=1, x=10)
        # ______________________________________________________________________________________________________________
        """# Lista de busca"""
        self.var_lista_result_busca = tk.IntVar()
        self.lista_de_result_busca = tk.Listbox(self.frames_central, width=145, height=5)
        self.lista_de_result_busca.place(y=20, x=10)

        # -=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
        """# Frame Inferior: Responsável por registro das informações de busca"""
        self.frames_inferior = tk.Frame(self.janela_principal, bg='#A9A9A9')
        self.frames_inferior.config(width=900, height=200)
        self.frames_inferior.config(bd=2)
        self.frames_inferior.place(y=440, x=50)

        self.janela_principal.mainloop()

    def selecao_combo_extensao(self, *args):
        tipos_de_extensoes = dict(
            AUDIO=['aac', 'adt', 'adts', 'cda', 'm4a', 'mp3', 'wav', 'aif', 'aifc', 'aiff', 'mid', 'midi'],
            VIDEOS=['flv', 'mov', 'mp4', 'mpeg', 'mpg', 'vob', 'wmv', 'IFF'   'AVI'  'ASF', 'DVR-MS', 'MOV', 'MPEG-2',
                    'Ogg', 'OGM', 'RealMedia', 'Matroska', 'MKV', '3gp', 'VOB'],
            TEXTOS=['pdf', 'rtf', 'wbk', 'wpd', 'wp5', 'txt', 'log', 'xml'],
            IMAGEM=['ai', 'art', 'blend', 'bmp', 'cdr', 'cgm', 'cin', 'cpt', 'dpx', 'dxf', 'dwg', 'eps', 'emf', 'exr',
                    'fla', 'swf', 'fpx', 'gif', 'iff', 'ilbm', 'jpeg', 'jpg', 'jpg2', 'jp2', 'mng', 'pbm', 'pcd', 'pdf',
                    'pgm', 'pict', 'png', 'ppm', 'ps', 'psd', 'psp', 'svg', 'svgz', 'skp', 'skb', 'swf', 'tiff', 'tif',
                    'wbmp', 'wmf', 'xar', 'xcf', 'xpm'],
            ARQUIVOS=['exe', 'dll', 'ini', 'in', 'bat', 'bin', 'cab', 'csv', 'dif', 'dll', 'iso', 'jar', 'msi', 'mui',
                      'rar', 'sys', 'tmp', 'wmd', 'py', 'lua', 'java', 'pas', 'r', 'rar', 'dmg', '7z', 'tar', 'aspx',
                      'php', 'css', 'ico', 'modell-usb', 'modell', 'version', 'gitattributes', 'awk', 'inc', 'lib',
                      'sdb', 'dat', 'bfc', 'data', 'properties', 'jar', 'src', 'cpx', 'tlb', 'rs', 'vbs', 'ax', 'acm',
                      'com', 'mof', 'nls', 'rsp', 'sdi', 'sep', 'tbl', 'tsp', 'uce', 'ocx', 'msc', 'rtf', 'drv', 'scr',
                      'cmd', 'conf', 'wsf', 'config', 'json', 'dtd', 'iec', 'ime', 'nsl'],
            ACCESS=['accdb', 'accde', 'accdr', 'accdt', 'mdb'],
            WORD=['doc', 'docm', 'docx', 'dot', 'dotx'],
            POWERPOINT=['pot', 'potm', 'potx', 'ppam', 'pps', 'ppsm', 'ppsx', 'ppt', 'pptm', 'pptx'],
            EXCEL=['xla', 'xlam', 'xll', 'xlm', 'xls', 'xlsm', 'xlsx', 'xlt', 'xltm', 'xltx'],
            HTML=['xps', 'htm', 'html'])

        valor_categoria_extensao = self.var_combo_box_categoria.get()
        print(valor_categoria_extensao)
        for chave, valor in tipos_de_extensoes.items():
            if chave == valor_categoria_extensao:
                for valor_extensao in valor:
                    print(valor_extensao)


iniciando_obj = ProgramaPrincipal()
