'''
    DiceSimulator.py
    I don't know if I should say die or dice :()
    Author: Alan Richmond, Python3.codes
'''

import pygame, random, time

size = 100                      # Size of window/dice
spsz = size//10                 # size of spots
m = int(size/2)                 # mid-point of dice (or die?)
l=t=int(size/4)                 # location of left and top spots
r=b=size-l                      # location of right and bottom spots
rolling = 12                    # times that dice rolls before stopping
diecol = (255,255,127)          # die colour
spotcol = (0,127,127)           # spot colour

d = pygame.display.set_mode((1440, 900))
d.fill((255,255,255))
pygame.display.set_caption("Dice Simulator")

for i in range(rolling):            # roll the die...
    n=random.randint(1,6)                   # random number between 1 & 6
    d.fill((255,255,255))                          # clear previous spots
    if n % 2 == 1:
        pygame.draw.circle(d,spotcol,(m,m),spsz)  # middle spot
    if n==2 or n==3 or n==4 or n==5 or n==6:
        pygame.draw.circle(d,spotcol,(l,b),spsz)  # left bottom
        pygame.draw.circle(d,spotcol,(r,t),spsz)  # right top
    if n==4 or n==5 or n==6:
        pygame.draw.circle(d,spotcol,(l,t),spsz)  # left top
        pygame.draw.circle(d,spotcol,(r,b),spsz)  # right bottom
    if n==6:
        pygame.draw.circle(d,spotcol,(m,b),spsz)  # middle bottom
        pygame.draw.circle(d,spotcol,(m,t),spsz)  # middle top
    
    pygame.display.flip()
    time.sleep(0.2)

"""
import random

def dice_sim(die_size, rolls):

    results = 0
    dice_sum = 0

    for i in range(0,rolls):
        results = random.randint(1,die_size)
        print("Die %d rolled %d." % (i+1,results))
        dice_sum += results

    print("Total of %d dice rolls is: %d" % (rolls,dice_sum))

    return None

dice_sim(6,2)
"""
