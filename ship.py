import pygame
from pygame.sprite import Sprite

class Ship(Sprite):
    def __init__(self, screen):
        'Инициализация корабля'
        super(Ship, self).__init__()
        self.screen=screen
        self.image=pygame.image.load('текстуры/31.png')
        self.rect=self.image.get_rect()
        self.screen_rect=screen.get_rect()
        self.rect.centerx=self.screen_rect.centerx
        self.center=float(self.rect.centerx)
        self.rect.bottom= self.screen_rect.bottom
        self.mright=False
        self.mleft=False

    def output(self):
        "Отрисовка коробля"
        self.screen.blit(self.image, self.rect)

    def apdata(self):
        "Обновление позиции"
        if self.mright==True and self.rect.right<self.screen_rect.right:
            self.center+= 1.5
        elif self.mleft==True and self.rect.left>0:
            self.center-=1.5

        self.rect.centerx=self.center

    def create_ship(self):
        'Размещает пушку по центру внизу'
        self.center=self.screen_rect.centerx