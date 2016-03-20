import pygame
import sys
import pygame.gfxdraw
from pygame.locals import *

from variables import *
from Card import *


# --------------CREATE PLAYER INFO--------------
# creates the player information box which shows the property owned by the player


def create_player_info(screen,Players,Cards,cur_player,dist_x = 1155,dist_y = 100,Mark = []):

    Other_Mark = []

    if Mark == []:
        Mark = Players[cur_player].property_owned
        Mark.extend(Players[cur_player].property_mortgaged)

        
        current = Players[cur_player]

        # adding other player property
        Other_Mark = []
        
        for player in Players:
            if current != player:
                Other_Mark.extend(player.property_owned)
                Other_Mark.extend(player.property_mortgaged)

        
    
    # create cards

    color = WHITE

    player = Players[cur_player]

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
    screen.blit(font.render('$ ' + str(player.cur_balance), True, color), (1350, 55))


    # PLAYER INFO
    pygame.draw.rect(screen,
                     color,
                     (((BOARD_WIDTH + INFO_BOARD_SPACING/2),
                       INFO_MARGIN + INFO_HEIGHT),
                      (INFO_WIDTH,
                      (INFO_HEIGHT + INFO_MARGIN) * 3 + 25)),2)

    create_info_cards(screen) 

 

    j = 4
    k = 0
    name_x = 1155
    amt_x = 1350
    y = 400

    if cur_player != len(Players) - 1:
        
        for player in Players[cur_player+1:]:
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
            screen.blit(font.render('$ ' + str(player.cur_balance), True, color), (amt_x, y))
    
            j = j + 1
            k = k + 1
            y = y + 50


    if cur_player != 0:

        for player in Players[:cur_player]:
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
            screen.blit(font.render('$ ' + str(player.cur_balance), True, color), (amt_x, y))
    
            j = j + 1
            k = k + 1
            y = y + 50


   #   UPDATING PLAYER PROPERTY

    for player_property in Mark:
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

        height = INFO_CARD_HEIGHT

        #half the height for mortgaged property
        
        if Cards[player_property].status == 2:
            height = int((INFO_CARD_HEIGHT+1)/2)
        else:
            height = INFO_CARD_HEIGHT

        pygame.draw.rect(screen,
                         color,
                         (Cards[player_property].info_pos,
                          (INFO_CARD_WIDTH,
                           height)))

        if Cards[player_property].hotel_built == 1:
            pygame.gfxdraw.circle(screen, Cards[player_property].info_pos[0] + 12,Cards[player_property].info_pos[1] + 12, 5, BLACK)
        elif Cards[player_property].houses_built > 0:

            pygame.gfxdraw.circle(screen, Cards[player_property].info_pos[0] + 7,Cards[player_property].info_pos[1] + 7, 3, BLACK)

            if Cards[player_property].houses_built == 2:
                pygame.gfxdraw.circle(screen, Cards[player_property].info_pos[0] + 18,Cards[player_property].info_pos[1] + 7, 3, BLACK)

            if Cards[player_property].houses_built == 3:
                pygame.gfxdraw.circle(screen, Cards[player_property].info_pos[0] + 18,Cards[player_property].info_pos[1] + 7, 3, BLACK)
                pygame.gfxdraw.circle(screen, Cards[player_property].info_pos[0] + 7,Cards[player_property].info_pos[1] + 18, 3, BLACK)

            if Cards[player_property].houses_built == 4:
                pygame.gfxdraw.circle(screen, Cards[player_property].info_pos[0] + 18,Cards[player_property].info_pos[1] + 7, 3, BLACK)
                pygame.gfxdraw.circle(screen, Cards[player_property].info_pos[0] + 7,Cards[player_property].info_pos[1] + 18, 3, BLACK)
                pygame.gfxdraw.circle(screen, Cards[player_property].info_pos[0] + 18,Cards[player_property].info_pos[1] + 18, 3, BLACK)
            

    # UPDATING OTHER PLAYER PROPERTY
    
    for other_property in Other_Mark:
        color = DISABLED

        pygame.draw.rect(screen,
                         color,
                         (Cards[other_property].info_pos,
                          (INFO_CARD_WIDTH,
                           INFO_CARD_HEIGHT)))

    
        

