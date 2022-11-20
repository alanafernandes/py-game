import pygame
from pygame.locals import *

class Jogador (pygame.sprite.Sprite):
    def _init_(self):
        pygame.sprite.Sprite._init_(self)

        self.imagens = [pygame.image.load("img/jogador1.png").convert_alpha(),
                            pygame.image.load("img/jogador2.png").convert_alpha()]

        self.image_agora = 0
        self.velocidade = 20

        self.image = pygame.image.load("img/jogador1.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (61, 78))
        self.rect = self.image.get_rect()
        self.rect[0] = 600
        self.rect[1] = 490
        self.pontos = 0

    def update(self):
        self.animation()

    def animation(self):
        self.image_agora = (self.image_agora +1 ) %2
        self.image = self.imagens[self.image_agora]
        self.image = pygame.transform.scale(self.image, (68, 78))


class Tiro (pygame.sprite.Sprite):
    def _init_(self):
        pygame.sprite.Sprite._init_(self)
        self.image = pygame.image.load("img/tiro.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.velocidade = 30


    def update(self):
        self.rect[1] -= self.velocidade

class Planeta (pygame.sprite.Sprite):
    def _init_(self):
        pygame.sprite.Sprite._init_(self)
        self.image = pygame.image.load("img/planeta.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (1200, 100))
        self.rect = self.image.get_rect()
        self.rect[0] = 0
        self.rect[1] = 560

    def update(self):
        self.rect[1] -= self.velocidade



