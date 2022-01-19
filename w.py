import pygame

class War(pygame.sprite.Sprite):
    "класс врага"
    def __init__(self,screen):
        "инициализация и задание начальной позиции"
        super(War,self).__init__()
        self.screen=screen
        self.image=pygame.image.load('текстуры/вар.png')
        self.rect=self.image.get_rect()
        self.rect.x=self.rect.width
        self.rect.y=self.rect.height
        self.x=float(self.rect.x)
        self.y=float(self.rect.y)

    def draw(self):
        "вывод на экран"
        self.screen.blit(self.image,self.rect)

    def update(self):
        "Движение армии вниз"
        self.y+=0.1
        self.rect.y= self.y