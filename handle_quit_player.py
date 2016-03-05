import pygame
import sys
from pygame.locals import *

from variables import *
from Player import *
from Card import *
from create_board import *
from create_game_options import *
from create_player_info import *
from handle_mouse_event import *
from update_game_dice import *
from handle_game import *


# handles all the action to remove player from the game

"""

Rules :

1) return all the cards allocated to that player
2) clear player details from the list

"""

def handle_quit_player(screen,Players,Cards,cur_player):

    player = Players[cur_player]

    # updating the card status and other related fields

    for prop in player.property_owned:

        Cards[prop].status = 0
        Cards[prop].houses_built = 0
        Cards[prop].hotel_built = 0

    for player in player.property_mortgaged:

        Cards[prop].status = 0
        Cards[prop].houses_built = 0
        Cards[prop].hotel_built = 0
   
    # remove player from the list

    Players.remove(player)
    
