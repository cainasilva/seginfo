import ctypes

pasta = input("Digite o caminho da pasta a ser ocultado ex (C:/pasta): ")

atributo_ocultar = 0x02

retorno = ctypes.windll.kernel32.SetFileAttributesW('arquivo.txt', atributo_ocultar)

if retorno:
    print("Arquivo foi ocultado")
else:
    print("Arquivo não foi ocultado")