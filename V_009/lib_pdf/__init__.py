from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from tkinter.filedialog import askdirectory
from tkinter.simpledialog import askstring
from tkinter.messagebox import showinfo
from pathlib import Path


"""Escolhendo as informações para salvar o arquivo"""
showinfo('AVISA!', 'Escolha o direto para salvar o documento')
local_save = Path(askdirectory())
nome_arquivo_pdf = askstring('Imprestante!', 'Digite o nome do arquivo')
pdf_diretorio_save = local_save + '\\' + nome_arquivo_pdf + '.pdf'
print(pdf_diretorio_save)
""" Criando o Arquivos PDF"""
pdf = canvas.Canvas(pdf_diretorio_save, pagesize=A4)
pdf.save()
