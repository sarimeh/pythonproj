# -*- coding: cp1252 -*-
import pygame
from pygame.locals import *
import time
import math

class Track:
    def __init__(self, trackimage, screen, trackposX, trackposY):
        self.trackimage = trackimage
        self.screen = screen
        self.trackposX = trackposX
        self.trackposY = trackposY

class Car:
    def __init__(self, carimage, forwardspeed, reversespeed, carposX, carposY):
        self.carimage = carimage
        self.forwardspeed = forwardspeed
        self.reversespeed = reversespeed
        self.carposX = carposX
        self.carposY = carposY
 
class Phalanx:
    def __init__(self, X, Y):
        self.X = X
        self.Y = Y
    def printP(self):
        print "Point: (", self.X, ",", self.Y, ")"
    def getX(self):
        return self.X
    def getY(self):
        return self.Y
    def setX(X):
        self.X = X
    def setY(Y):
        self.Y = Y
       
def loadvariables():
    global trackimage, font, carimage, screen
    global colorBunt, tracky
    global MAX_FORWARD_SPEED, MAX_REVERSE_SPEED, xpos, ypos




def main():
    pygame.init()
    #loading variables
    trackimage = pygame.image.load("resources/images/track2.png")
    carimage = pygame.image.load("resources/images/block2.png")
    screen = pygame.display.set_mode((600,600))
    colorBunt = (120,50,130)
    trackx = -540
    tracky = -1025
    MAX_FORWARD_SPEED = 5
    MAX_REVERSE_SPEED = -5
    xpos = 275
    ypos = 350 
    font = pygame.font.Font(None, 24)
    keys=[False,False,False,False]
    direction = 0
    forward = 0
    running = 1
    Color = 0
    
    #creating objects
    track1 = Track(trackimage, screen, trackx, tracky)
    car1 = Car(carimage, MAX_FORWARD_SPEED, MAX_REVERSE_SPEED, xpos, ypos)

    P1 = Phalanx(200, 350)
    Px1 = [0, 0, 0, 0, 0]
    Px2 = [0, 0, 0, 0, 0]
    Px3 = [0, 0, 0, 0, 0]
    Px4 = [0, 0, 0, 0, 0]
    Px5 = [0, 0, 0, 0, 0]
    Px1[0] = Px2[0] = Px3[0] = Px4[0] = Px5[0] = P1

    for i in xrange(1, 5):
        Px1[i] = Phalanx(Px1[i-1].X, Px1[i-1].Y+10)
        Px2[i] = Phalanx(Px2[i-1].X-10, Px2[i-1].Y+10)
        Px3[i] = Phalanx(Px3[i-1].X-10, Px3[i-1].Y)
        Px4[i] = Phalanx(Px4[i-1].X-10, Px4[i-1].Y-10)
        Px5[i] = Phalanx(Px5[i-1].X, Px5[i-1].Y-10) 


    for i in xrange(0, 5):
        Px1[i].printP()
    print "----"
    for i in xrange(0, 5):
        Px2[i].printP()
    print "----"
    for i in xrange(0, 5):
        Px3[i].printP()    
    print "----"
    for i in xrange(0, 5):
        Px4[i].printP()
    print "----"
    for i in xrange(0, 5):
        Px5[i].printP()

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
        playerrot = pygame.transform.rotate(carimage,direction)
        rect = playerrot.get_rect()
        rect.center = position
    
        
        text = font.render(str(Color), True, (150, 150, 0))
        screen.blit(text,(0,0))
        text1 = font.render("speed: "+str(forward), True, (150, 150, 0))
        text2 = font.render("pos x: "+str(xpos), True, (150, 150, 0))
        text3 = font.render("pos y: "+str(ypos), True, (150, 150, 0))
        screen.fill((0, 128, 255), ((190, 350), (1,1)))
        screen.set_at((190, 350), colorBunt)
        screen.blit(trackimage, (trackx,tracky))
        screen.blit(playerrot, rect)
        screen.blit(text,(0,0))
        screen.blit(text1,(0,20))
        screen.blit(text2,(0,40))
        screen.blit(text3,(0,60))
        pygame.draw.rect(screen, (0, 128, 255), pygame.Rect(200,350, 5, 5))

	for i in xrange(0, 5):
		pygame.draw.rect(screen, (0, 128, 255), pygame.Rect(Px1[i].X,Px1[i].Y, 2, 2))
		pygame.draw.rect(screen, (0, 128, 255), pygame.Rect(Px2[i].X,Px2[i].Y, 2, 2))
		pygame.draw.rect(screen, (0, 128, 255), pygame.Rect(Px3[i].X,Px3[i].Y, 2, 2))
		pygame.draw.rect(screen, (0, 128, 255), pygame.Rect(Px4[i].X,Px4[i].Y, 2, 2))
		pygame.draw.rect(screen, (0, 128, 255), pygame.Rect(Px5[i].X,Px5[i].Y, 2, 2))

        pygame.display.flip()
        Color =screen.get_at((199,350))
        
        time.sleep(0.02)

        #get keyboardkeystrokes
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                exit(0)

	    if event.type == pygame.KEYDOWN:            
		if event.key==K_q:
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
        # --- end ---

# �berpr�fen, ob dieses Modul als Programm l�uft und nicht in einem anderen Modul importiert wird.
if __name__ == '__main__':
    # Unsere Main-Funktion aufrufen.
    main()