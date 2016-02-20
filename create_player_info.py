import pygame
import sys
from pygame.locals import *

from variables import *


# --------------CREATE PLAYER INFO--------------
# creates the player information box which shows the property owned by the player


def create_player_info(screen):

    color = WHITE


    # PLAYER 1
    pygame.draw.rect(screen,
                     color,
                     (((BOARD_WIDTH + INFO_BOARD_SPACING/2),
                       INFO_MARGIN),
                      (INFO_WIDTH,
                      INFO_HEIGHT)),2)

    font = pygame.font.SysFont(CARD_TEXT_STYLE, 20)
    screen.blit(font.render('PLAYER 1', True, WHITE), (1155, 55))
    screen.blit(font.render('M 1500', True, WHITE), (1350, 55))


    # PLAYER INFO
    pygame.draw.rect(screen,
                     color,
                     (((BOARD_WIDTH + INFO_BOARD_SPACING/2),
                       INFO_MARGIN + INFO_HEIGHT),
                      (INFO_WIDTH,
                      (INFO_HEIGHT + INFO_MARGIN) * 3 + 25)),2)

    # KENTUCKY AVENUE
    pygame.draw.rect(screen,
                     RED,
                     ((1180,
                       100),
                      (25,
                       25)))


    # INDIANA AVENUE
    pygame.draw.rect(screen,
                     RED,
                     ((1230,
                       100),
                      (25,
                       25)),2)

    
    #   ILLINOIS AVENUE
    pygame.draw.rect(screen,
                     RED,
                     ((1255,
                       100),
                      (25,
                       25)),2)


    #   B. & O. RAILROAD
    pygame.draw.rect(screen,
                     BLACK,
                     ((1280,
                       100),
                      (25,
                       25)),2)


    #   ATLANTIC AVENUE
    pygame.draw.rect(screen,
                     YELLOW,
                     ((1305,
                       100),
                      (25,
                       25)),2)


    #   VENTORA AVENUE
    pygame.draw.rect(screen,
                     YELLOW,
                     ((1330,
                       100),
                      (25,
                       25)))


    #   WATER WORKS
    pygame.draw.rect(screen,
                     WHITE,
                     ((1355,
                       100),
                      (25,
                       25)),2)


    #   MARVIN GARDENS
    pygame.draw.rect(screen,
                     YELLOW,
                     ((1380,
                       100),
                      (25,
                       25)),2)


    #   PACIFIC AVENUE
    pygame.draw.rect(screen,
                     GREEN,
                     ((1405,
                       125),
                      (25,
                       25)),2)



    #   CAROLINA AVENUE
    pygame.draw.rect(screen,
                     GREEN,
                     ((1405,
                       150),
                      (25,
                       25)),2)



    #   PENNSYLVANIA AVENUE
    pygame.draw.rect(screen,
                     GREEN,
                     ((1405,
                       200),
                      (25,
                       25)))



    #   SHORT LINE
    pygame.draw.rect(screen,
                     BLACK,
                     ((1405,
                       225),
                      (25,
                       25)))



    #   PARK PLACE
    pygame.draw.rect(screen,
                     BLUE,
                     ((1405,
                       275),
                      (25,
                       25)),2)



    #   BROADWALK
    pygame.draw.rect(screen,
                     BLUE,
                     ((1405,
                       325),
                      (25,
                       25)))



    #   MEDITERRANEAN AVENUE
    pygame.draw.rect(screen,
                     BROWN,
                     ((1380,
                       350),
                      (25,
                       25)),2)


    #   BALTIC AVENUE
    pygame.draw.rect(screen,
                     BROWN,
                     ((1330,
                       350),
                      (25,
                       25)))



    #   READING RAILROAD
    pygame.draw.rect(screen,
                     BLACK,
                     ((1280,
                       350),
                      (25,
                       25)),2)



    #   ORIENTAL AVENUE
    pygame.draw.rect(screen,
                     LIGHT_BLUE,
                     ((1255,
                       350),
                      (25,
                       25)),2)



    #   VERMONT AVENUE
    pygame.draw.rect(screen,
                     LIGHT_BLUE,
                     ((1205,
                       350),
                      (25,
                       25)))



    #   CONNECTICUT AVENUE
    pygame.draw.rect(screen,
                     LIGHT_BLUE,
                     ((1180,
                       350),
                      (25,
                       25)),2)



    #   ST. CHARLES PLACE
    pygame.draw.rect(screen,
                     PINK,
                     ((1155,
                       325),
                      (25,
                       25)),2)



    #   ELECTRIC COMPANY
    pygame.draw.rect(screen,
                     WHITE,
                     ((1155,
                       300),
                      (25,
                       25)))



    #   STATES AVENUE
    pygame.draw.rect(screen,
                     PINK,
                     ((1155,
                       275),
                      (25,
                       25)),2)



    #   VIRGINIA AVENUE
    pygame.draw.rect(screen,
                     PINK,
                     ((1155,
                       250),
                      (25,
                       25)))



    #   PENNSYLVANIA RAILROAD
    pygame.draw.rect(screen,
                     BLACK,
                     ((1155,
                       225),
                      (25,
                       25)),2)



    #   ST. JAMES PLACE
    pygame.draw.rect(screen,
                     ORANGE,
                     ((1155,
                       200),
                      (25,
                       25)),2)



    #   TENNESSEE AVENUE
    pygame.draw.rect(screen,
                     ORANGE,
                     ((1155,
                       150),
                      (25,
                       25)))



    #   NEW YORK AVENUE
    pygame.draw.rect(screen,
                     ORANGE,
                     ((1155,
                       125),
                      (25,
                       25)),2)






    
    # PLAYER 2
    pygame.draw.rect(screen,
                     color,
                     (((BOARD_WIDTH + INFO_BOARD_SPACING/2),
                       (INFO_MARGIN + INFO_HEIGHT) * 4 + 25),
                      (INFO_WIDTH,
                      INFO_HEIGHT)),2)

    font = pygame.font.SysFont(CARD_TEXT_STYLE, 20)
    screen.blit(font.render('PLAYER 2', True, WHITE), (1155, 400))
    screen.blit(font.render('M 1500', True, WHITE), (1350, 400))


    # PLAYER 3
    pygame.draw.rect(screen,
                     color,
                     (((BOARD_WIDTH + INFO_BOARD_SPACING/2),
                      (INFO_MARGIN + INFO_HEIGHT) * 5 - INFO_MARGIN + 25),
                      (INFO_WIDTH,
                      INFO_HEIGHT)),2)

    font = pygame.font.SysFont(CARD_TEXT_STYLE, 20)
    screen.blit(font.render('PLAYER 3', True, WHITE), (1155, 450))
    screen.blit(font.render('M 1500', True, WHITE), (1350, 450))


    # PLAYER 4
    pygame.draw.rect(screen,
                     color,
                     (((BOARD_WIDTH + INFO_BOARD_SPACING/2),
                      (INFO_MARGIN + INFO_HEIGHT) * 6 - INFO_MARGIN * 2 + 25),
                      (INFO_WIDTH,
                      INFO_HEIGHT)),2)

    font = pygame.font.SysFont(CARD_TEXT_STYLE, 20)
    screen.blit(font.render('PLAYER 4', True, WHITE), (1155, 500))
    screen.blit(font.render('M 1500', True, WHITE), (1350, 500))


    # BANK
    pygame.draw.rect(screen,
                     color,
                     (((BOARD_WIDTH + INFO_BOARD_SPACING/2),
                      (INFO_MARGIN + INFO_HEIGHT) * 7 - INFO_MARGIN * 3 + 25),
                      (INFO_WIDTH,
                      INFO_HEIGHT)),2)

    font = pygame.font.SysFont(CARD_TEXT_STYLE, 20)
    screen.blit(font.render('BANK', True, WHITE), (1155, 550))
    screen.blit(font.render('M 6000', True, WHITE), (1350, 550))
    
    
