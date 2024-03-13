from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from tkinter.filedialog import askdirectory
from tkinter.simpledialog import askstring
from tkinter.messagebox import showinfo


"""Escolhendo as informações para salvar o arquivo"""
showinfo('AVISA!', 'Escolha o direto para salvar o documento')
local_save = askdirectory()
nome_arquivo_pdf = askstring('Imprestante!', 'Digite o nome do arquivo')

""" Criando o Arquivos PDF"""
pdf = canvas.Canvas(nome_arquivo_pdf + '.pdf', pagesize=A4)