def create_info_cards(screen,dist_x = 1155,dist_y = 100):

    # KENTUCKY AVENUE
    pygame.draw.rect(screen,
                     RED,
                     ((dist_x + INFO_CARD_WIDTH * 1,
                       dist_y),
                      (INFO_CARD_WIDTH,
                       INFO_CARD_HEIGHT)),2)


    # INDIANA AVENUE
    pygame.draw.rect(screen,
                     RED,
                     ((dist_x + INFO_CARD_WIDTH * 3,
                       dist_y),
                      (INFO_CARD_WIDTH,
                       INFO_CARD_HEIGHT)),2)

    
    #   ILLINOIS AVENUE
    pygame.draw.rect(screen,
                     RED,
                     ((dist_x + INFO_CARD_WIDTH * 4,
                       dist_y),
                      (INFO_CARD_WIDTH,
                       INFO_CARD_HEIGHT)),2)


    #   B. & O. RAILROAD
    pygame.draw.rect(screen,
                     BLACK,
                     ((dist_x + INFO_CARD_WIDTH * 5,
                       dist_y),
                      (INFO_CARD_WIDTH,
                       INFO_CARD_HEIGHT)),2)


    #   ATLANTIC AVENUE
    pygame.draw.rect(screen,
                     YELLOW,
                     ((dist_x + INFO_CARD_WIDTH * 6,
                       dist_y),
                      (INFO_CARD_WIDTH,
                       INFO_CARD_HEIGHT)),2)


    #   VENTORA AVENUE
    pygame.draw.rect(screen,
                     YELLOW,
                     ((dist_x + INFO_CARD_WIDTH * 7,
                       dist_y),
                      (INFO_CARD_WIDTH,
                       INFO_CARD_HEIGHT)),2)


    #   WATER WORKS
    pygame.draw.rect(screen,
                     WHITE,
                     ((dist_x + INFO_CARD_WIDTH * 8,
                       dist_y),
                      (INFO_CARD_WIDTH,
                       INFO_CARD_HEIGHT)),2)


    #   MARVIN GARDENS
    pygame.draw.rect(screen,
                     YELLOW,
                     ((dist_x + INFO_CARD_WIDTH * 9,
                       dist_y),
                      (INFO_CARD_WIDTH,
                       INFO_CARD_HEIGHT)),2)


    #   PACIFIC AVENUE
    pygame.draw.rect(screen,
                     GREEN,
                     ((dist_x + INFO_CARD_WIDTH * 10,
                       dist_y + INFO_CARD_HEIGHT * 1),
                      (INFO_CARD_WIDTH,
                       INFO_CARD_HEIGHT)),2)



    #   CAROLINA AVENUE
    pygame.draw.rect(screen,
                     GREEN,
                     ((dist_x + INFO_CARD_WIDTH * 10,
                       dist_y + INFO_CARD_HEIGHT * 2),
                      (INFO_CARD_WIDTH,
                       INFO_CARD_HEIGHT)),2)


    #   PENNSYLVANIA AVENUE
    pygame.draw.rect(screen,
                     GREEN,
                     ((dist_x + INFO_CARD_WIDTH * 10,
                       dist_y + INFO_CARD_HEIGHT * 4),
                      (INFO_CARD_WIDTH,
                       INFO_CARD_HEIGHT)),2)



    #   SHORT LINE                      
    pygame.draw.rect(screen,
                     BLACK,
                     ((dist_x + INFO_CARD_WIDTH * 10,
                       dist_y + INFO_CARD_HEIGHT * 5),
                      (INFO_CARD_WIDTH,
                       INFO_CARD_HEIGHT)),2)



    #   PARK PLACE
    pygame.draw.rect(screen,
                     BLUE,
                     ((dist_x + INFO_CARD_WIDTH * 10,
                       dist_y + INFO_CARD_HEIGHT * 7),
                      (INFO_CARD_WIDTH,
                       INFO_CARD_HEIGHT)),2)



    #   BROADWALK
    pygame.draw.rect(screen,
                     BLUE,
                     ((dist_x + INFO_CARD_WIDTH * 10,
                       dist_y + INFO_CARD_HEIGHT * 9),
                      (INFO_CARD_WIDTH,
                       INFO_CARD_HEIGHT)),2)



    #   MEDITERRANEAN AVENUE
    pygame.draw.rect(screen,
                     BROWN,
                     ((dist_x + INFO_CARD_WIDTH * 9,
                       dist_y + INFO_CARD_HEIGHT * 10),
                      (INFO_CARD_WIDTH,
                       INFO_CARD_HEIGHT)),2)


    #   BALTIC AVENUE
    pygame.draw.rect(screen,
                     BROWN,
                     ((dist_x + INFO_CARD_WIDTH * 7,
                       dist_y + INFO_CARD_HEIGHT * 10),
                      (INFO_CARD_WIDTH,
                       INFO_CARD_HEIGHT)),2)



    #   READING RAILROAD
    pygame.draw.rect(screen,
                     BLACK,
                     ((dist_x + INFO_CARD_WIDTH * 5,
                       dist_y + INFO_CARD_HEIGHT * 10),
                      (INFO_CARD_WIDTH,
                       INFO_CARD_HEIGHT)),2)



    #   ORIENTAL AVENUE
    pygame.draw.rect(screen,
                     LIGHT_BLUE,
                     ((dist_x + INFO_CARD_WIDTH * 4,
                       dist_y + INFO_CARD_HEIGHT * 10),
                      (INFO_CARD_WIDTH,
                       INFO_CARD_HEIGHT)),2)



    #   VERMONT AVENUE
    pygame.draw.rect(screen,
                     LIGHT_BLUE,
                     ((dist_x + INFO_CARD_WIDTH * 2,
                       dist_y + INFO_CARD_HEIGHT * 10),
                      (INFO_CARD_WIDTH,
                       INFO_CARD_HEIGHT)),2)



    #   CONNECTICUT AVENUE
    pygame.draw.rect(screen,
                     LIGHT_BLUE,
                     ((dist_x + INFO_CARD_WIDTH * 1,
                       dist_y + INFO_CARD_HEIGHT * 10),
                      (INFO_CARD_WIDTH,
                       INFO_CARD_HEIGHT)),2)



    #   ST. CHARLES PLACE
    pygame.draw.rect(screen,
                     PINK,
                     ((dist_x,
                       dist_y + INFO_CARD_HEIGHT * 9),
                      (INFO_CARD_WIDTH,
                       INFO_CARD_HEIGHT)),2)



    #   ELECTRIC COMPANY
    pygame.draw.rect(screen,
                     WHITE,
                     ((dist_x,
                       dist_y + INFO_CARD_HEIGHT * 8),
                      (INFO_CARD_WIDTH,
                       INFO_CARD_HEIGHT)),2)



    #   STATES AVENUE
    pygame.draw.rect(screen,
                     PINK,
                     ((dist_x,
                       dist_y + INFO_CARD_HEIGHT * 7),
                      (INFO_CARD_WIDTH,
                       INFO_CARD_HEIGHT)),2)



    #   VIRGINIA AVENUE
    pygame.draw.rect(screen,
                     PINK,
                     ((dist_x,
                       dist_y + INFO_CARD_HEIGHT * 6),
                      (INFO_CARD_WIDTH,
                       INFO_CARD_HEIGHT)),2)



    #   PENNSYLVANIA RAILROAD
    pygame.draw.rect(screen,
                     BLACK,
                     ((dist_x,
                       dist_y + INFO_CARD_HEIGHT * 5),
                      (INFO_CARD_WIDTH,
                       INFO_CARD_HEIGHT)),2)



    #   ST. JAMES PLACE
    pygame.draw.rect(screen,
                     ORANGE,
                     ((dist_x,
                       dist_y + INFO_CARD_HEIGHT * 4),
                      (INFO_CARD_WIDTH,
                       INFO_CARD_HEIGHT)),2)



    #   TENNESSEE AVENUE
    pygame.draw.rect(screen,
                     ORANGE,
                     ((dist_x,
                       dist_y + INFO_CARD_HEIGHT * 2),
                      (INFO_CARD_WIDTH,
                       INFO_CARD_HEIGHT)),2)



    #   NEW YORK AVENUE
    pygame.draw.rect(screen,
                     ORANGE,
                     ((dist_x,
                       dist_y + INFO_CARD_HEIGHT * 1),
                      (INFO_CARD_WIDTH,
                       INFO_CARD_HEIGHT)),2)



