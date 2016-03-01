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
1) Property owned can be mortgaged to the bank at half the cost
2) If house or hotel is built on card sell all the house/hotel
3) Add property in property_mortgaged

"""

def update_game_mortgage(screen,Players,Cards,cur_player,Cards_Rects,Option_Rects,Info_Cards_Rects,Mark):

    # removing cards with houses/hotel built on them

    for card in Mark:
        if Cards[card].hotel_built == 1 or Cards[card].houses_built > 0:
            Mark.remove(card)


    # get the card that was selected
    mortgage_card = display_mortgage_window(screen,Players,Cards,cur_player,Mark)

    # check if the card is valid
    # check the card against selling rules

    if mortgage_card != None:
        if mortgage_card in Mark:

            card = Cards[mortgage_card]

            screen.fill(BACKGROUND_COLOR)

            create_board(screen)

            create_game_options(screen)
            
            for player in Players:
                player.move_player(screen,player.cur_position)

            create_player_info(screen,Players,Cards,cur_player)

            # confirmation prompt
            # show mortgage infomation

            mortgage_prop = display_mortgage_confirm_window(screen,card)



            # update card status and player balance

            if mortgage_prop == True:

                player = Players[cur_player]
                # mortgage property action

                player.cur_balance += card.mortgage_value
                player.property_owned.remove(card.id_no)
                player.property_mortgaged.append(card.id_no)
                card.status = 2

                
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
                
                # display mortgage window

                if Mark != []:
                    # adding static part
                    
                    screen.fill(BACKGROUND_COLOR)

                    create_board(screen)

                    create_game_options(screen)

                    create_player_info(screen,Players,Cards,cur_player)

                    for player in Players:
                        player.move_player(screen,player.cur_position)


                    update_game_mortgage(screen,Players,Cards,cur_player,Cards_Rects,Option_Rects,Info_Cards_Rects,Mark)


        else:
            Mark = []

            player = Players[cur_player]

            for prop in player.property_owned:
                Mark.append(prop)
           
            # display mortgage window

            if Mark != []:
                # adding static part
                
                screen.fill(BACKGROUND_COLOR)

                create_board(screen)

                create_game_options(screen)

                create_player_info(screen,Players,Cards,cur_player)

                for player in Players:
                    player.move_player(screen,player.cur_position)


                update_game_mortgage(screen,Players,Cards,cur_player,Cards_Rects,Option_Rects,Info_Cards_Rects,Mark)
            


