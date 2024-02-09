
lista_extenoes_valores = ['jpg', 'png', 'mp4', 'mp3', 'pfd', 'txt', 'dll', 'exe', 'ini']

valor_extensao = input('Digite uma extensao: ').lower().strip()

if valor_extensao in lista_extenoes_valores:
    print(True)
else:
    print(False)
    