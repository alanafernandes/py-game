import pygame, random,  pygame.mixer, time
from pygame.locals import *
from scripts.jogador import Jogador, Tiro, Planeta
from scripts.inimigo import Inimigo
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
        
        self.game_init = True
        while self.game_init:
            self.fps.tick(30) 
            for event in pygame.event.get(): 
                if event.type == QUIT:
                    pygame.quit()

                if event.type == KEYDOWN: 
                    if event.key == K_RIGHT:
                        self.jogador_direita = True
                    if event.key == K_LEFT:
                        self.jogador_esquerda = True
                    if event.key == K_UP: 
                        self.jogador_tiro = Tiro() 
                        self.jogador_tiro.rect[0] = self.jogador.rect[0]+23 
                        self.jogador_tiro.rect[1] = self.jogador.rect[1]
                        self.tiros_grupo.add(self.jogador_tiro) 
                        pygame.mixer.Channel(1).play(pygame.mixer.Sound("sons/som_tiro.wav")) 
                        pygame.mixer.Channel(1).set_volume(0.1)


                if event.type == KEYUP: 
                    if event.key == K_RIGHT:
                        self.jogador_direita = False
                    if event.key == K_LEFT:
                        self.jogador_esquerda = False

            if self.jogador_direita: 
                self.jogador.rect[0] += self.jogador.velocidade
            if self.jogador_esquerda: 
                self.jogador.rect[0] -= self.jogador.velocidade

            self.janela.blit(self.fundo,(0,0)) 
            self.janela.blit(self.placar,(850,10)) 
            self.janela.blit(self.placar_nivel,(650,10))
            self.tiros_grupo.update() 
            self.grupo_jogador.update() 
            self.grupo_jogador.draw(self.janela) 
            self.planet_group.update() 
            self.planet_group.draw(self.janela) 
            self.grupo_inimigo.update() 
            self.grupo_inimigo.draw(self.janela)
            
            if len(self.grupo_inimigo) <5: 
                for i in range(5):
                    self.inimigo = Inimigo()
                    self.grupo_inimigo.add(self.inimigo)
                    print("adicionou mais um")


            if self.pontos_jogador > 500:
                self.inimigo.velocidade  = 2
                self.nivel = 1
                self.placar_nivel = self.font.render("NÍVEL: "+ str(self.nivel),1,(255,255,255))
            if self.pontos_jogador > 800:
                self.inimigo.velocidade  = 3
                self.nivel = 2
                self.placar_nivel = self.font.render("NÍVEL: "+ str(self.nivel),1,(255,255,255))
            if self.pontos_jogador > 1000:
                self.inimigo.velocidade  = 4
                self.nivel = 3
                self.placar_nivel = self.font.render("NÍVEL: "+ str(self.nivel),1,(255,255,255))
            if self.pontos_jogador > 1500:
                self.inimigo.velocidade  = 6
                self.nivel = 4
                self.placar_nivel = self.font.render("NÍVEL: "+ str(self.nivel),1,(255,255,255))
            if self.pontos_jogador > 1900:
                self.inimigo.velocidade  = 8
                self.nivel = 5
                self.placar_nivel = self.font.render("NÍVEL: "+ str(self.nivel),1,(255,255,255))
            if self.pontos_jogador > 2200:
                self.inimigo.velocidade  = 9
                self.nivel = 6
                self.placar_nivel = self.font.render("NÍVEL: "+ str(self.nivel),1,(255,255,255))
            if self.pontos_jogador > 3000:
                self.inimigo.velocidade  = 12
                self.nivel = "NÍVEL FINAL"
                self.placar_nivel = self.font.render("NÍVEL: "+ str(self.nivel),1,(255,255,255))

            for bullet in self.tiros_grupo:
                self.tiros_grupo.draw(self.janela) 
                if self.jogador_tiro.rect[1]< -20: 
                    self.tiros_grupo.remove(self.jogador_tiro) 
                    print('tiro removido')


            if (pygame.sprite.groupcollide(self.tiros_grupo, self.grupo_inimigo, True, True)):
                self.pontos_jogador += random.randint(1,10)
                self.placar = self.font.render("PONTOS: " + str(self.pontos_jogador), 1, (255,255,255))
                pygame.mixer.Channel(2).play(pygame.mixer.Sound("sons/som_inimigo.wav")) 
                pygame.mixer.Channel(2).set_volume(0.1)

            if (pygame.sprite.groupcollide(self.grupo_jogador, self.grupo_inimigo, True, True)):
                    Game()
                    morreu()
                    self.game_init = False
                    
                    

            if (pygame.sprite.groupcollide(self.planet_group, self.grupo_inimigo, True, True)):
                    Game()
                    morreu()
                    self.game_init = False
                    
                    




            pygame.display.update()
            
Game()
