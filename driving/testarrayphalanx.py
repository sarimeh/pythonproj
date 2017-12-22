# -*- coding: cp1252 -*-
from pygame.locals import *
import time
import math

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
        

def main():
    xpos = 275
    ypos = 350 
    
    P1 = Phalanx(0, 0)
    Px1 = Px2 = Px3 = Px4 = Px5 = [0, 0, 0, 0, 0]
    Px1[0] = Px2[0] = Px3[0] = Px4[0] = Px5[0] = P1

    for i in xrange(1, 5):
        P1 = Phalanx(Px1[i-1].X, Px1[i-1].Y)
        Px1[i] = Phalanx(P1.X, P1.Y+10)
        P2 = Phalanx(Px1[i-1].X, Px1[i-1].Y)
        Px2[i] = Phalanx(P2.X-10, P2.Y+10)
        P3 = Phalanx(Px1[i-1].X, Px1[i-1].Y)
        Px3[i] = Phalanx(P3.X-10, P3.Y)
        P4 = Phalanx(Px1[i-1].X, Px1[i-1].Y)
        Px4[i] = Phalanx(P4.X-10, P4.Y-10)
        P5 = Phalanx(Px1[i-1].X, Px1[i-1].Y)
        Px5[i] = Phalanx(P5.X, P5.Y-10) 
        Px1[i].printP()
        Px2[i].printP()
        Px3[i].X = 66
        Px3[i].printP()
        Px4[i].printP()
        Px5[i].printP()


# Überprüfen, ob dieses Modul als Programm läuft und nicht in einem anderen Modul importiert wird.
if __name__ == '__main__':
    # Unsere Main-Funktion aufrufen.
    main()
