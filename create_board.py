

import pygame
from random import *
from pygame.locals import *

from variables import *
from Card import *


# --------------CREATE BOARD FUNCTION--------------
# creates the board and all the cards inside it


def create_board(screen):

    screen.fill(BACKGROUND_COLOR)

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
    


    # horizontal and vertical margin

    pygame.draw.line(screen, WHITE, (0,BOARD_HEIGHT + OPTION_BOARD_SPACING/2), (SCREEN_WIDTH,BOARD_HEIGHT + OPTION_BOARD_SPACING/2))
    
    pygame.draw.line(screen, WHITE, (BOARD_WIDTH + INFO_BOARD_SPACING/2,0), (BOARD_WIDTH + INFO_BOARD_SPACING/2,BOARD_HEIGHT + OPTION_BOARD_SPACING/2))


    # Monopoly man image
    
    manImg = pygame.image.load('man.png')
    screen.blit(manImg,(350,320))


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
    screen.blit(font.render('MEDITERRANEAN', True, BLACK), (908, 720))
    screen.blit(font.render('AVENUE', True, BLACK), (908, 735))
    screen.blit(font.render('(M 60)', True, BLACK), (908, 755))
    
    
    #   BALTIC  AVENUE
    pygame.draw.rect(screen,
                     color,
                     [(CARD_MARGIN+CARD_WIDTH) * 7 + CARD_MARGIN,
                     (CARD_MARGIN+CARD_HEIGHT) * 10 + CARD_MARGIN,
                     CARD_WIDTH,
                     COLOR_RECT_SIZE])

    font = pygame.font.SysFont(CARD_TEXT_STYLE, 10)
    screen.blit(font.render('BALTIC', True, BLACK), (708, 720))
    screen.blit(font.render('AVENUE', True, BLACK), (708, 735))
    screen.blit(font.render('(M 80)', True, BLACK), (708, 755))


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
    screen.blit(font.render('CONNECTICUT', True, BLACK), (108, 720))
    screen.blit(font.render('AVENUE', True, BLACK), (108, 735))
    screen.blit(font.render('(M 120)', True, BLACK), (108, 755))


    #   VERMONT AVENUE
    pygame.draw.rect(screen,
                     color,
                     [(CARD_MARGIN+CARD_WIDTH) * 2 + CARD_MARGIN,
                     (CARD_MARGIN+CARD_HEIGHT) * 10 + CARD_MARGIN,
                     CARD_WIDTH,
                     COLOR_RECT_SIZE])

    font = pygame.font.SysFont(CARD_TEXT_STYLE, 10)
    screen.blit(font.render('VERMONT', True, BLACK), (208, 720))
    screen.blit(font.render('AVENUE', True, BLACK), (208, 735))
    screen.blit(font.render('(M 100)', True, BLACK), (208, 755))


    #   ORIENTAL AVENUE
    pygame.draw.rect(screen,
                     color,
                     [(CARD_MARGIN+CARD_WIDTH) * 4 + CARD_MARGIN,
                     (CARD_MARGIN+CARD_HEIGHT) * 10 + CARD_MARGIN,
                     CARD_WIDTH,
                     COLOR_RECT_SIZE])

    font = pygame.font.SysFont(CARD_TEXT_STYLE, 10)
    screen.blit(font.render('ORIENTAL', True, BLACK), (408, 720))
    screen.blit(font.render('AVENUE', True, BLACK), (408, 735))
    screen.blit(font.render('(M 100)', True, BLACK), (408, 755))



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
    text = font.render('VIRGINIA', True, BLACK)
    text = pygame.transform.rotate(text, 270)
    screen.blit(text, (70, 430))
    text = font.render('AVENUE', True, BLACK)
    text = pygame.transform.rotate(text, 270)
    screen.blit(text, (55, 430))
    text = font.render('(M 160)', True, BLACK)
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
    text = font.render('STATES', True, BLACK)
    text = pygame.transform.rotate(text, 270)
    screen.blit(text, (70, 500))
    text = font.render('AVENUE', True, BLACK)
    text = pygame.transform.rotate(text, 270)
    screen.blit(text, (55, 500))
    text = font.render('(M 140)', True, BLACK)
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
    text = font.render('ST. CHARLES', True, BLACK)
    text = pygame.transform.rotate(text, 270)
    screen.blit(text, (70, 640))
    text = font.render('PLACE', True, BLACK)
    text = pygame.transform.rotate(text, 270)
    screen.blit(text, (55, 640))
    text = font.render('(M 140)', True, BLACK)
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
    text = font.render('NEW YORK', True, BLACK)
    text = pygame.transform.rotate(text, 270)
    screen.blit(text, (70, 80))
    text = font.render('AVENUE', True, BLACK)
    text = pygame.transform.rotate(text, 270)
    screen.blit(text, (55, 80))
    text = font.render('(M 200)', True, BLACK)
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
    text = font.render('TENNESSEE', True, BLACK)
    text = pygame.transform.rotate(text, 270)
    screen.blit(text, (70, 150))
    text = font.render('AVENUE', True, BLACK)
    text = pygame.transform.rotate(text, 270)
    screen.blit(text, (55, 150))
    text = font.render('(M 180)', True, BLACK)
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
    text = font.render('ST. JAMES', True, BLACK)
    text = pygame.transform.rotate(text, 270)
    screen.blit(text, (70, 290))
    text = font.render('PLACE', True, BLACK)
    text = pygame.transform.rotate(text, 270)
    screen.blit(text, (55, 290))
    text = font.render('(M 180)', True, BLACK)
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
    text = font.render('KENTUCKY', True, BLACK)
    text = pygame.transform.rotate(text, 180)
    screen.blit(text, (125, 45))
    text = font.render('AVENUE', True, BLACK)
    text = pygame.transform.rotate(text, 180)
    screen.blit(text, (125, 30))
    text = font.render('(M 220)', True, BLACK)
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
    text = font.render('INDIANA', True, BLACK)
    text = pygame.transform.rotate(text, 180)
    screen.blit(text, (325, 45))
    text = font.render('AVENUE', True, BLACK)
    text = pygame.transform.rotate(text, 180)
    screen.blit(text, (325, 30))
    text = font.render('(M 220)', True, BLACK)
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
    text = font.render('ILLINOIS', True, BLACK)
    text = pygame.transform.rotate(text, 180)
    screen.blit(text, (425, 45))
    text = font.render('AVENUE', True, BLACK)
    text = pygame.transform.rotate(text, 180)
    screen.blit(text, (425, 30))
    text = font.render('(M 240)', True, BLACK)
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
    text = font.render('ATLANTIC', True, BLACK)
    text = pygame.transform.rotate(text, 180)
    screen.blit(text, (625, 45))
    text = font.render('AVENUE', True, BLACK)
    text = pygame.transform.rotate(text, 180)
    screen.blit(text, (625, 30))
    text = font.render('(M 260)', True, BLACK)
    text = pygame.transform.rotate(text, 180)
    screen.blit(text, (625, 10))


    #   VENTNOR AVENUE
    pygame.draw.rect(screen,
                     color,
                     [(CARD_MARGIN+CARD_WIDTH) * 7 + CARD_MARGIN,
                     (CARD_MARGIN+CARD_HEIGHT) * 1 - COLOR_RECT_SIZE,
                     CARD_WIDTH,
                     COLOR_RECT_SIZE])

    font = pygame.font.SysFont(CARD_TEXT_STYLE, 10)
    text = font.render('VENTNOR', True, BLACK)
    text = pygame.transform.rotate(text, 180)
    screen.blit(text, (725, 45))
    text = font.render('AVENUE', True, BLACK)
    text = pygame.transform.rotate(text, 180)
    screen.blit(text, (725, 30))
    text = font.render('(M 226)', True, BLACK)
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
    text = font.render('MARVIN', True, BLACK)
    text = pygame.transform.rotate(text, 180)
    screen.blit(text, (925, 45))
    text = font.render('GARDENS', True, BLACK)
    text = pygame.transform.rotate(text, 180)
    screen.blit(text, (925, 30))
    text = font.render('(M 280)', True, BLACK)
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
    text = font.render('PACIFIC', True, BLACK)
    text = pygame.transform.rotate(text, 90)
    screen.blit(text, (1025, 80))
    text = font.render('AVENUE', True, BLACK)
    text = pygame.transform.rotate(text, 90)
    screen.blit(text, (1040, 80))
    text = font.render('(M 300)', True, BLACK)
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
    text = font.render('CAROLINA', True, BLACK)
    text = pygame.transform.rotate(text, 90)
    screen.blit(text, (1025, 150))
    text = font.render('AVENUE', True, BLACK)
    text = pygame.transform.rotate(text, 90)
    screen.blit(text, (1040, 150))
    text = font.render('(M 300)', True, BLACK)
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
    text = font.render('PENNSYLVA-', True, BLACK)
    text = pygame.transform.rotate(text, 90)
    screen.blit(text, (1025, 290))
    text = font.render('NIA AVENUE', True, BLACK)
    text = pygame.transform.rotate(text, 90)
    screen.blit(text, (1040, 290))
    text = font.render('(M 320)', True, BLACK)
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
    text = font.render('PARK', True, BLACK)
    text = pygame.transform.rotate(text, 90)
    screen.blit(text, (1025, 500))
    text = font.render('PLACE', True, BLACK)
    text = pygame.transform.rotate(text, 90)
    screen.blit(text, (1040, 500))
    text = font.render('(M 350)', True, BLACK)
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
    text = font.render('BROAD-', True, BLACK)
    text = pygame.transform.rotate(text, 90)
    screen.blit(text, (1025, 640))
    text = font.render('WALK', True, BLACK)
    text = pygame.transform.rotate(text, 90)
    screen.blit(text, (1040, 640))
    text = font.render('(M 400)', True, BLACK)
    text = pygame.transform.rotate(text, 90)
    screen.blit(text, (1075, 640))

    #adding COMMUNITY CHEST CARDS


    #   COM CHEST 1
    font = pygame.font.SysFont(CARD_TEXT_STYLE, 10)
    screen.blit(font.render('COMMUNITY', True, BLACK), (808, 720))
    screen.blit(font.render('CHEST', True, BLACK), (808, 735))
    font = pygame.font.SysFont(CARD_TEXT_STYLE, 20)
    screen.blit(font.render('$', True, BLACK), (845, 745))


    #   COM CHEST 2
    font = pygame.font.SysFont(CARD_TEXT_STYLE, 10)
    text = font.render('COMMUNITY', True, BLACK)
    text = pygame.transform.rotate(text, 270)
    screen.blit(text, (70, 219))
    text = font.render('CHEST', True, BLACK)
    text = pygame.transform.rotate(text, 270)
    screen.blit(text, (55, 219))
    font = pygame.font.SysFont(CARD_TEXT_STYLE, 30)
    text = font.render('$', True, BLACK)
    text = pygame.transform.rotate(text, 270)
    screen.blit(text, (10, 240))


    #   COM CHEST 3
    font = pygame.font.SysFont(CARD_TEXT_STYLE, 10)
    text = font.render('COMMUNITY', True, BLACK)
    text = pygame.transform.rotate(text, 90)
    screen.blit(text, (1025, 219))
    text = font.render('CHEST', True, BLACK)
    text = pygame.transform.rotate(text, 90)
    screen.blit(text, (1040, 219))
    font = pygame.font.SysFont(CARD_TEXT_STYLE, 30)
    text = font.render('$', True, BLACK)
    text = pygame.transform.rotate(text, 90)
    screen.blit(text, (1065, 240))


    #adding CHANCE CARDS


    #   CHANCE 1
    font = pygame.font.SysFont(CARD_TEXT_STYLE, 10)
    screen.blit(font.render('CHANCE', True, BLACK), (308, 720))
    font = pygame.font.SysFont(CARD_TEXT_STYLE, 25)
    screen.blit(font.render('?', True, BLACK), (345, 745))


    #   CHANCE 2
    font = pygame.font.SysFont(CARD_TEXT_STYLE, 10)
    text = font.render('CHANCE', True, BLACK)
    text = pygame.transform.rotate(text, 180)
    screen.blit(text, (225, 45))
    font = pygame.font.SysFont(CARD_TEXT_STYLE, 30)
    text = font.render('?', True, BLACK)
    text = pygame.transform.rotate(text, 180)
    screen.blit(text, (245, 10))


    #   CHANCE 3
    font = pygame.font.SysFont(CARD_TEXT_STYLE, 10)
    text = font.render('CHANCE', True, BLACK)
    text = pygame.transform.rotate(text, 90)
    screen.blit(text, (1025, 429))
    font = pygame.font.SysFont(CARD_TEXT_STYLE, 30)
    text = font.render('?', True, BLACK)
    text = pygame.transform.rotate(text, 90)
    screen.blit(text, (1065, 450))

    #adding JAIL,GO AND FREE PARKING


    #   GO
    font = pygame.font.SysFont(CARD_TEXT_STYLE, 6)
    screen.blit(font.render('(COLLECT M220 AS YOU PASS)', True, BLACK), (1008, 710))
    font = pygame.font.SysFont(CARD_TEXT_STYLE, 25)
    text = font.render('GO', True, BLACK)
    text = pygame.transform.rotate(text, 45)
    screen.blit(text, (1028, 715))
    screen.blit(font.render('<------<', True, BLACK), (1008, 745))


    #   IN JAIL
    font = pygame.font.SysFont(CARD_TEXT_STYLE, 20)
    text = font.render('IN', True, BLACK)
    text = pygame.transform.rotate(text, 315)
    screen.blit(text, (55, 705))
    text = font.render('JAIL', True, BLACK)
    text = pygame.transform.rotate(text, 315)
    screen.blit(text, (30, 715))


    #   GO  TO  JAIL
    font = pygame.font.SysFont(CARD_TEXT_STYLE, 20)
    text = font.render('GO TO', True, BLACK)
    text = pygame.transform.rotate(text, 135)
    screen.blit(text, (1002, 2))
    text = font.render('JAIL', True, BLACK)
    text = pygame.transform.rotate(text, 135)
    screen.blit(text, (1045, 5))


    #   FREE    PARKING
    font = pygame.font.SysFont(CARD_TEXT_STYLE, 15)
    text = font.render('FREE', True, BLACK)
    text = pygame.transform.rotate(text, 225)
    screen.blit(text, (65, 5))
    text = font.render('PARKING', True, BLACK)
    text = pygame.transform.rotate(text, 225)
    screen.blit(text, (5, 5))



    #adding RAILROAD


    #   READING RAILROAD
    font = pygame.font.SysFont(CARD_TEXT_STYLE, 10)
    screen.blit(font.render('READING', True, BLACK), (508, 720))
    screen.blit(font.render('RAILROAD', True, BLACK), (508, 735))
    screen.blit(font.render('(M 200)', True, BLACK), (508, 755))


    #   PENNSYLVANIA    RAILROAD
    font = pygame.font.SysFont(CARD_TEXT_STYLE, 8)
    text = font.render('PENNSYLVANIA', True, BLACK)
    text = pygame.transform.rotate(text, 270)
    screen.blit(text, (70, 360))
    text = font.render('RAILROAD', True, BLACK)
    text = pygame.transform.rotate(text, 270)
    screen.blit(text, (55, 360))
    text = font.render('(M 200)', True, BLACK)
    text = pygame.transform.rotate(text, 270)
    screen.blit(text, (20, 360))


    #   B. & O. RAILROAD
    font = pygame.font.SysFont(CARD_TEXT_STYLE, 10)
    text = font.render('B. & O.', True, BLACK)
    text = pygame.transform.rotate(text, 180)
    screen.blit(text, (525, 45))
    text = font.render('RAILROAD', True, BLACK)
    text = pygame.transform.rotate(text, 180)
    screen.blit(text, (525, 30))
    text = font.render('(M 200)', True, BLACK)
    text = pygame.transform.rotate(text, 180)
    screen.blit(text, (525, 10))


    #   SHORT   LINE
    font = pygame.font.SysFont(CARD_TEXT_STYLE, 10)
    text = font.render('SHORT', True, BLACK)
    text = pygame.transform.rotate(text, 90)
    screen.blit(text, (1025, 360))
    text = font.render('LINE', True, BLACK)
    text = pygame.transform.rotate(text, 90)
    screen.blit(text, (1040, 360))
    text = font.render('(M 200)', True, BLACK)
    text = pygame.transform.rotate(text, 90)
    screen.blit(text, (1075, 360))


    #adding TAX PAY CARDS


    #   INCOME  TAX
    font = pygame.font.SysFont(CARD_TEXT_STYLE, 10)
    screen.blit(font.render('INCOME', True, BLACK), (608, 720))
    screen.blit(font.render('TAX', True, BLACK), (608, 735))
    screen.blit(font.render('(PAY M.200)', True, BLACK), (608, 755))


    #   LUXURY  TAX
    font = pygame.font.SysFont(CARD_TEXT_STYLE, 10)
    text = font.render('LUXURY', True, BLACK)
    text = pygame.transform.rotate(text, 90)
    screen.blit(text, (1025, 570))
    text = font.render('TAX', True, BLACK)
    text = pygame.transform.rotate(text, 90)
    screen.blit(text, (1040, 570))
    text = font.render('(PAY M.200)', True, BLACK)
    text = pygame.transform.rotate(text, 90)
    screen.blit(text, (1075, 570))


    #adding GOVERNEMENT CARDS


    #   ELECTRIC    COMPANY
    font = pygame.font.SysFont(CARD_TEXT_STYLE, 10)
    text = font.render('ELECTRIC', True, BLACK)
    text = pygame.transform.rotate(text, 270)
    screen.blit(text, (70, 570))
    text = font.render('COMPANY', True, BLACK)
    text = pygame.transform.rotate(text, 270)
    screen.blit(text, (55, 570))
    text = font.render('(M 150)', True, BLACK)
    text = pygame.transform.rotate(text, 270)
    screen.blit(text, (20, 570))

    
    #   WATER   WORKS
    font = pygame.font.SysFont(CARD_TEXT_STYLE, 10)
    text = font.render('WATER', True, BLACK)
    text = pygame.transform.rotate(text, 180)
    screen.blit(text, (825, 45))
    text = font.render('WORKS', True, BLACK)
    text = pygame.transform.rotate(text, 180)
    screen.blit(text, (825, 30))
    text = font.render('(M 150)', True, BLACK)
    text = pygame.transform.rotate(text, 180)
    screen.blit(text, (825, 10))


 
