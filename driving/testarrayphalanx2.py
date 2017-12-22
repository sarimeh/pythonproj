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

# Überprüfen, ob dieses Modul als Programm läuft und nicht in einem anderen Modul importiert wird.
if __name__ == '__main__':
    # Unsere Main-Funktion aufrufen.
    main()
