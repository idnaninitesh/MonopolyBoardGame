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
from update_game_build import *
from update_game_sell import *


# allow user to decide winner

def handle_decide_winner(screen,Players,Cards,cur_player):

    if cur_player == 0:

        # adding static part

        screen.fill(BACKGROUND_COLOR)

        create_board(screen,Cards)

        create_game_options(screen)

        create_player_info(screen,Players,Cards,cur_player)

        for player in Players:
            player.move_player(screen,player.cur_position)


        # declare winner logic
        # calculate current balance, property value

        Players_Worth = []
        worth = 0

        for player in Players:
            worth = 0

            # adding current balance
            worth += player.cur_balance

            # adding owned property worth
            for own in player.property_owned:
                worth += (Cards[own].houses_built * Cards[own].house_cost)
                worth += (Cards[own].hotel_built * Cards[own].hotel_cost)
                worth += (Cards[own].cost)

            for mort in player.property_mortgaged:
                worth += Cards[mort].mortgage_value

            Players_Worth.append(worth)

        end = display_decide_winner_window(screen,Players,Players_Worth)

        if end == True:
            pygame.quit()
            sys.exit()
        else:

            screen.fill(BACKGROUND_COLOR)

            create_board(screen,Cards)

            create_game_options(screen)

            roll_dice(screen,4,2)
            
            for player in Players:
                player.move_player(screen,player.cur_position)

            create_player_info(screen,Players,Cards,cur_player)


    return cur_player


