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

        self.pontos_jogador = self.jogador.pontos
        self.font = pygame.font.Font("font/8bit.ttf", 30)
        self.placar = self.font.render("PONTOS: " + str(self.pontos_jogador), 1, (255,255,255))
        self.nivel = 0
        self.inimigo_janela = 5
        self.placar_nivel = self.font.render("NÍVEL: "+ str(self.nivel),1,(255,255,255))

        pygame.mixer.init()
        pygame.mixer.set_reserved(0)
        self.musica = pygame.mixer.Sound("sons/musica_jogo.wav")
        pygame.mixer.Channel(0).play(self.musica,-1)
        pygame.mixer.Channel(0).set_volume(0.1)


        self.fps = pygame.time.Clock()