# Rolls dice and places them at random positions
# Generates random number between 1 and 6 for each die
# DICE
# dice 1 boundary ( 150 <= x <= 500  80 <= y <= 280 )
# dice 2 boundart ( 550 <= x <= 900  80 <= y <= 280 )
# dice width = dice height = 35
# spot radius = 5



def roll_dice(screen,no1=0,no2=0):

    if True:            # because I'm too lazy to indent all the lines below ;)

        dice1_x = randint(150,500)
        dice1_y = randint(80,280)

        # draw dice 1 
        
        pygame.draw.rect(screen,
                         WHITE,
                         ((dice1_x,dice1_y),
                         (DICE_WIDTH,DICE_HEIGHT)))

        # draw spots for dice 1

        if no1 == 0:
            no1 = randint(1,6)

        # for odd no draw a spot in center of dice
        
        if no1 % 2 == 1:
            pygame.draw.circle(screen,
                               BLACK,
                               (dice1_x + 17,dice1_y + 17),
                               DICE_SPOT_RADIUS)

        # 1 - center 
        # 2 - left-top right-bottom
        # 3 - left-top right-bottom center
        # 4 - left-top right-top left-bottom right-bottom
        # 5 - left-top right-top left-bottom right-bottom center
        # 6 - left-top right-top left-bottom right-bottom middle-top middle-bottom

        # for 2 to 6 draw left-top and right-bottom
        
        if no1 >= 2 and no1 <= 6:
            pygame.draw.circle(screen,
                               BLACK,
                               (dice1_x + 7,dice1_y + 7),
                               DICE_SPOT_RADIUS)


            pygame.draw.circle(screen,
                               BLACK,
                               (dice1_x + 27,dice1_y + 27),
                               DICE_SPOT_RADIUS)


        # for 4 to 6 draw left-bottom and right-top

        if no1 >= 4 and no1 <= 6:
            pygame.draw.circle(screen,
                               BLACK,
                               (dice1_x + 7,dice1_y + 27),
                               DICE_SPOT_RADIUS)


            pygame.draw.circle(screen,
                               BLACK,
                               (dice1_x + 27,dice1_y + 7),
                               DICE_SPOT_RADIUS)
            


        # for 6 draw middle-top and middle-bottom
        
        if no1 == 6:
            pygame.draw.circle(screen,
                               BLACK,
                               (dice1_x + 17,dice1_y + 7),
                               DICE_SPOT_RADIUS)


            pygame.draw.circle(screen,
                               BLACK,
                               (dice1_x + 17,dice1_y + 27),
                               DICE_SPOT_RADIUS)





    if True:            # because I'm too lazy to indent all the lines below ;)

        dice2_x = randint(550,900)
        dice2_y = randint(80,280)

        # draw dice 2 
        
        pygame.draw.rect(screen,
                         WHITE,
                         ((dice2_x,dice2_y),
                         (DICE_WIDTH,DICE_HEIGHT)))

        # draw spots for dice 1

        if no2 == 0:
            if no1 >3:
                no2 = randint(1,3)
            else:
                no2 = randint(1,6)

        # for odd no draw a spot in center of dice
        
        if no2 % 2 == 1:
            pygame.draw.circle(screen,
                               BLACK,
                               (dice2_x + 17,dice2_y + 17),
                               DICE_SPOT_RADIUS)

        # 1 - center 
        # 2 - left-top right-bottom
        # 3 - left-top right-bottom center
        # 4 - left-top right-top left-bottom right-bottom
        # 5 - left-top right-top left-bottom right-bottom center
        # 6 - left-top right-top left-bottom right-bottom middle-top middle-bottom

        # for 2 to 6 draw left-top and right-bottom
        
        if no2 >= 2 and no2 <= 6:
            pygame.draw.circle(screen,
                               BLACK,
                               (dice2_x + 7,dice2_y + 7),
                               DICE_SPOT_RADIUS)


            pygame.draw.circle(screen,
                               BLACK,
                               (dice2_x + 27,dice2_y + 27),
                               DICE_SPOT_RADIUS)


        # for 4 to 6 draw left-bottom and right-top

        if no2 >= 4 and no2 <= 6:
            pygame.draw.circle(screen,
                               BLACK,
                               (dice2_x + 7,dice2_y + 27),
                               DICE_SPOT_RADIUS)


            pygame.draw.circle(screen,
                               BLACK,
                               (dice2_x + 27,dice2_y + 7),
                               DICE_SPOT_RADIUS)
            


        # for 6 draw middle-top and middle-bottom
        
        if no2 == 6:
            pygame.draw.circle(screen,
                               BLACK,
                               (dice2_x + 17,dice2_y + 7),
                               DICE_SPOT_RADIUS)


            pygame.draw.circle(screen,
                               BLACK,
                               (dice2_x + 17,dice2_y + 27),
                               DICE_SPOT_RADIUS)

    return no1,no2


