'''
    DiceSimulator.py
    I don't know if I should say die or dice :()
    Author: Alan Richmond, Python3.codes

import pygame, random, time

size = 256                      # Size of window/dice
spsz = size//10                 # size of spots
m = int(size/2)                 # mid-point of dice (or die?)
l=t=int(size/4)                 # location of left and top spots
r=b=size-l                      # location of right and bottom spots
rolling = 12                    # times that dice rolls before stopping
diecol = (255,255,127)          # die colour
spotcol = (0,127,127)           # spot colour

d = pygame.display.set_mode((size, size))
d.fill(diecol)
pygame.display.set_caption("Dice Simulator")

for i in range(rolling):            # roll the die...
    n=random.randint(1,6)                   # random number between 1 & 6
    d.fill(diecol)                          # clear previous spots
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
'''


# Display keyboard input using pygame.  Only prints letters (no numbers
# or special chars).  Backspace deletes one character.  Return clears
# the entire input.
#
# Run with the following command:
#   python pygame-display-input.py
 
import pygame
from pygame.locals import *

from variables import *
 
def name():
    pygame.init()
    screen = pygame.display.set_mode((1440, 900))
    number = "0"

    no_done = False
    
    while not no_done:
        for evt in pygame.event.get():
            if evt.type == KEYDOWN:
                if evt.unicode.isdigit() and evt.unicode>="2" and evt.unicode<="4":
                    number = evt.unicode
                elif evt.key == K_BACKSPACE:
                    number = "0"
                elif evt.key == K_RETURN:
                    print(number)
                    no_done = True
            elif evt.type == QUIT:
                return

        names = ['nitesh','sarup']
                
        screen.fill((0,0,0))
        font = pygame.font.SysFont(CARD_TEXT_STYLE, 30)
        screen.blit(font.render('Enter no of players : ' + str(names), True, WHITE),(100,100))
        screen.blit(font.render(number, True, WHITE), (100,200))
        pygame.display.flip()
 
if __name__ == "__main__":
    name()
    pygame.quit()


"""

# EzText example
from pygame.locals import *
import pygame, sys, eztext

def main():
    # initialize pygame
    pygame.init()
    # create the screen
    screen = pygame.display.set_mode((640,240))
    # fill the screen w/ white
    screen.fill((255,255,255))
    # here is the magic: making the text input
    # create an input with a max length of 45,
    # and a red color and a prompt saying 'type here: '
    txtbx = eztext.Input(maxlength=45, color=(255,0,0), prompt='type here: ')
    # create the pygame clock
    clock = pygame.time.Clock()
    # main loop!

    while 1:
        # make sure the program is running at 30 fps
        clock.tick(30)

        # events for txtbx
        events = pygame.event.get()
        # process other events
        for event in events:
            # close it x button si pressed
            if event.type == QUIT: return

        # clear the screen
        screen.fill((255,255,255))
        # update txtbx
        txtbx.update(events)
        # blit txtbx on the sceen
        txtbx.draw(screen)
        # refresh the display
        pygame.display.flip()

if __name__ == '__main__': main()

"""
"""


import pygame, sys, eztext
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((640,240))
screen.fill((255,255,255))
clock = pygame.time.Clock()
baseFont = pygame.font.SysFont(None, 30)
BLACK = (0,0,0)

question = eztext.Input(maxlength=20, color=BLACK, prompt='What is your name? ')

while True:
    clock.tick(30)
    events = pygame.event.get()
    txt = ''

    for event in events:
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    question.draw(screen)
    question.update(events)
    yourname = 'Your name is ' + question.value
    yournameTxt = baseFont.render(yourname, True, BLACK)
    yournameRect = yournameTxt.get_rect()
    yournameRect.top = 50
    screen.blit(yournameTxt, yournameRect)
    

    pygame.display.flip()

"""

"""
import pygame

pygame.init()
screen = pygame.display.set_mode((640,480))

screen.fill((0,0,0))

pygame.draw.rect(screen,
                 (255,0,0),
                 ((0,0),
                 (300,200)))

clock = pygame.time.Clock()

done = False

while not done:
    clock.tick(30)
    events = pygame.event.get()

    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()
        elif event.type == pygame.MOUSEBUTTONUP:
            x,y = pygame.mouse.get_pos()

            if x>0 and x<300 and y>0 and y<200:

                print("In if")
                
                pygame.display.flip()
                
                screen = pygame.display.set_mode((640,480))

                screen.fill((0,0,0))

                pygame.draw.rect(screen,
                                 (0,255,0),
                                 ((320,220),
                                  (300,200)))

"""


                                 


