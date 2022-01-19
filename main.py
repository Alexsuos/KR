import pygame, manag
from ship import Ship
from pygame.sprite import Group
from status import Status
from score import Scores

def run():
    pygame.init()
    screen=pygame.display.set_mode((1000,700))
    pygame.display.set_caption("Rengers")
    bg_color=(0,0,0)
    ship=Ship(screen)
    bullets=Group()
    wars=Group()
    manag.create_arwy(screen,wars)
    status=Status()
    sc=Scores(screen, status )


    while True:
        manag.events(screen,ship,bullets)
        if status.run_game==True:
            ship.apdata()
            manag.update(bg_color, screen, status, sc, ship, wars, bullets)
            manag.update_bullets(screen,status, sc, wars, bullets)
            manag.update_wars(status, screen,sc, ship, wars, bullets)

run()