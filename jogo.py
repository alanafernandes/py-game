import pygame, random,  pygame.mixer, time
from pygame.locals import *
from scripts.player import Jogador, Tiro, Planeta
from scripts.enemy import Inimigo
from funcoes import limparTela, lerTexto, lerArquivo, salvarArquivo


limparTela()
nome = lerTexto("DIGITE O SEU NOME: ")
email = lerTexto("DIGITE O SEU E-MAIL: ")
limparTela()

dados = lerArquivo()
dados.append("\n" + "NOME: " +nome+ "\n" + "E-MAIL: " + email)
salvarArquivo(dados)

class Game():
    def __init__(self):

        pygame.init() 

        self.inicio_jogo = True 

        self.largura = 1200 
        self.altura = 600 

        self.janela = pygame.display.set_mode((self.largura, self.altura)) 

        self.fundo = pygame.image.load("img/fundo.jpg") 
        self.fundo = pygame.transform.scale(self.fundo, (self.largura, self.altura)) 
        
        self.planet_group = pygame.sprite.Group()
        self.planeta = Planeta()
        self.planet_group.add(self.planeta)

        self.grupo_jogador = pygame.sprite.Group() 
        self.jogador = Jogador() 
        self.grupo_jogador.add(self.jogador) 
        self.jogador_direita = False 
        self.jogador_esquerda = False 

        self.tiros_grupo = pygame.sprite.Group() 

        self.inimigo_c = True
        self.grupo_inimigo = pygame.sprite.Group()

