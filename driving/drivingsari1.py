import pygame
from pygame.locals import *
import time
import math



pygame.init()
ok = 1
font = pygame.font.Font(None, 24)

track = pygame.image.load("resources/images/track2.png")
player = pygame.image.load("resources/images/block2.png")
screen = pygame.display.set_mode((600,600))
colorBunt = (120,50,130)
trackx= -540
tracky= -1025
MAX_FORWARD_SPEED = 5
MAX_REVERSE_SPEED = -5
xpos = 275
ypos = 350

#trackx= -540
#tracky= -1025
#xpos = 275
#ypos = 350

keys=[False,False,False,False]
direction = 0
forward = 0

running = 1
while running:
    pygame.display.set_caption('driving')
    screen.fill(0)

    if keys[0]==True:
        direction+= 2
    if keys[1]==True:
        direction-= 2
    if keys[2]==True:
        forward+= 0.1
    if keys[3]==True:
        forward-= 0.5

    if forward > MAX_FORWARD_SPEED:
        forward = MAX_FORWARD_SPEED
    if forward < MAX_REVERSE_SPEED:
        forward = MAX_REVERSE_SPEED    
    movex=math.cos(direction/57.29)*forward
    movey=math.sin(direction/57.29)*forward
    trackx+=movex
    tracky-=movey

    position = (xpos, ypos)
    playerrot = pygame.transform.rotate(player,direction)
    rect = playerrot.get_rect()
    rect.center = position

    
    
    text = font.render(str(Color), True, (150, 150, 0))
    text1 = font.render("speed: "+str(forward), True, (150, 150, 0))
    text2 = font.render("pos x: "+str(xpos), True, (150, 150, 0))
    text3 = font.render("pos y: "+str(ypos), True, (150, 150, 0))
    #screen.fill((0, 128, 255), ((190, 350), (1,1)))
    screen.set_at((190, 350), colorBunt)
    screen.blit(track, (trackx,tracky))
    screen.blit(playerrot, rect)
    screen.blit(text,(0,0))
    screen.blit(text1,(0,20))
    screen.blit(text2,(0,40))
    screen.blit(text3,(0,60))
    pygame.draw.rect(screen, (0, 128, 255), pygame.Rect(200,350, 5, 5))
    pygame.display.flip()
    time.sleep(0.02)
    Color =screen.get_at((199,350))


    for event in pygame.event.get():
    # check if the event is the X button 
        if event.type==pygame.QUIT:
            # if it is quit the game
            pygame.quit()
            exit(0)

        if event.type == pygame.KEYDOWN:
            if event.key==K_LEFT:
                keys[0]=True
            elif event.key==K_RIGHT:
                keys[1]=True
            elif event.key==K_UP:
                keys[2]=True
            elif event.key==K_DOWN:
                keys[3]=True

        if event.type == pygame.KEYUP:
            if event.key==pygame.K_LEFT:
                keys[0]=False
            elif event.key==pygame.K_RIGHT:
                keys[1]=False
            elif event.key==pygame.K_UP:
                keys[2]=False
            elif event.key==pygame.K_DOWN:
                keys[3]=False
