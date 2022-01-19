import pygame
import sys
from bullet import Bullet
from w import War
import time

def events(screen,ship,bullets):
    "Обработка событий"
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type==pygame.KEYDOWN:
            # кнопка вправо
            if event.key==pygame.K_d:
               ship.mright=True
            elif event.key==pygame.K_a:
               ship.mleft=True
            elif event.key==pygame.K_SPACE:
                new_bullet=Bullet(screen,ship)
                bullets.add(new_bullet)
        elif event.type==pygame.KEYUP:
            # кнопка вправо
            if event.key==pygame.K_d:
                ship.mright=False
            elif event.key==pygame.K_a:
                ship.mleft=False

def update(bg_color,screen,status, sc,ship,wars,bullets):
    'Обновление экрана'
    screen.fill(bg_color)
    sc.show_score()
    for bullet in bullets.sprites():
        bullet.dr_dul()
    ship.output()
    wars.draw(screen)
    pygame.display.flip()

def update_bullets(screen,status,sc,wars,bullets):
    'Обновление позиции пуль'
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <=0:
            bullets.remove(bullet)
    collisions=pygame.sprite.groupcollide(bullets,wars,True, True)
    if collisions:
        for wars in collisions.values():
            status.score += 10*len(wars)
        sc.image_score()
        check_high_score(status,sc)
        sc.image_ship()
    if len(wars)==0:
        bullets.empty()
        create_arwy(screen,wars)

def ship_kill(status,screen,sc,ship,wars,bullet):
    "Столкновение коробля и армии"
    if status.ship_life>0:
        status.ship_life -= 1
        sc.image_ship()
        wars.empty()
        bullet.empty()
        create_arwy(screen, wars)
        ship.create_ship()
        time.sleep(2)
    else:
        status.run_game=False
        sys.exit()

def update_wars(status,screen,sc,ship,wars,bullets):
    "обновление позиции врагов"
    wars.update()
    if pygame.sprite.spritecollideany(ship,wars):
        ship_kill(status,screen,sc,ship,wars,bullets)
    wars_check(status, screen,sc, ship, wars, bullets)

def wars_check(status,screen,sc,ship,wars,bullets):
    'проверка долбралась ли армия до края'
    screem_rect=screen.get_rect()
    for war in wars.sprites():
        if war.rect.bottom>=screem_rect.bottom:
            ship_kill(status,screen,sc,ship,wars,bullets)
            break

def create_arwy(screen,wars):
    "Создание армии противника"
    war=War(screen)
    war_width=war.rect.width
    numbers_war_x=int((1000-2*war_width)/war_width)
    war_height=war.rect.height
    number_war_y=int((700-100-2*war_height)/war_height)

    for row_number in range(number_war_y-2):
        for war_number in range(numbers_war_x):
            war = War(screen)
            war.x = war_width + (war_width * war_number)
            war.y=war_height+(war_height*row_number)
            war.rect.x = war.x
            war.rect.y = war.rect.height+war.rect.height*row_number
            wars.add(war)

def check_high_score(status,sc):
    "Проверка новвых рекордов"
    if status.score>status.high_score:
        status.high_score=status.score
        sc.image_high_score()
        with open('record.txt','w')as f:
            f.write(str(status.high_score))