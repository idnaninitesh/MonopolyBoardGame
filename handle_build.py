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



# allow user to build house and update Player and Card objects

def handle_build(screen,Players,Cards,cur_player,Cards_Rects,Option_Rects,Info_Cards_Rects):

    # adding static part
    
    screen.fill(BACKGROUND_COLOR)

    create_board(screen)

    create_game_options(screen)

    create_player_info(screen,Players,Cards,cur_player)

    for player in Players:
        player.move_player(screen,player.cur_position)


    # check if property is available for building house/hotel

    Mark = []

    player = Players[cur_player]

    for color_list in player.color_cards_owned:
        Mark.extend(color_list)
    
    # display build window

    if Mark != []:
        update_game_build(screen,Players,Cards,cur_player,Cards_Rects,Option_Rects,Info_Cards_Rects,Mark)

    # show the state after update


    screen.fill(BACKGROUND_COLOR)

    create_board(screen)

    create_game_options(screen)

    roll_dice(screen,4,2)
    
    for player in Players:
        player.move_player(screen,player.cur_position)

    create_player_info(screen,Players,Cards,cur_player)

    return cur_player

    



    

    

    

    

    


    

