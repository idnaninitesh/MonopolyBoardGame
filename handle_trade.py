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
from update_game_trade import *
from update_game_sell import *
from update_game_mortgage import *
from update_game_unmortgage import *


def handle_trade(screen,Players,Cards,cur_player,Cards_Rects,Option_Rects,Info_Cards_Rects):

    # adding static part

    screen.fill(BACKGROUND_COLOR)

    create_board(screen,Cards)

    create_game_options(screen)

    create_player_info(screen,Players,Cards,cur_player)

    for player in Players:
        player.move_player(screen,player.cur_position)

    other_player = display_select_trade_player_window(screen,Players,Cards,cur_player)

    # create current and other player cards available for trade

    if other_player != -1:

        create_board(screen,Cards)

        create_game_options(screen)

        create_player_info(screen,Players,Cards,cur_player)

        for player in Players:
            player.move_player(screen,player.cur_position)


        player = Players[cur_player]
        other = Players[other_player]

        Cur_Mark = []
        Other_Mark = []

        for prop in player.property_owned:
            Cur_Mark.append(prop)

        for prop in player.property_mortgaged:
            Cur_Mark.append(prop)

        for prop in other.property_owned:
            Other_Mark.append(prop)

        for prop in other.property_mortgaged:
            Other_Mark.append(prop)

        if Cur_Mark != None or Other_Mark != None:
            update_game_trade(screen,Players,Cards,cur_player,other_player,Cards_Rects,Option_Rects,Info_Cards_Rects,Cur_Mark,Other_Mark)
            


    # show the state after update


    screen.fill(BACKGROUND_COLOR)

    create_board(screen,Cards)

    create_game_options(screen)

    roll_dice(screen,4,2)
    
    for player in Players:
        player.move_player(screen,player.cur_position)

    create_player_info(screen,Players,Cards,cur_player)

    return cur_player


        

            
