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
1) Property owned will be sold at 90% of the price to the bank
2) Property mortgaged will be sold at 90% of price
3) If houses/hotel is built on property sell them in the reverse order
4) Display properties on which house can/should be sold

"""

def update_game_sell(screen,Players,Cards,cur_player,Cards_Rects,Option_Rects,Info_Cards_Rects,Mark):

    card_list = []
    flag = 0
    # removing cards with houses one less than the remaining houses in same color

    for color_cards in Players[cur_player].color_cards_owned:
        # color_cards = [1,3]
        for card in color_cards:
            card_list.append(Cards[card])
        # card_list(Card[1],Card[3])
        min_house_card = min(card_list,key=attrgetter('houses_built'))
        if min_house_card.houses_built == 4:     # hotel
            for crd in color_cards:
                if Cards[crd].hotel_built == 1:
                    flag = 1
            if flag == 1:       # hotel built on any card ; flag = 0 -> 4 houses on all cards
                for crd in color_cards:
                    if Cards[crd].hotel_built == 0:
                        if crd in Mark:
                            Mark.remove(crd)
        else:                   # house
            for crd in color_cards:
                if Cards[crd].houses_built != min_house_card.houses_built:
                    flag = 1
            if flag == 1:       #extra house built on some card ; flag = 0 -> all card have 0 houses
                for crd in color_cards:
                    if Cards[crd].houses_built == min_house_card.houses_built:
                        if crd in Mark:
                            Mark.remove(crd)
    
    
    # get the card that was selected
    sell_card = display_sell_window(screen,Players,Cards,cur_player,Mark)


    # check if the card is valid
    # check the card against selling rules

    if sell_card != None:
        if sell_card in Mark:

            card = Cards[sell_card]

            screen.fill(BACKGROUND_COLOR)

            create_board(screen,Cards)

            create_game_options(screen)
            
            for player in Players:
                player.move_player(screen,player.cur_position)

            create_player_info(screen,Players,Cards,cur_player)

            # confirmation prompt
            # show sell infomation

            sell_prop = display_sell_confirm_window(screen,card)



            # update card status and player balance

            if sell_prop == True:

                player = Players[cur_player]
                # sell property action
                
                if card.hotel_built == 1:       # selling hotel
                    
                    player.cur_balance += (card.hotel_cost//2)
                    card.hotel_built = 0
                elif card.houses_built > 0:     # selling house
                    
                    player.cur_balance += (card.house_cost//2)
                    card.houses_built -= 1
                elif card.status == 2:          # mortgaged property

                    player.cur_balance -= card.mortgage_value
                    player.cur_balance += int(card.cost*0.9)
                    card.status = 0
                    player.property_mortgaged.remove(card.id_no)
                else:                           # owned property
                    player.cur_balance += int(card.cost*0.9)
                    card.status = 0
                    player.property_owned.remove(card.id_no)
                    
                    # check rail,utility or color card
                    if card.id_no in RAILS_CARDS:
                        player.total_rails_owned -= 1
                    elif card.id_no in UTILITY_CARDS:
                        player.total_utilities_owned -= 1
                    else:
                        del_color = []

                        # finding color group to which the card belongs
                        
                        for color_cards in player.color_cards_owned:
                            if card.id_no in color_cards:
                                del_color = color_cards

                        if del_color != []:
                            player.color_cards_owned.remove(del_color)
                    
            else:

                Mark = []

                player = Players[cur_player]

                for prop in player.property_owned:
                    Mark.append(prop)

                for prop in player.property_mortgaged:
                    Mark.append(prop)
                
                # display sell window

                if Mark != []:
                    # adding static part
                    
                    screen.fill(BACKGROUND_COLOR)

                    create_board(screen,Cards)

                    create_game_options(screen)

                    create_player_info(screen,Players,Cards,cur_player)

                    for player in Players:
                        player.move_player(screen,player.cur_position)


                    update_game_sell(screen,Players,Cards,cur_player,Cards_Rects,Option_Rects,Info_Cards_Rects,Mark)


        else:
            Mark = []

            player = Players[cur_player]

            for prop in player.property_owned:
                Mark.append(prop)

            for prop in player.property_mortgaged:
                Mark.append(prop)
            
            # display build window

            if Mark != []:
                # adding static part
                
                screen.fill(BACKGROUND_COLOR)

                create_board(screen,Cards)

                create_game_options(screen)

                create_player_info(screen,Players,Cards,cur_player)

                for player in Players:
                    player.move_player(screen,player.cur_position)


                update_game_sell(screen,Players,Cards,cur_player,Cards_Rects,Option_Rects,Info_Cards_Rects,Mark)
            

    




    
   
