import pygame
from pygame.locals import *

from variables import *


class Player:

    
    #   add new player
    def __init__(self,name,color,cur_balance):     
        self.name = name
        self.color = color.upper()
        self.cur_balance = cur_balance
        self.cur_position = ()
        self.property_owned = []
        self.property_mortgaged = []
        total_rails_owned = 0
        total_utilities_owned = 0
        self.jail_card = False
        isBankrupt = False



    #   move player

    
    #adding dice and pieces(blue,red,green,yellow
    # x = x coordinate of the card
    # y = y coordinate of the card
    # blue position   = x + 20, y + 20
    # red position    = x + 60, y + 20
    # green position  = x + 20, y + 50
    # yellow position = x + 60, y + 50



    def move_player(self,screen,next_position):
        if self.color == "BLUE":
            pygame.draw.circle(screen,
                               BLUE,
                               next_position,
                               PIECE_RADIUS)
        elif self.color == "RED":
            pygame.draw.circle(screen,
                               RED,
                               next_position,
                               PIECE_RADIUS)
        elif self.color == "GREEN":
            pygame.draw.circle(screen,
                               GREEN,
                               next_position,
                               PIECE_RADIUS)
        elif self.color == "YELLOW":
            pygame.draw.circle(screen,
                               YELLOW,
                               next_position,
                               PIECE_RADIUS)

        self.cur_position = next_position


            
    
    #   update balance
    #   add property
    #   remove property
    #   mortgage property
    #   unmortgage property
    #   set jail card
    #   remove player
    
