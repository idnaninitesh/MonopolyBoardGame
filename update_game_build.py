import pygame
import sys
from random import *
from pygame.locals import *
from operator import attrgetter

from variables import *
from Card import *
from Player import *
from create_board import *
from create_game_options import *
from create_player_info import *
from handle_mouse_event import *
from display_windows import *

"""

Rules :

1) Show property on which house/hotel can be built
   - there should be equal number of houses on all property before increasing it by one
2) Player selects the property
3) Update the state of player and card
4) Repeat steps 1-3 till player does not selects cancel
"""

def update_game_build(screen,Players,Cards,cur_player,Cards_Rects,Option_Rects,Info_Cards_Rects,Mark):

    card_list = []


    # removing card which have hotels built on them
    # removing cards which have greater no of houses than other cards of same color
    
    for color_cards in Players[cur_player].color_cards_owned:
        # color_cards = [1,3]
        for card in color_cards:
            card_list.append(Cards[card])
        # card_list(Card[1],Card[3])
        min_house_card = min(card_list,key=attrgetter('houses_built'))
        if min_house_card.houses_built == 4:     # hotel
            for crd in color_cards:
                if Cards[crd].hotel_built == 1:
                    if crd in Mark:
                        Mark.remove(crd)
        else:                   # house
            for crd in color_cards:
                if Cards[crd].houses_built != min_house_card.houses_built:
                    if crd in Mark:
                        Mark.remove(crd)
    

    # get the card index that was clicked
    build_card = display_build_window(screen,Players,Cards,cur_player,Mark)

    # check if the card is valid
    # none implies user clicked cancel
    # check if card is in mark

    if build_card != None:
        if build_card in Mark:

            card = Cards[build_card]

            screen.fill(BACKGROUND_COLOR)

            create_board(screen)

            create_game_options(screen)
            
            for player in Players:
                player.move_player(screen,player.cur_position)

            create_player_info(screen,Players,Cards,cur_player)

            # confirmation prompt
            # show build infomation

            build_prop = display_build_confirm_window(screen,card)

            # update card status and player balance

            if build_prop == True:

                player = Players[cur_player]
                
                # build hotel
                if card.houses_built == 4 and card.hotel_built == 0:
                    if player.cur_balance > card.hotel_cost:
                        player.cur_balance -= card.hotel_cost
                        card.hotel_built = 1
                    else:
                        player.cur_balance -= card.hotel_cost
                        card.hotel_built = 1
                        player.isBankrupt = True
                else:
                    if player.cur_balance > card.house_cost:
                        player.cur_balance -= card.house_cost
                        card.houses_built += 1
                    else:
                        player.cur_balance -= card.house_cost
                        card.hotel_built += 1
                        player.isBankrupt = True
            else:
                Mark = []

                player = Players[cur_player]

                for color_list in player.color_cards_owned:
                    Mark.extend(color_list)
                
                # display build window

                if Mark != []:
                    # adding static part
                    
                    screen.fill(BACKGROUND_COLOR)

                    create_board(screen)

                    create_game_options(screen)

                    create_player_info(screen,Players,Cards,cur_player)

                    for player in Players:
                        player.move_player(screen,player.cur_position)


                    update_game_build(screen,Players,Cards,cur_player,Cards_Rects,Option_Rects,Info_Cards_Rects,Mark)

        else:
            Mark = []

            player = Players[cur_player]

            for color_list in player.color_cards_owned:
                Mark.extend(color_list)
            
            # display build window

            if Mark != []:
                # adding static part
                
                screen.fill(BACKGROUND_COLOR)

                create_board(screen)

                create_game_options(screen)

                create_player_info(screen,Players,Cards,cur_player)

                for player in Players:
                    player.move_player(screen,player.cur_position)


                update_game_build(screen,Players,Cards,cur_player,Cards_Rects,Option_Rects,Info_Cards_Rects,Mark)
            



    

    

    
