class mytest:
    def __init_(self, car):
        self.car = car

class Track:
    def __init__(self, trackimage, screen, trackposX, trackposY):
        self.trackimage = trackimage
        self.screen = screen
        self.trackposX = trackposX
        self.trackposY = trackposY

def loadvariables():
    global trackimage, font, carimage, screen
    global colorBunt, trackx, tracky
    global MAX_FORWARD_SPEED, MAX_REVERSE_SPEED, xpos, ypos
    trackimage = 1
    screen = 1
    trackx = -540
    tracky = -1025
    MAX_FORWARD_SPEED = 5
    MAX_REVERSE_SPEED = -5
    xpos = 275
    ypos = 350 



def main():
    loadvariables()
    track1 = Track(trackimage, screen, trackx, tracky)
    print hello


main()