# creating the cards
# creating cards rectangles for handling events on them

def create_card_rects():
    

    Cards = []
    Rects = []

    # card - id_no,name,color,cost,rent,mortgage_value,house_cost,hotel_cost,house_rent,hotel_rent,board_pos,info_pos
    # rect - left,top,width,height

    card = Card(0,"GO","",0,0,0,0,0,[],0,(1001,701),())
    Cards.append(card)
    rect = pygame.Rect((1001,701),(CARD_WIDTH,CARD_HEIGHT))
    Rects.append(rect)
    
    card = Card(1,"MEDITARREANEAN AVENUE","BROWN",60,2,30,50,50,[10,30,90,160],250,(901,701),(1380,350))
    Cards.append(card)
    rect = pygame.Rect((901,701),(CARD_WIDTH,CARD_HEIGHT))
    Rects.append(rect)

    
    card = Card(2,"COMMUNITY CHEST","",0,0,0,0,0,[],0,(801,701),())
    Cards.append(card)
    rect = pygame.Rect((801,701),(CARD_WIDTH,CARD_HEIGHT))
    Rects.append(rect)


    card = Card(3,"BALTIC AVENUE","BROWN",80,4,30,50,50,[20,60,80,320],450,(701,701),(1330,350))
    Cards.append(card)
    rect = pygame.Rect((701,701),(CARD_WIDTH,CARD_HEIGHT))
    Rects.append(rect)


    card = Card(4,"INCOME TAX","",0,0,0,0,0,[],0,(601,701),())
    Cards.append(card)
    rect = pygame.Rect((601,701),(CARD_WIDTH,CARD_HEIGHT))
    Rects.append(rect)


    card = Card(5,"READING RAILROAD","BLACK",200,25,100,0,0,[],0,(501,701),(1280,350))
    Cards.append(card)
    rect = pygame.Rect((501,701),(CARD_WIDTH,CARD_HEIGHT))
    Rects.append(rect)


    card = Card(6,"ORIENTAL AVENUE","LIGHT_BLUE",100,6,50,50,50,[30,90,270,400],450,(401,701),(1255,350))
    Cards.append(card)
    rect = pygame.Rect((401,701),(CARD_WIDTH,CARD_HEIGHT))
    Rects.append(rect)

   
    card = Card(7,"CHANCE","",0,0,0,0,0,[],0,(301,701),())
    Cards.append(card)
    rect = pygame.Rect((301,701),(CARD_WIDTH,CARD_HEIGHT))
    Rects.append(rect)

   
    card = Card(8,"VERMONT AVENUE","LIGHT_BLUE",100,6,50,50,50,[30,90,270,400],450,(201,701),(1205,350))
    Cards.append(card)
    rect = pygame.Rect((201,701),(CARD_WIDTH,CARD_HEIGHT))
    Rects.append(rect)


    card = Card(9,"CONNECTICUT AVENUE","LIGHT_BLUE",120,8,60,50,50,[40,100,300,450],600,(101,701),(1180,350))
    Cards.append(card)
    rect = pygame.Rect((101,701),(CARD_WIDTH,CARD_HEIGHT))
    Rects.append(rect)


    card = Card(10,"IN JAIL","",0,0,0,0,0,[],0,(1,701),())
    Cards.append(card)
    rect = pygame.Rect((1,701),(CARD_WIDTH,CARD_HEIGHT))
    Rects.append(rect)


    card = Card(11,"ST. CHARLES PLACE","PINK",140,10,70,100,100,[50,150,450,625],750,(1,631),(1155,325))
    Cards.append(card)
    rect = pygame.Rect((1,631),(CARD_WIDTH,CARD_HEIGHT))
    Rects.append(rect)


    card = Card(12,"ELECTIC COMPANY","WHITE",150,10,75,0,0,[],0,(1,561),(1155,300))
    Cards.append(card)
    rect = pygame.Rect((1,561),(CARD_WIDTH,CARD_HEIGHT))
    Rects.append(rect)


    card = Card(13,"STATES AVENUE","PINK",140,10,70,100,100,[50,150,450,625],750,(1,491),(1155,275))
    Cards.append(card)
    rect = pygame.Rect((1,491),(CARD_WIDTH,CARD_HEIGHT))
    Rects.append(rect)


    card = Card(14,"VIRGINIA AVENUE","PINK",160,12,80,100,100,[60,180,500,700],900,(1,421),(1155,250))
    Cards.append(card)
    rect = pygame.Rect((1,421),(CARD_WIDTH,CARD_HEIGHT))
    Rects.append(rect)


    card = Card(15,"PENNSYLVANIA RAILROAD","BLACK",200,25,100,0,0,[],0,(1,351),(1155,225))
    Cards.append(card)
    rect = pygame.Rect((1,351),(CARD_WIDTH,CARD_HEIGHT))
    Rects.append(rect)


    card = Card(16,"ST. JAMES PLACE","ORANGE",180,14,90,100,100,[70,200,550,750],950,(1,281),(1155,200))
    Cards.append(card)
    rect = pygame.Rect((1,281),(CARD_WIDTH,CARD_HEIGHT))
    Rects.append(rect)


    card = Card(17,"COMMUNITY CHEST","",0,0,0,0,0,[],0,(1,211),())
    Cards.append(card)
    rect = pygame.Rect((1,211),(CARD_WIDTH,CARD_HEIGHT))
    Rects.append(rect)


    card = Card(18,"TENNESSEE AVENUE","ORANGE",180,14,90,100,100,[70,200,550,750],950,(1,141),(1155,150))
    Cards.append(card)
    rect = pygame.Rect((1,141),(CARD_WIDTH,CARD_HEIGHT))
    Rects.append(rect)


    card = Card(19,"NEW YORK AVENUE","ORANGE",200,16,100,100,100,[80,220,600,800],1000,(1,71),(1155,125))
    Cards.append(card)
    rect = pygame.Rect((1,71),(CARD_WIDTH,CARD_HEIGHT))
    Rects.append(rect)


    card = Card(20,"FREE PARKING","",0,0,0,0,0,[],0,(1,1),())
    Cards.append(card)
    rect = pygame.Rect((1,1),(CARD_WIDTH,CARD_HEIGHT))
    Rects.append(rect)


    card = Card(21,"KENTUCKY AVENUE","RED",220,18,110,150,150,[90,250,700,875],1050,(101,1),(1180,100))
    Cards.append(card)
    rect = pygame.Rect((101,1),(CARD_WIDTH,CARD_HEIGHT))
    Rects.append(rect)


    card = Card(22,"CHANCE","",0,0,0,0,0,[],0,(201,1),())
    Cards.append(card)
    rect = pygame.Rect((201,1),(CARD_WIDTH,CARD_HEIGHT))
    Rects.append(rect)


    card = Card(23,"INDIANA AVENUE","RED",220,18,110,150,150,[90,250,700,875],1050,(301,1),(1230,100))
    Cards.append(card)
    rect = pygame.Rect((301,1),(CARD_WIDTH,CARD_HEIGHT))
    Rects.append(rect)


    card = Card(24,"ILLINOIS AVENUE","RED",240,20,120,150,150,[100,300,750,925],1100,(401,1),(1255,100))
    Cards.append(card)
    rect = pygame.Rect((401,1),(CARD_WIDTH,CARD_HEIGHT))
    Rects.append(rect)


    card = Card(25,"B. & O. RAILROAD","BLACK",200,25,100,0,0,[],0,(501,1),(1280,100))
    Cards.append(card)
    rect = pygame.Rect((501,1),(CARD_WIDTH,CARD_HEIGHT))
    Rects.append(rect)


    card = Card(26,"ATLANTIC AVENUE","YELLOW",260,22,130,150,150,[110,330,800,975],1150,(601,1),(1305,100))
    Cards.append(card)
    rect = pygame.Rect((601,1),(CARD_WIDTH,CARD_HEIGHT))
    Rects.append(rect)


    card = Card(27,"VENTNOR AVENUE","YELLOW",260,22,130,150,150,[110,330,800,975],1150,(701,1),(1330,100))
    Cards.append(card)
    rect = pygame.Rect((701,1),(CARD_WIDTH,CARD_HEIGHT))
    Rects.append(rect)


    card = Card(28,"WATER WORKS","WHITE",150,10,75,0,0,[],0,(801,1),(1355,100))
    Cards.append(card)
    rect = pygame.Rect((801,1),(CARD_WIDTH,CARD_HEIGHT))
    Rects.append(rect)


    card = Card(29,"MARVIN GARDENS","YELLOW",280,24,140,150,150,[120,360,850,1025],1200,(901,1),(1380,100))
    Cards.append(card)
    rect = pygame.Rect((901,1),(CARD_WIDTH,CARD_HEIGHT))
    Rects.append(rect)


    card = Card(30,"GO TO JAIL","",0,0,0,0,0,[],0,(1001,1),())
    Cards.append(card)
    rect = pygame.Rect((1001,1),(CARD_WIDTH,CARD_HEIGHT))
    Rects.append(rect)


    card = Card(31,"PACIFIC AVENUE","GREEN",300,26,150,200,200,[130,390,900,1100],1275,(1001,71),(1405,125))
    Cards.append(card)
    rect = pygame.Rect((1001,71),(CARD_WIDTH,CARD_HEIGHT))
    Rects.append(rect)


    card = Card(32,"CAROLINA AVENUE","GREEN",300,26,150,200,200,[130,390,900,1100],1275,(1001,141),(1405,150))
    Cards.append(card)
    rect = pygame.Rect((1001,141),(CARD_WIDTH,CARD_HEIGHT))
    Rects.append(rect)


    card = Card(33,"COMMUNITY CHEST","",0,0,0,0,0,[],0,(1001,211),())
    Cards.append(card)
    rect = pygame.Rect((1001,211),(CARD_WIDTH,CARD_HEIGHT))
    Rects.append(rect)


    card = Card(34,"PENNSYLVANIA AVENUE","GREEN",320,28,160,200,200,[150,450,1000,1200],1400,(1001,281),(1405,200))
    Cards.append(card)
    rect = pygame.Rect((1001,281),(CARD_WIDTH,CARD_HEIGHT))
    Rects.append(rect)


    card = Card(35,"SHORT LANE","BLACK",200,25,100,0,0,[],0,(1001,351),(1405,225))
    Cards.append(card)
    rect = pygame.Rect((1001,351),(CARD_WIDTH,CARD_HEIGHT))
    Rects.append(rect)


    card = Card(36,"CHANCE","",0,0,0,0,0,[],0,(1001,421),())
    Cards.append(card)
    rect = pygame.Rect((1001,421),(CARD_WIDTH,CARD_HEIGHT))
    Rects.append(rect)

 
    card = Card(37,"PARK PLACE","BLUE",350,35,175,200,200,[175,500,1100,1300],1500,(1001,491),(1405,275))
    Cards.append(card)
    rect = pygame.Rect((1001,491),(CARD_WIDTH,CARD_HEIGHT))
    Rects.append(rect)


    card = Card(38,"LUXURY TAX","",0,0,0,0,0,[],0,(1001,561),())
    Cards.append(card)
    rect = pygame.Rect((1001,561),(CARD_WIDTH,CARD_HEIGHT))
    Rects.append(rect)


    card = Card(39,"BROADWALK","BLUE",400,50,200,200,200,[200,600,1400,1700],2000,(1001,631),(1405,325))
    Cards.append(card)
    rect = pygame.Rect((1001,631),(CARD_WIDTH,CARD_HEIGHT))
    Rects.append(rect)

    return (Cards,Rects)
    
