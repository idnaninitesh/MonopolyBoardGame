import pygame
import sys
from pygame.locals import *

from variables import *
from Card import *


# --------------CREATE PLAYER INFO--------------
# creates the player information box which shows the property owned by the player


def create_player_info(screen,Players,Cards):

    # create cards

    color = WHITE

    player = Players[0]

    if player.color == "RED":
        color = RED
    elif player.color == "GREEN":
        color = GREEN
    elif player.color == "BLUE":
        color = BLUE
    elif player.color == "YELLOW":
        color = YELLOW
    else:
        color = WHITE

    # PLAYER 1
    pygame.draw.rect(screen,
                     color,
                     (((BOARD_WIDTH + INFO_BOARD_SPACING/2),
                       INFO_MARGIN),
                      (INFO_WIDTH,
                      INFO_HEIGHT)),2)

    font = pygame.font.SysFont(CARD_TEXT_STYLE, 20)
    screen.blit(font.render('' + player.name, True, color), (1155, 55))
    screen.blit(font.render('M ' + str(player.cur_balance), True, color), (1350, 55))


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
                       25)),2)


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
                       25)),2)


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
                       25)),2)



    #   SHORT LINE
    pygame.draw.rect(screen,
                     BLACK,
                     ((1405,
                       225),
                      (25,
                       25)),2)



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
                       25)),2)



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
                       25)),2)



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
                       25)),2)



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
                       25)),2)



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
                       25)),2)



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
                       25)),2)



    #   NEW YORK AVENUE
    pygame.draw.rect(screen,
                     ORANGE,
                     ((1155,
                       125),
                      (25,
                       25)),2)


    #   UPDATING PLAYER PROPERTY

    for player_property in player.property_owned:
        if Cards[player_property].color == "RED":
            color = RED
        elif Cards[player_property].color == "GREEN":
            color = GREEN
        elif Cards[player_property].color == "BLUE":
            color = BLUE
        elif Cards[player_property].color == "YELLOW":
            color = YELLOW
        elif Cards[player_property].color == "BLACK":
            color = BLACK
        elif Cards[player_property].color == "BROWN":
            color = BROWN
        elif Cards[player_property].color == "LIGHT_BLUE":
            color = LIGHT_BLUE
        elif Cards[player_property].color == "PINK":
            color = PINK
        elif Cards[player_property].color == "ORANGE":
            color = ORANGE
        else:
            color = WHITE

        pygame.draw.rect(screen,
                         color,
                         (Cards[player_property].info_pos,
                          (25,
                           25)))


    j = 4
    k = 0
    name_x = 1155
    amt_x = 1350
    y = 400
    
    for player in Players[1:]:
        if player.color == "RED":
            color = RED
        elif player.color == "GREEN":
            color = GREEN
        elif player.color == "BLUE":
            color = BLUE
        elif player.color == "YELLOW":
            color = YELLOW
        else:
            color = WHITE

        pygame.draw.rect(screen,
                     color,
                     (((BOARD_WIDTH + INFO_BOARD_SPACING/2),
                       (INFO_MARGIN + INFO_HEIGHT) * j - INFO_MARGIN * k + 25),
                      (INFO_WIDTH,
                      INFO_HEIGHT)),2)
        

        font = pygame.font.SysFont(CARD_TEXT_STYLE, 20)
        screen.blit(font.render('' + player.name, True, color), (name_x, y))
        screen.blit(font.render('M ' + str(player.cur_balance), True, color), (amt_x, y))

        j = j + 1
        k = k + 1
        y = y + 50

        

