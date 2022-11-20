import os

def lerArquivo():
    try:
        arquivo = open("jogo.txt", "r")
    except:
        arquivo = open("jogo.txt", "w")
        arquivo.close()
        arquivo = open("jogo.txt", "r")
    dados = arquivo.readlines()
    arquivo.close()
    return dados

def salvarArquivo(dados):
    arquivo = open("jogo.txt","w")
    arquivo.writelines(dados)
    arquivo.close()

def lerTexto(mensagemEntrada):
    nome = input(mensagemEntrada)
    return nome.upper()

def limparTela():
    os.system("cls")