# creating info card rectangles for handling events on them

def create_info_rects(dist_x = 1155,dist_y = 100):
    Info_Cards_Rects = []


    #   GO
    Info_Cards_Rects.append(None)


    #   MEDITERRANEAN AVENUE
    rect = pygame.Rect((dist_x + INFO_CARD_WIDTH * 9,
                       dist_y + INFO_CARD_HEIGHT * 10),
                     (INFO_CARD_WIDTH,
                      INFO_CARD_HEIGHT))
    Info_Cards_Rects.append(rect)


    #   COMMUNITY CHEST

    Info_Cards_Rects.append(None)


    #   BALTIC AVENUE
    rect = pygame.Rect((dist_x + INFO_CARD_WIDTH * 7,
                       dist_y + INFO_CARD_HEIGHT * 10),
                     (INFO_CARD_WIDTH,
                      INFO_CARD_HEIGHT))
    Info_Cards_Rects.append(rect)


    #   INCOME TAX

    Info_Cards_Rects.append(None)


    #   READING RAILROAD
    rect = pygame.Rect((dist_x + INFO_CARD_WIDTH * 5,
                       dist_y + INFO_CARD_HEIGHT * 10),
                     (INFO_CARD_WIDTH,
                      INFO_CARD_HEIGHT))
    Info_Cards_Rects.append(rect)



    #   ORIENTAL AVENUE
    rect = pygame.Rect((dist_x + INFO_CARD_WIDTH * 4,
                       dist_y + INFO_CARD_HEIGHT * 10),
                     (INFO_CARD_WIDTH,
                      INFO_CARD_HEIGHT))
    Info_Cards_Rects.append(rect)


    #   CHANCE

    Info_Cards_Rects.append(None)


    #   VERMONT AVENUE
    rect = pygame.Rect((dist_x + INFO_CARD_WIDTH * 2,
                       dist_y + INFO_CARD_HEIGHT * 10),
                     (INFO_CARD_WIDTH,
                      INFO_CARD_HEIGHT))
    Info_Cards_Rects.append(rect)



    #   CONNECTICUT AVENUE
    rect = pygame.Rect((dist_x + INFO_CARD_WIDTH * 1,
                       dist_y + INFO_CARD_HEIGHT * 10),
                     (INFO_CARD_WIDTH,
                      INFO_CARD_HEIGHT))
    Info_Cards_Rects.append(rect)


    #   IN JAIL

    Info_Cards_Rects.append(None)


    #   ST. CHARLES PLACE
    rect = pygame.Rect((dist_x,
                       dist_y + INFO_CARD_HEIGHT * 9),
                     (INFO_CARD_WIDTH,
                      INFO_CARD_HEIGHT))
    Info_Cards_Rects.append(rect)



    #   ELECTRIC COMPANY
    rect = pygame.Rect((dist_x,
                       dist_y + INFO_CARD_HEIGHT * 8),
                     (INFO_CARD_WIDTH,
                      INFO_CARD_HEIGHT))
    Info_Cards_Rects.append(rect)



    #   STATES AVENUE
    rect = pygame.Rect((dist_x,
                       dist_y + INFO_CARD_HEIGHT * 7),
                     (INFO_CARD_WIDTH,
                      INFO_CARD_HEIGHT))
    Info_Cards_Rects.append(rect)



    #   VIRGINIA AVENUE
    rect = pygame.Rect((dist_x,
                       dist_y + INFO_CARD_HEIGHT * 6),
                     (INFO_CARD_WIDTH,
                      INFO_CARD_HEIGHT))
    Info_Cards_Rects.append(rect)



    #   PENNSYLVANIA RAILROAD
    rect = pygame.Rect((dist_x,
                       dist_y + INFO_CARD_HEIGHT * 5),
                     (INFO_CARD_WIDTH,
                      INFO_CARD_HEIGHT))
    Info_Cards_Rects.append(rect)



    #   ST. JAMES PLACE
    rect = pygame.Rect((dist_x,
                       dist_y + INFO_CARD_HEIGHT * 4),
                     (INFO_CARD_WIDTH,
                      INFO_CARD_HEIGHT))
    Info_Cards_Rects.append(rect)


    #   COMMUNITY CHEST

    Info_Cards_Rects.append(None)


    #   TENNESSEE AVENUE
    rect = pygame.Rect((dist_x,
                       dist_y + INFO_CARD_HEIGHT * 2),
                     (INFO_CARD_WIDTH,
                      INFO_CARD_HEIGHT))
    Info_Cards_Rects.append(rect)



    #   NEW YORK AVENUE
    rect = pygame.Rect((dist_x,
                       dist_y + INFO_CARD_HEIGHT * 1),
                     (INFO_CARD_WIDTH,
                      INFO_CARD_HEIGHT))
    Info_Cards_Rects.append(rect)


    #   FREE PARKING

    Info_Cards_Rects.append(None)


    # KENTUCKY AVENUE
    rect = pygame.Rect((dist_x + INFO_CARD_WIDTH * 1,
                       dist_y),
                      (INFO_CARD_WIDTH,
                       INFO_CARD_HEIGHT))
    Info_Cards_Rects.append(rect)


    #   CHANCE

    Info_Cards_Rects.append(None)


    # INDIANA AVENUE
    rect = pygame.Rect((dist_x + INFO_CARD_WIDTH * 3,
                      dist_y),
                     (INFO_CARD_WIDTH,
                      INFO_CARD_HEIGHT))
    Info_Cards_Rects.append(rect)

    
    #   ILLINOIS AVENUE
    rect = pygame.Rect((dist_x + INFO_CARD_WIDTH * 4,
                      dist_y),
                     (INFO_CARD_WIDTH,
                      INFO_CARD_HEIGHT))
    Info_Cards_Rects.append(rect)


    #   B. & O. RAILROAD
    rect = pygame.Rect((dist_x + INFO_CARD_WIDTH * 5,
                      dist_y),
                     (INFO_CARD_WIDTH,
                      INFO_CARD_HEIGHT))
    Info_Cards_Rects.append(rect)


    #   ATLANTIC AVENUE
    rect = pygame.Rect((dist_x + INFO_CARD_WIDTH * 6,
                       dist_y),
                     (INFO_CARD_WIDTH,
                      INFO_CARD_HEIGHT))
    Info_Cards_Rects.append(rect)


    #   VENTORA AVENUE
    rect = pygame.Rect((dist_x + INFO_CARD_WIDTH * 7,
                       dist_y),
                     (INFO_CARD_WIDTH,
                      INFO_CARD_HEIGHT))
    Info_Cards_Rects.append(rect)


    #   WATER WORKS
    rect = pygame.Rect((dist_x + INFO_CARD_WIDTH * 8,
                       dist_y),
                     (INFO_CARD_WIDTH,
                      INFO_CARD_HEIGHT))
    Info_Cards_Rects.append(rect)


    #   MARVIN GARDENS
    rect = pygame.Rect((dist_x + INFO_CARD_WIDTH * 9,
                       dist_y),
                     (INFO_CARD_WIDTH,
                      INFO_CARD_HEIGHT))
    Info_Cards_Rects.append(rect)


    #   GO TO JAIL

    Info_Cards_Rects.append(None)


    #   PACIFIC AVENUE
    rect = pygame.Rect((dist_x + INFO_CARD_WIDTH * 10,
                       dist_y + INFO_CARD_HEIGHT * 1),
                     (INFO_CARD_WIDTH,
                      INFO_CARD_HEIGHT))
    Info_Cards_Rects.append(rect)



    #   CAROLINA AVENUE
    rect = pygame.Rect((dist_x + INFO_CARD_WIDTH * 10,
                       dist_y + INFO_CARD_HEIGHT * 2),
                     (INFO_CARD_WIDTH,
                      INFO_CARD_HEIGHT))
    Info_Cards_Rects.append(rect)


    #   COMMUNITY CHEST

    Info_Cards_Rects.append(None)


    #   PENNSYLVANIA AVENUE
    rect = pygame.Rect((dist_x + INFO_CARD_WIDTH * 10,
                        dist_y + INFO_CARD_HEIGHT * 4),
                       (INFO_CARD_WIDTH,
                        INFO_CARD_HEIGHT))
    Info_Cards_Rects.append(rect)



    #   SHORT LINE
    rect = pygame.Rect((dist_x + INFO_CARD_WIDTH * 10,
                       dist_y + INFO_CARD_HEIGHT * 5),
                     (INFO_CARD_WIDTH,
                      INFO_CARD_HEIGHT))
    Info_Cards_Rects.append(rect)


    #   CHANCE

    Info_Cards_Rects.append(None)


    #   PARK PLACE
    rect = pygame.Rect((dist_x + INFO_CARD_WIDTH * 10,
                       dist_y + INFO_CARD_HEIGHT * 7),
                     (INFO_CARD_WIDTH,
                      INFO_CARD_HEIGHT))
    Info_Cards_Rects.append(rect)


    #   LUXURY TAX

    Info_Cards_Rects.append(None)


    #   BROADWALK
    rect = pygame.Rect((dist_x + INFO_CARD_WIDTH * 10,
                       dist_y + INFO_CARD_HEIGHT * 9),
                     (INFO_CARD_WIDTH,
                      INFO_CARD_HEIGHT))
    Info_Cards_Rects.append(rect)



    return Info_Cards_Rects
    
