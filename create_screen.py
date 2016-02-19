import pygame
import sys
from pygame.locals import *

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0,255,0)
BLUE = (0,0,255)
ORANGE = (255,128,0)
YELLOW = (255,255,0)
BROWN = (165,42,42)
LIGHT_BLUE = (198,226,255)
PINK = (255,20,147)
BOARD_GREEN = (230,255,230)
RED = (255, 0, 0)

# Define dimensions
SCREEN_WIDTH = 1440
SCREEN_HEIGHT = 900
BOARD_WIDTH = 1100
BOARD_HEIGHT = 770
BOARD_ROWS = 11
BOARD_COLS = 11
COLOR_RECT_SIZE = 9
INFO_BOARD_SPACING = 90
CARD_WIDTH = 99
CARD_HEIGHT = 69
CARD_MARGIN = 1
INFO_WIDTH = 250
INFO_HEIGHT = 770
GAME_OPTIONS_WIDTH = 1440
GAME_OPTIONS_HEIGHT = 130

CARD_TEXT_STYLE = 'gillsansmt'

# --------------CREATE BOARD FUNCTION--------------
# creates the board and all the cards inside it


def create_board():

    if True:
        screen.fill(BLACK)


        # creating the board
        for row in range(BOARD_ROWS):
            for col in range(BOARD_COLS):
                color = BOARD_GREEN
                if row == 0 or row == 10 or col == 0 or col == 10:
                    pygame.draw.rect(screen,
                                     color,
                                     [(CARD_MARGIN + CARD_WIDTH) * col + CARD_MARGIN,
                                      (CARD_MARGIN + CARD_HEIGHT) * row + CARD_MARGIN,
                                      CARD_WIDTH,
                                      CARD_HEIGHT])

        #adding brown cards

        color = BROWN
        
        #   MEDITERRANEAN   AVENUE
        pygame.draw.rect(screen,
                         color,
                         [(CARD_MARGIN+CARD_WIDTH) * 9 + CARD_MARGIN,
                         (CARD_MARGIN+CARD_HEIGHT) * 10 + CARD_MARGIN,
                         CARD_WIDTH,
                         COLOR_RECT_SIZE])

        font = pygame.font.SysFont(CARD_TEXT_STYLE, 10)
        screen.blit(font.render('MEDITERRANEAN', True, (0,0,0)), (908, 720))
        screen.blit(font.render('AVENUE', True, (0,0,0)), (908, 735))
        screen.blit(font.render('(M 60)', True, (0,0,0)), (908, 755))
        
        
        #   BALTIC  AVENUE
        pygame.draw.rect(screen,
                         color,
                         [(CARD_MARGIN+CARD_WIDTH) * 7 + CARD_MARGIN,
                         (CARD_MARGIN+CARD_HEIGHT) * 10 + CARD_MARGIN,
                         CARD_WIDTH,
                         COLOR_RECT_SIZE])

        font = pygame.font.SysFont(CARD_TEXT_STYLE, 10)
        screen.blit(font.render('BALTIC', True, (0,0,0)), (708, 720))
        screen.blit(font.render('AVENUE', True, (0,0,0)), (708, 735))
        screen.blit(font.render('(M 60)', True, (0,0,0)), (708, 755))


        #adding light blue cards

        color = LIGHT_BLUE

        #   CONNECTICUT AVENUE
        pygame.draw.rect(screen,
                         color,
                         [(CARD_MARGIN+CARD_WIDTH) * 1 + CARD_MARGIN,
                         (CARD_MARGIN+CARD_HEIGHT) * 10 + CARD_MARGIN,
                         CARD_WIDTH,
                         COLOR_RECT_SIZE])

        font = pygame.font.SysFont(CARD_TEXT_STYLE, 10)
        screen.blit(font.render('CONNECTICUT', True, (0,0,0)), (108, 720))
        screen.blit(font.render('AVENUE', True, (0,0,0)), (108, 735))
        screen.blit(font.render('(M 120)', True, (0,0,0)), (108, 755))


        #   VERMONT AVENUE
        pygame.draw.rect(screen,
                         color,
                         [(CARD_MARGIN+CARD_WIDTH) * 2 + CARD_MARGIN,
                         (CARD_MARGIN+CARD_HEIGHT) * 10 + CARD_MARGIN,
                         CARD_WIDTH,
                         COLOR_RECT_SIZE])

        font = pygame.font.SysFont(CARD_TEXT_STYLE, 10)
        screen.blit(font.render('VERMONT', True, (0,0,0)), (208, 720))
        screen.blit(font.render('AVENUE', True, (0,0,0)), (208, 735))
        screen.blit(font.render('(M 100)', True, (0,0,0)), (208, 755))


        #   ORIENTAL AVENUE
        pygame.draw.rect(screen,
                         color,
                         [(CARD_MARGIN+CARD_WIDTH) * 4 + CARD_MARGIN,
                         (CARD_MARGIN+CARD_HEIGHT) * 10 + CARD_MARGIN,
                         CARD_WIDTH,
                         COLOR_RECT_SIZE])

        font = pygame.font.SysFont(CARD_TEXT_STYLE, 10)
        screen.blit(font.render('ORIENTAL', True, (0,0,0)), (408, 720))
        screen.blit(font.render('AVENUE', True, (0,0,0)), (408, 735))
        screen.blit(font.render('(M 100)', True, (0,0,0)), (408, 755))



        #adding pink cards

        color = PINK


        #   VIRGINIA    AVENUE
        pygame.draw.rect(screen,
                         color,
                         [(CARD_MARGIN+CARD_WIDTH) * 1 - COLOR_RECT_SIZE,
                         (CARD_MARGIN+CARD_HEIGHT) * 6 + CARD_MARGIN,
                         COLOR_RECT_SIZE,
                         CARD_HEIGHT])

        font = pygame.font.SysFont(CARD_TEXT_STYLE, 10)
        text = font.render('VIRGINIA', True, (0,0,0))
        text = pygame.transform.rotate(text, 270)
        screen.blit(text, (70, 430))
        text = font.render('AVENUE', True, (0,0,0))
        text = pygame.transform.rotate(text, 270)
        screen.blit(text, (55, 430))
        text = font.render('(M 160)', True, (0,0,0))
        text = pygame.transform.rotate(text, 270)
        screen.blit(text, (20, 430))


        #   STATES  AVENUE
        pygame.draw.rect(screen,
                         color,
                         [(CARD_MARGIN+CARD_WIDTH) * 1 - COLOR_RECT_SIZE,
                         (CARD_MARGIN+CARD_HEIGHT) * 7 + CARD_MARGIN,
                         COLOR_RECT_SIZE,
                         CARD_HEIGHT])

        font = pygame.font.SysFont(CARD_TEXT_STYLE, 10)
        text = font.render('STATES', True, (0,0,0))
        text = pygame.transform.rotate(text, 270)
        screen.blit(text, (70, 500))
        text = font.render('AVENUE', True, (0,0,0))
        text = pygame.transform.rotate(text, 270)
        screen.blit(text, (55, 500))
        text = font.render('(M 140)', True, (0,0,0))
        text = pygame.transform.rotate(text, 270)
        screen.blit(text, (20, 500))


        #   ST. CHARLES PLACE
        pygame.draw.rect(screen,
                         color,
                         [(CARD_MARGIN+CARD_WIDTH) * 1 - COLOR_RECT_SIZE,
                         (CARD_MARGIN+CARD_HEIGHT) * 9 + CARD_MARGIN,
                         COLOR_RECT_SIZE,
                         CARD_HEIGHT])

        font = pygame.font.SysFont(CARD_TEXT_STYLE, 10)
        text = font.render('ST. CHARLES', True, (0,0,0))
        text = pygame.transform.rotate(text, 270)
        screen.blit(text, (70, 640))
        text = font.render('PLACE', True, (0,0,0))
        text = pygame.transform.rotate(text, 270)
        screen.blit(text, (55, 640))
        text = font.render('(M 140)', True, (0,0,0))
        text = pygame.transform.rotate(text, 270)
        screen.blit(text, (20, 640))


        #adding orange cards

        color = ORANGE


        #   NEW     YORK    AVENUE
        pygame.draw.rect(screen,
                         color,
                         [(CARD_MARGIN+CARD_WIDTH) * 1 - COLOR_RECT_SIZE,
                         (CARD_MARGIN+CARD_HEIGHT) * 1 + CARD_MARGIN,
                         COLOR_RECT_SIZE,
                         CARD_HEIGHT])

        font = pygame.font.SysFont(CARD_TEXT_STYLE, 10)
        text = font.render('NEW YORK', True, (0,0,0))
        text = pygame.transform.rotate(text, 270)
        screen.blit(text, (70, 80))
        text = font.render('AVENUE', True, (0,0,0))
        text = pygame.transform.rotate(text, 270)
        screen.blit(text, (55, 80))
        text = font.render('(M 200)', True, (0,0,0))
        text = pygame.transform.rotate(text, 270)
        screen.blit(text, (20, 80))
        

        #   TENNESSEE   AVENUE
        pygame.draw.rect(screen,
                         color,
                         [(CARD_MARGIN+CARD_WIDTH) * 1 - COLOR_RECT_SIZE,
                         (CARD_MARGIN+CARD_HEIGHT) * 2 + CARD_MARGIN,
                         COLOR_RECT_SIZE,
                         CARD_HEIGHT])
        
        font = pygame.font.SysFont(CARD_TEXT_STYLE, 10)
        text = font.render('TENNESSEE', True, (0,0,0))
        text = pygame.transform.rotate(text, 270)
        screen.blit(text, (70, 150))
        text = font.render('AVENUE', True, (0,0,0))
        text = pygame.transform.rotate(text, 270)
        screen.blit(text, (55, 150))
        text = font.render('(M 180)', True, (0,0,0))
        text = pygame.transform.rotate(text, 270)
        screen.blit(text, (20, 150))


        #   ST. JAMES   PLACE
        pygame.draw.rect(screen,
                         color,
                         [(CARD_MARGIN+CARD_WIDTH) * 1 - COLOR_RECT_SIZE,
                         (CARD_MARGIN+CARD_HEIGHT) * 4 + CARD_MARGIN,
                         COLOR_RECT_SIZE,
                         CARD_HEIGHT])

        font = pygame.font.SysFont(CARD_TEXT_STYLE, 10)
        text = font.render('ST. JAMES', True, (0,0,0))
        text = pygame.transform.rotate(text, 270)
        screen.blit(text, (70, 290))
        text = font.render('PLACE', True, (0,0,0))
        text = pygame.transform.rotate(text, 270)
        screen.blit(text, (55, 290))
        text = font.render('(M 180)', True, (0,0,0))
        text = pygame.transform.rotate(text, 270)
        screen.blit(text, (20, 290))


        #adding red cards

        color = RED

        #   KENTUCKY AVENUE
        pygame.draw.rect(screen,
                         color,
                         [(CARD_MARGIN+CARD_WIDTH) * 1 + CARD_MARGIN,
                         (CARD_MARGIN+CARD_HEIGHT) * 1 - COLOR_RECT_SIZE,
                         CARD_WIDTH,
                         COLOR_RECT_SIZE])

        font = pygame.font.SysFont(CARD_TEXT_STYLE, 10)
        text = font.render('KENTUCKY', True, (0,0,0))
        text = pygame.transform.rotate(text, 180)
        screen.blit(text, (125, 45))
        text = font.render('AVENUE', True, (0,0,0))
        text = pygame.transform.rotate(text, 180)
        screen.blit(text, (125, 30))
        text = font.render('(M 220)', True, (0,0,0))
        text = pygame.transform.rotate(text, 180)
        screen.blit(text, (125, 10))
        

        #   INDIANA AVENUE
        pygame.draw.rect(screen,
                         color,
                         [(CARD_MARGIN+CARD_WIDTH) * 3 + CARD_MARGIN,
                         (CARD_MARGIN+CARD_HEIGHT) * 1 - COLOR_RECT_SIZE,
                         CARD_WIDTH,
                         COLOR_RECT_SIZE])

        font = pygame.font.SysFont(CARD_TEXT_STYLE, 10)
        text = font.render('INDIANA', True, (0,0,0))
        text = pygame.transform.rotate(text, 180)
        screen.blit(text, (325, 45))
        text = font.render('AVENUE', True, (0,0,0))
        text = pygame.transform.rotate(text, 180)
        screen.blit(text, (325, 30))
        text = font.render('(M 220)', True, (0,0,0))
        text = pygame.transform.rotate(text, 180)
        screen.blit(text, (325, 10))


        #   ILLINOIS    AVENUE
        pygame.draw.rect(screen,
                         color,
                         [(CARD_MARGIN+CARD_WIDTH) * 4 + CARD_MARGIN,
                         (CARD_MARGIN+CARD_HEIGHT) * 1 - COLOR_RECT_SIZE,
                         CARD_WIDTH,
                         COLOR_RECT_SIZE])

        font = pygame.font.SysFont(CARD_TEXT_STYLE, 10)
        text = font.render('ILLINOIS', True, (0,0,0))
        text = pygame.transform.rotate(text, 180)
        screen.blit(text, (425, 45))
        text = font.render('AVENUE', True, (0,0,0))
        text = pygame.transform.rotate(text, 180)
        screen.blit(text, (425, 30))
        text = font.render('(M 240)', True, (0,0,0))
        text = pygame.transform.rotate(text, 180)
        screen.blit(text, (425, 10))


        #adding yellow cards

        color = YELLOW


        #   ATLANTIC    AVENUE
        pygame.draw.rect(screen,
                         color,
                         [(CARD_MARGIN+CARD_WIDTH) * 6 + CARD_MARGIN,
                         (CARD_MARGIN+CARD_HEIGHT) * 1 - COLOR_RECT_SIZE,
                         CARD_WIDTH,
                         COLOR_RECT_SIZE])

        font = pygame.font.SysFont(CARD_TEXT_STYLE, 10)
        text = font.render('ATLANTIC', True, (0,0,0))
        text = pygame.transform.rotate(text, 180)
        screen.blit(text, (625, 45))
        text = font.render('AVENUE', True, (0,0,0))
        text = pygame.transform.rotate(text, 180)
        screen.blit(text, (625, 30))
        text = font.render('(M 260)', True, (0,0,0))
        text = pygame.transform.rotate(text, 180)
        screen.blit(text, (625, 10))


        #   VENTORA AVENUE
        pygame.draw.rect(screen,
                         color,
                         [(CARD_MARGIN+CARD_WIDTH) * 7 + CARD_MARGIN,
                         (CARD_MARGIN+CARD_HEIGHT) * 1 - COLOR_RECT_SIZE,
                         CARD_WIDTH,
                         COLOR_RECT_SIZE])

        font = pygame.font.SysFont(CARD_TEXT_STYLE, 10)
        text = font.render('VENTORA', True, (0,0,0))
        text = pygame.transform.rotate(text, 180)
        screen.blit(text, (725, 45))
        text = font.render('AVENUE', True, (0,0,0))
        text = pygame.transform.rotate(text, 180)
        screen.blit(text, (725, 30))
        text = font.render('(M 226)', True, (0,0,0))
        text = pygame.transform.rotate(text, 180)
        screen.blit(text, (725, 10))


        #   MARVIN  GARDENS
        pygame.draw.rect(screen,
                         color,
                         [(CARD_MARGIN+CARD_WIDTH) * 9 + CARD_MARGIN,
                         (CARD_MARGIN+CARD_HEIGHT) * 1 - COLOR_RECT_SIZE,
                         CARD_WIDTH,
                         COLOR_RECT_SIZE])

        font = pygame.font.SysFont(CARD_TEXT_STYLE, 10)
        text = font.render('MARVIN', True, (0,0,0))
        text = pygame.transform.rotate(text, 180)
        screen.blit(text, (925, 45))
        text = font.render('GARDENS', True, (0,0,0))
        text = pygame.transform.rotate(text, 180)
        screen.blit(text, (925, 30))
        text = font.render('(M 280)', True, (0,0,0))
        text = pygame.transform.rotate(text, 180)
        screen.blit(text, (925, 10))


        #adding green cards

        color = GREEN


        #   PACIFIC AVENUE
        pygame.draw.rect(screen,
                         color,
                         [(CARD_MARGIN+CARD_WIDTH) * 10 + CARD_MARGIN,
                         (CARD_MARGIN+CARD_HEIGHT) * 1 + CARD_MARGIN,
                         COLOR_RECT_SIZE,
                         CARD_HEIGHT])

        font = pygame.font.SysFont(CARD_TEXT_STYLE, 10)
        text = font.render('PACIFIC', True, (0,0,0))
        text = pygame.transform.rotate(text, 90)
        screen.blit(text, (1025, 80))
        text = font.render('AVENUE', True, (0,0,0))
        text = pygame.transform.rotate(text, 90)
        screen.blit(text, (1040, 80))
        text = font.render('(M 300)', True, (0,0,0))
        text = pygame.transform.rotate(text, 90)
        screen.blit(text, (1075, 80))


        #   CAROLINA    AVENUE
        pygame.draw.rect(screen,
                         color,
                         [(CARD_MARGIN+CARD_WIDTH) * 10 + CARD_MARGIN,
                         (CARD_MARGIN+CARD_HEIGHT) * 2 + CARD_MARGIN,
                         COLOR_RECT_SIZE,
                         CARD_HEIGHT])

        font = pygame.font.SysFont(CARD_TEXT_STYLE, 10)
        text = font.render('CAROLINA', True, (0,0,0))
        text = pygame.transform.rotate(text, 90)
        screen.blit(text, (1025, 150))
        text = font.render('AVENUE', True, (0,0,0))
        text = pygame.transform.rotate(text, 90)
        screen.blit(text, (1040, 150))
        text = font.render('(M 300)', True, (0,0,0))
        text = pygame.transform.rotate(text, 90)
        screen.blit(text, (1075, 150))


        #   PENNSYLVANIA    AVENUE
        pygame.draw.rect(screen,
                         color,
                         [(CARD_MARGIN+CARD_WIDTH) * 10 + CARD_MARGIN,
                         (CARD_MARGIN+CARD_HEIGHT) * 4 + CARD_MARGIN,
                         COLOR_RECT_SIZE,
                         CARD_HEIGHT])

        font = pygame.font.SysFont(CARD_TEXT_STYLE, 10)
        text = font.render('PENNSYLVA-', True, (0,0,0))
        text = pygame.transform.rotate(text, 90)
        screen.blit(text, (1025, 290))
        text = font.render('NIA AVENUE', True, (0,0,0))
        text = pygame.transform.rotate(text, 90)
        screen.blit(text, (1040, 290))
        text = font.render('(M 320)', True, (0,0,0))
        text = pygame.transform.rotate(text, 90)
        screen.blit(text, (1075, 290))


        #adding blue cards

        color = BLUE


        #   PARK    PLACE
        pygame.draw.rect(screen,
                         color,
                         [(CARD_MARGIN+CARD_WIDTH) * 10 + CARD_MARGIN,
                         (CARD_MARGIN+CARD_HEIGHT) * 7 + CARD_MARGIN,
                         COLOR_RECT_SIZE,
                         CARD_HEIGHT])

        font = pygame.font.SysFont(CARD_TEXT_STYLE, 10)
        text = font.render('PARK', True, (0,0,0))
        text = pygame.transform.rotate(text, 90)
        screen.blit(text, (1025, 500))
        text = font.render('PLACE', True, (0,0,0))
        text = pygame.transform.rotate(text, 90)
        screen.blit(text, (1040, 500))
        text = font.render('(M 350)', True, (0,0,0))
        text = pygame.transform.rotate(text, 90)
        screen.blit(text, (1075, 500))


        #   BROADWALK
        pygame.draw.rect(screen,
                         color,
                         [(CARD_MARGIN+CARD_WIDTH) * 10 + CARD_MARGIN,
                         (CARD_MARGIN+CARD_HEIGHT) * 9 + CARD_MARGIN,
                         COLOR_RECT_SIZE,
                         CARD_HEIGHT])

        font = pygame.font.SysFont(CARD_TEXT_STYLE, 10)
        text = font.render('BROAD-', True, (0,0,0))
        text = pygame.transform.rotate(text, 90)
        screen.blit(text, (1025, 640))
        text = font.render('WALK', True, (0,0,0))
        text = pygame.transform.rotate(text, 90)
        screen.blit(text, (1040, 640))
        text = font.render('(M 400)', True, (0,0,0))
        text = pygame.transform.rotate(text, 90)
        screen.blit(text, (1075, 640))

        #adding COMMUNITY CHEST CARDS


        #   COM CHEST 1
        font = pygame.font.SysFont(CARD_TEXT_STYLE, 10)
        screen.blit(font.render('COMMUNITY', True, (0,0,0)), (808, 720))
        screen.blit(font.render('CHEST', True, (0,0,0)), (808, 735))
        font = pygame.font.SysFont(CARD_TEXT_STYLE, 20)
        screen.blit(font.render('$', True, (0,0,0)), (845, 745))


        #   COM CHEST 2
        font = pygame.font.SysFont(CARD_TEXT_STYLE, 10)
        text = font.render('COMMUNITY', True, (0,0,0))
        text = pygame.transform.rotate(text, 270)
        screen.blit(text, (70, 219))
        text = font.render('CHEST', True, (0,0,0))
        text = pygame.transform.rotate(text, 270)
        screen.blit(text, (55, 219))
        font = pygame.font.SysFont(CARD_TEXT_STYLE, 30)
        text = font.render('$', True, (0,0,0))
        text = pygame.transform.rotate(text, 270)
        screen.blit(text, (10, 240))


        #   COM CHEST 3
        font = pygame.font.SysFont(CARD_TEXT_STYLE, 10)
        text = font.render('COMMUNITY', True, (0,0,0))
        text = pygame.transform.rotate(text, 90)
        screen.blit(text, (1025, 219))
        text = font.render('CHEST', True, (0,0,0))
        text = pygame.transform.rotate(text, 90)
        screen.blit(text, (1040, 219))
        font = pygame.font.SysFont(CARD_TEXT_STYLE, 30)
        text = font.render('$', True, (0,0,0))
        text = pygame.transform.rotate(text, 90)
        screen.blit(text, (1065, 240))


        #adding CHANCE CARDS


        #   CHANCE 1
        font = pygame.font.SysFont(CARD_TEXT_STYLE, 10)
        screen.blit(font.render('CHANCE', True, (0,0,0)), (308, 720))
        font = pygame.font.SysFont(CARD_TEXT_STYLE, 25)
        screen.blit(font.render('?', True, (0,0,0)), (345, 745))


        #   CHANCE 2
        font = pygame.font.SysFont(CARD_TEXT_STYLE, 10)
        text = font.render('CHANCE', True, (0,0,0))
        text = pygame.transform.rotate(text, 180)
        screen.blit(text, (225, 45))
        font = pygame.font.SysFont(CARD_TEXT_STYLE, 30)
        text = font.render('?', True, (0,0,0))
        text = pygame.transform.rotate(text, 180)
        screen.blit(text, (245, 10))


        #   CHANCE 3
        font = pygame.font.SysFont(CARD_TEXT_STYLE, 10)
        text = font.render('CHANCE', True, (0,0,0))
        text = pygame.transform.rotate(text, 90)
        screen.blit(text, (1025, 429))
        font = pygame.font.SysFont(CARD_TEXT_STYLE, 30)
        text = font.render('?', True, (0,0,0))
        text = pygame.transform.rotate(text, 90)
        screen.blit(text, (1065, 450))

        #adding JAIL,GO AND FREE PARKING


        #   GO
        font = pygame.font.SysFont(CARD_TEXT_STYLE, 6)
        screen.blit(font.render('(COLLECT M220 AS YOU PASS)', True, (0,0,0)), (1008, 710))
        font = pygame.font.SysFont(CARD_TEXT_STYLE, 25)
        text = font.render('GO', True, (0,0,0))
        text = pygame.transform.rotate(text, 45)
        screen.blit(text, (1028, 715))
        screen.blit(font.render('<------<', True, (0,0,0)), (1008, 745))


        #   IN JAIL
        font = pygame.font.SysFont(CARD_TEXT_STYLE, 20)
        text = font.render('IN', True, (0,0,0))
        text = pygame.transform.rotate(text, 315)
        screen.blit(text, (55, 705))
        text = font.render('JAIL', True, (0,0,0))
        text = pygame.transform.rotate(text, 315)
        screen.blit(text, (30, 715))


        #   GO  TO  JAIL
        font = pygame.font.SysFont(CARD_TEXT_STYLE, 20)
        text = font.render('GO TO', True, (0,0,0))
        text = pygame.transform.rotate(text, 135)
        screen.blit(text, (1002, 2))
        text = font.render('JAIL', True, (0,0,0))
        text = pygame.transform.rotate(text, 135)
        screen.blit(text, (1045, 5))


        #   FREE    PARKING
        font = pygame.font.SysFont(CARD_TEXT_STYLE, 15)
        text = font.render('FREE', True, (0,0,0))
        text = pygame.transform.rotate(text, 225)
        screen.blit(text, (65, 5))
        text = font.render('PARKING', True, (0,0,0))
        text = pygame.transform.rotate(text, 225)
        screen.blit(text, (5, 5))



        #adding RAILROAD


        #   READING RAILROAD
        font = pygame.font.SysFont(CARD_TEXT_STYLE, 10)
        screen.blit(font.render('READING', True, (0,0,0)), (508, 720))
        screen.blit(font.render('RAILROAD', True, (0,0,0)), (508, 735))
        screen.blit(font.render('(M 200)', True, (0,0,0)), (508, 755))


        #   PENNSYLVANIA    RAILROAD
        font = pygame.font.SysFont(CARD_TEXT_STYLE, 8)
        text = font.render('PENNSYLVANIA', True, (0,0,0))
        text = pygame.transform.rotate(text, 270)
        screen.blit(text, (70, 360))
        text = font.render('RAILROAD', True, (0,0,0))
        text = pygame.transform.rotate(text, 270)
        screen.blit(text, (55, 360))
        text = font.render('(M 200)', True, (0,0,0))
        text = pygame.transform.rotate(text, 270)
        screen.blit(text, (20, 360))


        #   B. & O. RAILROAD
        font = pygame.font.SysFont(CARD_TEXT_STYLE, 10)
        text = font.render('B. & O.', True, (0,0,0))
        text = pygame.transform.rotate(text, 180)
        screen.blit(text, (525, 45))
        text = font.render('RAILROAD', True, (0,0,0))
        text = pygame.transform.rotate(text, 180)
        screen.blit(text, (525, 30))
        text = font.render('(M 200)', True, (0,0,0))
        text = pygame.transform.rotate(text, 180)
        screen.blit(text, (525, 10))


        #   SHORT   LINE
        font = pygame.font.SysFont(CARD_TEXT_STYLE, 10)
        text = font.render('SHORT', True, (0,0,0))
        text = pygame.transform.rotate(text, 90)
        screen.blit(text, (1025, 360))
        text = font.render('LINE', True, (0,0,0))
        text = pygame.transform.rotate(text, 90)
        screen.blit(text, (1040, 360))
        text = font.render('(M 200)', True, (0,0,0))
        text = pygame.transform.rotate(text, 90)
        screen.blit(text, (1075, 360))


        #adding TAX PAY CARDS


        #   INCOME  TAX
        font = pygame.font.SysFont(CARD_TEXT_STYLE, 10)
        screen.blit(font.render('INCOME', True, (0,0,0)), (608, 720))
        screen.blit(font.render('TAX', True, (0,0,0)), (608, 735))
        screen.blit(font.render('(PAY M.200)', True, (0,0,0)), (608, 755))


        #   LUXURY  TAX
        font = pygame.font.SysFont(CARD_TEXT_STYLE, 10)
        text = font.render('LUXURY', True, (0,0,0))
        text = pygame.transform.rotate(text, 90)
        screen.blit(text, (1025, 570))
        text = font.render('TAX', True, (0,0,0))
        text = pygame.transform.rotate(text, 90)
        screen.blit(text, (1040, 570))
        text = font.render('(PAY M.200)', True, (0,0,0))
        text = pygame.transform.rotate(text, 90)
        screen.blit(text, (1075, 570))


        #adding GOVERNEMENT CARDS


        #   ELECTRIC    COMPANY
        font = pygame.font.SysFont(CARD_TEXT_STYLE, 10)
        text = font.render('ELECTRIC', True, (0,0,0))
        text = pygame.transform.rotate(text, 270)
        screen.blit(text, (70, 570))
        text = font.render('COMPANY', True, (0,0,0))
        text = pygame.transform.rotate(text, 270)
        screen.blit(text, (55, 570))
        text = font.render('(M 150)', True, (0,0,0))
        text = pygame.transform.rotate(text, 270)
        screen.blit(text, (20, 570))

        
        #   WATER   WORKS
        font = pygame.font.SysFont(CARD_TEXT_STYLE, 10)
        text = font.render('WATER', True, (0,0,0))
        text = pygame.transform.rotate(text, 180)
        screen.blit(text, (825, 45))
        text = font.render('WORKS', True, (0,0,0))
        text = pygame.transform.rotate(text, 180)
        screen.blit(text, (825, 30))
        text = font.render('(M 150)', True, (0,0,0))
        text = pygame.transform.rotate(text, 180)
        screen.blit(text, (825, 10))


        
        

# -------------------MAIN GAME FUNTION---------------
def run_game():
    done = False

    clock = pygame.time.Clock()

    #--------------MAIN GAME LOOP------------------
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            elif event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                col = pos[0] // (CARD_WIDTH + CARD_MARGIN)
                row = pos[1] // (CARD_HEIGHT + CARD_MARGIN)

                grid[row][col] = 1
                print("Click ", pos, "Grid coordinates : ", row, col)


        create_board()
        

        clock.tick(60)

        pygame.display.update()


    pygame.quit()

#---------------MODULE END---------
    
#--------------CODE----------------

if __name__ == '__main__':
    grid=[]
    for row in range(BOARD_ROWS):
        grid.append([])
        for col in range(BOARD_COLS):
            grid[row].append(0)

    pygame.init()

    WINDOW_SIZE = [SCREEN_WIDTH,SCREEN_HEIGHT]
    screen = pygame.display.set_mode(WINDOW_SIZE)

    pygame.display.set_caption("MONOPOLY")

    run_game()
                                  


    
    
