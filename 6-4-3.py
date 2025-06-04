# Pick&Place

from arturolib import robotarm

def placeThings(width, numLeft, numRight):
    while True:
        robotarm.pickup()
        coordinates = (0, 0)
        robotarm.place(coordinates)
        for i in range(1, numLeft):
            robotarm.pickup()
            coordinates = (-i*width, 0)
            robotarm.place(coordinates)
        for i in range(1, numLeft):
            robotarm.pickup()
            coordinates = (i*width, 0)
            robotarm.place(coordinates)
