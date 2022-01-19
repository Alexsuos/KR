import pygame

class Bullet(pygame.sprite.Sprite):

    def __init__(self,screen,ship):
        "Создаем пулю в позиции коробля"
        super(Bullet, self).__init__()
        self.screen= screen
        self.rect = pygame.Rect(0,0,2,12)
        self.collor=139,195,74
        self.speed=4.5
        self.rect.centerx=ship.rect.centerx
        self.rect.top=ship.rect.top
        self.y=float(self.rect.y)

    def update(self):
        "Движение пули вверх"
        self.y-=self.speed
        self.rect.y=self.y

    def dr_dul(self):
        "Русуем пулю на экране"
        pygame.draw.rect(self.screen,self.collor,self.rect)