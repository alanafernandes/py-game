import pygame, random, time
from pygame.locals import *


class Inimigo (pygame.sprite.Sprite):
    branco = (255,255,255)  

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.animacao = [pygame.image.load("img/meteoro1.png").convert_alpha(),
                                pygame.image.load("img/meteoro2.png").convert_alpha(),
                                pygame.image.load("img/meteoro3.png").convert_alpha()]


        self.image = pygame.image.load("img/meteoro1.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (68, 78))
        self.rect  = self.image.get_rect()
        self.rect[0] = random.randint(10,1100)
        self.rect[1] = random.randint(10,30)
        self.velocidade = 1
        self.imagem_agora = 0
        self.explosao_agora = 0

    def update(self):
        self.imagem_agora = (self.imagem_agora +1 ) %3
        self.image = self.animacao[self.imagem_agora]
        self.image = pygame.transform.scale(self.image, (68, 78))
        self.rect[1] += self.velocidade
    
    def morreu():
        self.fonte  = pygame.font.Font("font/8bit.ttf",95)
        self.fonte2  = pygame.font.Font("font/8bit.ttf",45)
        self.textoDisplay = fonte.render("GAME OVER",True,branco)
        self.textoDisplay2 = fonte2.render("Aperte enter para continuar !!!!",True,branco)
        self.gameDisplay.blit(self.textoDisplay, (150,150))
        self.gameDisplay.blit(self.textoDisplay2, (150,350))
        pygameDisplay.update()
        time.sleep(2)