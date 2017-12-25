# -*- coding: cp1252 -*-
import pygame
from pygame.locals import *
import time
import math


def main():
    pygame.init()

  
    calculatedDirection = 0
    running=True
    while running:
        pygame.display.set_caption('driving')
        screen.fill(0)



        pygame.display.flip()	
        
        time.sleep(0.02)

        #get keyboardkeystrokes
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                exit(0)
       # --- end ---

# Überprüfen, ob dieses Modul als Programm läuft und nicht in einem anderen Modul importiert wird.
if __name__ == '__main__':
    # Unsere Main-Funktion aufrufen.
    main()
