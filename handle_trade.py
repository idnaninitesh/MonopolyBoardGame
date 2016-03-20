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
        Cur_Other_Mark = []
        Other_Mark = []
        Other_Other_Mark = []
        
        Cur_Mark.extend(player.property_owned)
        
        Cur_Mark.extend(player.property_mortgaged)

        for prop in player.property_owned:
            if Cards[prop].houses_built > 0 or Cards[prop].hotel_built > 0:
                del_color = []           
                for color_cards in player.color_cards_owned:
                    if prop in color_cards:
                        del_color = color_cards
                if del_color != []:
                    for card in del_color:
                        Cur_Mark.remove(card)
                            
        for tmp in Players:
            if tmp != player:
                Cur_Other_Mark.extend(tmp.property_owned)
                Cur_Other_Mark.extend(tmp.property_mortgaged)


        Other_Mark.extend(other.property_owned)

        Other_Mark.extend(other.property_mortgaged)

        for prop in other.property_owned:
            if Cards[prop].houses_built > 0 or Cards[prop].hotel_built > 0:
                del_color = []            
                for color_cards in other.color_cards_owned:
                    if prop in color_cards:
                        del_color = color_cards
                if del_color != []:
                    for card in del_color:
                        Other_Mark.remove(card)

        for tmp in Players:
            if tmp != other:
                Other_Other_Mark.extend(tmp.property_owned)
                Other_Other_Mark.extend(tmp.property_mortgaged)


        if Cur_Mark != None or Other_Mark != None:
            update_game_trade(screen,Players,Cards,cur_player,other_player,Cards_Rects,Option_Rects,Info_Cards_Rects,Cur_Mark,Other_Mark,Cur_Other_Mark,Other_Other_Mark)
            


    # show the state after update


    screen.fill(BACKGROUND_COLOR)

    create_board(screen,Cards)

    create_game_options(screen)

    roll_dice(screen,4,2)
    
    for player in Players:
        player.move_player(screen,player.cur_position)

    create_player_info(screen,Players,Cards,cur_player)

    return cur_player


        

            
