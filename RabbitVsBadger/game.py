__author__ = 'eguoshi'

#1 - Import libs
import pygame
from pygame.locals import *
import math
import random

#2 Initialize the game
pygame.init()
width, height = 640, 480
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Rabbit Vs. Badger")

keys = [False, False, False, False]  #WASD
playerpos = [100, 100] # Player position

acc = [0, 0]  # Accuracy
arrows = []   # Track the arrows

badtimer = 100
badtimer1 = 0
badguys = [[640,100]]
healthvalue = 194
totaltimer = 90000

pygame.font.init()
pygame.mixer.init()

#3 load images
player = pygame.image.load("resources/images/dude.png")
grass = pygame.image.load("resources/images/grass.png")
castle = pygame.image.load("resources/images/castle.png")
arrow = pygame.image.load("resources/images/bullet.png")
badguyimg1 = pygame.image.load("resources/images/badguy.png")
badguyimg = badguyimg1
healthbar = pygame.image.load("resources/images/healthbar.png")
health = pygame.image.load("resources/images/health.png")
gameover = pygame.image.load("resources/images/gameover.png")
youwin = pygame.image.load("resources/images/youwin.png")

grass_w = grass.get_width()
grass_h = grass.get_height()
player_w = player.get_width()
player_h = player.get_height()
castle_w = castle.get_width()

#3.1 load audio
hit = pygame.mixer.Sound("resources/audio/explode.wav")
enemy = pygame.mixer.Sound("resources/audio/enemy.wav")
shoot = pygame.mixer.Sound("resources/audio/shoot.wav")
hit.set_volume(0.05)
enemy.set_volume(0.05)
shoot.set_volume(0.05)
pygame.mixer.music.load("resources/audio/moonlight.wav")
pygame.mixer.music.play(-1, 0.0)
pygame.mixer.music.set_volume(0.25)

#4 loop body
running = 1
exitcode = 0
while running:
    badtimer -= 1
    #5 Clear before re-drawing
    screen.fill(0)

    #6 Draw the screen elements
    for x in range(width/grass_w+1):
        for y in range(height/grass_h+1):
            screen.blit(grass, (x*grass_w, y*grass_h))

    screen.blit(castle, (0,30))
    screen.blit(castle, (0,135))
    screen.blit(castle, (0,240))
    screen.blit(castle, (0,345))

    #6.1 Set player position and rotation
    position = pygame.mouse.get_pos()
    angle = math.atan2(position[1]-(playerpos[1]+player_w/2), position[0]-(playerpos[0]+player_h/2))
    playerrot = pygame.transform.rotate(player, 360-angle*57.29)
    playerpos1 = (playerpos[0]-playerrot.get_rect().width/2, playerpos[1]-playerrot.get_rect().height/2)
    screen.blit(playerrot, playerpos1)

    #6.2 Draw Arrows
    index = 0
    for bullet in arrows:
        velx = math.cos(bullet[0]) * 10
        vely = math.sin(bullet[0]) * 10
        bullet[1] += velx
        bullet[2] += vely

        if bullet[1] < -64 or bullet[1] > width or bullet[2] < -64 or bullet[2] > height:
            arrows.pop(index)

        index += 1

    for projectile in arrows:
        arrow1 = pygame.transform.rotate(arrow, 360-projectile[0]*57.29)
        screen.blit(arrow1, (projectile[1], projectile[2]))

    #6.3 Darw Badgers
    if badtimer == 0:
        badguys.append([640, random.randint(50, height - 50)])
        badtimer = 100-(badtimer1*2)
        if badtimer1 >= 35:
            badtimer1 = 35
        else:
            badtimer1 += 5

    index = 0
    for badguy in badguys:
        if badguy[0] < -64:
            badguys.pop(index)
        badguy[0] -= 7

        # 6.3.1 Attack Castle
        badrect = pygame.Rect(badguyimg.get_rect())
        badrect.top = badguy[1]
        badrect.left = badguy[0]
        if badrect.left < castle_w:
            hit.play()
            healthvalue -= random.randint(5, 20)
            badguys.pop(index)

        #6.3.2 check for the collisions
        index1=0
        for bullet in arrows:
            bulletrect = pygame.Rect(arrow.get_rect())
            bulletrect.left = bullet[1]
            bulletrect.top = bullet[2]

            if badrect.colliderect(bulletrect):
                enemy.play()
                acc[0] += 1
                badguys.pop(index)
                arrows.pop(index1)

            index1 += 1

        index += 1

    for badguy in badguys:
        screen.blit(badguyimg, badguy)

    #6.4 Draw Clock
    font = pygame.font.Font(None, 24)
    survivedtext = font.render(str((totaltimer-pygame.time.get_ticks())/60000)+":"+str((totaltimer-pygame.time.get_ticks())/1000%60).zfill(2), True, (0,0,0))
    textRect = survivedtext.get_rect()
    textRect.topright = [width-5, 5]
    screen.blit(survivedtext, textRect)

    #6.5 Draw HelthBar
    screen.blit(healthbar, (5, 5))
    for heath1 in range(healthvalue):
        screen.blit(health, (heath1+8, 8))

    #7 update the screen
    pygame.display.flip()

    #8 loop through the events
    for event in pygame.event.get():
        #Check if the event is the CLOSE button, if yes, quit the game
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)

        if event.type == pygame.KEYDOWN:
            if event.key == K_w or event.key == K_UP:
                keys[0] = True
            elif event.key == K_a or event.key == K_LEFT:
                keys[1] = True
            elif event.key == K_s or event.key == K_DOWN:
                keys[2] = True
            elif event.key == K_d or event.key == K_RIGHT:
                keys[3] = True

        if event.type == pygame.KEYUP:
            if event.key == K_w or event.key == K_UP:
                keys[0] = False
            elif event.key == K_a or event.key == K_LEFT:
                keys[1] = False
            elif event.key == K_s or event.key == K_DOWN:
                keys[2] = False
            elif event.key == K_d or event.key == K_RIGHT:
                keys[3] = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            shoot.play()
            position = pygame.mouse.get_pos()
            acc[1] += 1
            arrows.append([math.atan2(position[1]-(playerpos1[1]+player_w/2),position[0]-(playerpos1[0]+player_h/2)),playerpos1[0]+player_w/2,playerpos1[1]+player_h/2])


    #9 Move Player
    if keys[0]:
        playerpos[1] -= 5
    elif keys[2]:
        playerpos[1] += 5

    if keys[1]:
        playerpos[0] -= 5
    elif keys[3]:
        playerpos[0] += 5

    #10 Win/Lose check
    if pygame.time.get_ticks() >= totaltimer:
        running = 0
        exitcode = 1

    if healthvalue <= 0:
        running = 0
        exitcode = 0

    if acc[1] != 0:
        accuracy = acc[0] * 1.0 / acc[1] * 100
    else:
        accuracy = 0

    #11 Win/Lose display
    font = pygame.font.Font(None, 24)
    if exitcode == 0:
        text = font.render("Accuracy: "+str(accuracy)+"%", True, (255,0,0))
        textRect = text.get_rect()
        textRect.centerx = screen.get_rect().centerx
        textRect.centery = screen.get_rect().centery+24
        screen.blit(gameover, (0,0))
        screen.blit(text, textRect)
    else:
        text = font.render("Accuracy: "+str(accuracy)+"%", True, (0,255,0))
        textRect = text.get_rect()
        textRect.centerx = screen.get_rect().centerx
        textRect.centery = screen.get_rect().centery+24
        screen.blit(youwin, (0,0))
        screen.blit(text, textRect)

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)
    pygame.display.flip()