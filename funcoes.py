import os

def lerArquivo():
    try:
        arquivo = open("jogo.py", "r")
    except:
        arquivo = open("jogo.py", "w")
        arquivo.close()
        arquivo = open("jogo.py", "r")
    dados = arquivo.readlines()
    arquivo.close()
    return dados

def salvarArquivo(dados):
    arquivo = open("jogo.py","w")
    arquivo.writelines(dados)
    arquivo.close()

def lerTexto(mensagemEntrada):
    nome = input(mensagemEntrada)
    return valor.upper()

def limparTela():
    os.system("cls")