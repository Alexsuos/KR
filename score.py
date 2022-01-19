import pygame.font
from ship import  Ship
from pygame.sprite import Group
class Scores():
    '''Вывод игровой инфы'''
    def __init__(self,screen,status):
        self.screen=screen
        self.screen_rect=screen.get_rect()
        self.status=status
        self.text_color=(139,195,74)
        self.font=pygame.font.SysFont(None,36)
        self.image_score()
        self.image_high_score()
        self.image_ship()

    def image_score(self):
        "преобразует текст счета в графическое изображение"
        self.score_img=self.font.render(str(self.status.score),True, self.text_color,(0,0,0))
        self.score_rect=self.score_img.get_rect()
        self.score_rect.right=self.screen_rect.right - 40
        self.score_rect.top=20
    def image_high_score(self):
        'Преобразует рекорд в графическое изображение'
        self.high_score_image=self.font.render(str(self.status.high_score),True,self.text_color,(0,0,0))
        self.high_score_rect=self.high_score_image.get_rect()
        self.high_score_rect.centerx=self.screen_rect.centerx
        self.high_score_rect.top=self.screen_rect.top+20

    def image_ship(self):
        "Колличестово жизней"
        self.ship=Group()
        for ship_number in range(self.status.ship_life):
            ship=Ship(self.screen)
            ship.rect.x=15+ship_number*ship.rect.width
            ship.rect.y=20
            self.ship.add(ship)


    def show_score(self):
       "вывод счета на экран"
       self.screen.blit(self.score_img, self.score_rect)
       self.screen.blit(self.high_score_image, self.high_score_rect)
       self.ship.draw(self.screen)