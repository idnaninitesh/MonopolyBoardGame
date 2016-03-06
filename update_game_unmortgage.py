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
1) Property mortgaged can be unmortgaged from the bank at mortgage cost + 10% interest
3) Add property in property_owned

"""

def update_game_unmortgage(screen,Players,Cards,cur_player,Cards_Rects,Option_Rects,Info_Cards_Rects,Mark):


    # get the card that was selected
    unmortgage_card = display_unmortgage_window(screen,Players,Cards,cur_player,Mark)

    # check if the card is valid
    # check the card against selling rules
    # check if card's unmortgage cost is less than player's current balance

    if unmortgage_card != None:
        if unmortgage_card in Mark and int(Cards[unmortgage_card].mortgage_value*1.1) <= Players[cur_player].cur_balance:

            card = Cards[unmortgage_card]

            screen.fill(BACKGROUND_COLOR)

            create_board(screen,Cards)

            create_game_options(screen)
            
            for player in Players:
                player.move_player(screen,player.cur_position)

            create_player_info(screen,Players,Cards,cur_player)

            # confirmation prompt
            # show unmortgage infomation

            unmortgage_prop = display_unmortgage_confirm_window(screen,card)



            # update card status and player balance

            if unmortgage_prop == True:

                player = Players[cur_player]
                # unmortgage property action

                player.cur_balance -= int(card.mortgage_value*1.1)
                player.property_mortgaged.remove(card.id_no)
                player.property_owned.append(card.id_no)
                card.status = 1

                
                # check rail,utility or color card
                if card.id_no in RAILS_CARDS:
                    player.total_rails_owned += 1
                elif card.id_no in UTILITY_CARDS:
                    player.total_utilities_owned += 1
                else:
                    
                    # finding color group to which the card belongs

                    property_owned = set(player.property_owned)
                    
                    if set(BROWN_CARDS).issubset(property_owned) and BROWN_CARDS not in player.color_cards_owned:
                        player.color_cards_owned.append(BROWN_CARDS)
                    if set(LIGHT_BLUE_CARDS).issubset(property_owned) and LIGHT_BLUE_CARDS not in player.color_cards_owned:
                        player.color_cards_owned.append(LIGHT_BLUE_CARDS)
                    if set(PINK_CARDS).issubset(property_owned) and PINK_CARDS not in player.color_cards_owned:
                        player.color_cards_owned.append(PINK_CARDS)
                    if set(ORANGE_CARDS).issubset(property_owned) and ORANGE_CARDS not in player.color_cards_owned:
                        player.color_cards_owned.append(ORANGE_CARDS)
                    if set(RED_CARDS).issubset(property_owned) and RED_CARDS not in player.color_cards_owned:
                        player.color_cards_owned.append(RED_CARDS)
                    if set(YELLOW_CARDS).issubset(property_owned) and YELLOW_CARDS not in player.color_cards_owned:
                        player.color_cards_owned.append(YELLOW_CARDS)
                    if set(GREEN_CARDS).issubset(property_owned) and GREEN_CARDS not in player.color_cards_owned:
                        player.color_cards_owned.append(GREEN_CARDS)
                    if set(BLUE_CARDS).issubset(property_owned) and BLUE_CARDS not in player.color_cards_owned:
                        player.color_cards_owned.append(BLUE_CARDS)    

                     
            else:

                Mark = []

                player = Players[cur_player]

                for prop in player.property_mortgaged:
                    Mark.append(prop)
                
                # display unmortgage window

                if Mark != []:
                    # adding static part
                    
                    screen.fill(BACKGROUND_COLOR)

                    create_board(screen,Cards)

                    create_game_options(screen)

                    create_player_info(screen,Players,Cards,cur_player)

                    for player in Players:
                        player.move_player(screen,player.cur_position)


                    update_game_unmortgage(screen,Players,Cards,cur_player,Cards_Rects,Option_Rects,Info_Cards_Rects,Mark)


        else:
            Mark = []

            player = Players[cur_player]

            for prop in player.property_mortgaged:
                Mark.append(prop)
           
            # display unmortgage window

            if Mark != []:
                # adding static part
                
                screen.fill(BACKGROUND_COLOR)

                create_board(screen,Cards)

                create_game_options(screen)

                create_player_info(screen,Players,Cards,cur_player)

                for player in Players:
                    player.move_player(screen,player.cur_position)


                update_game_unmortgage(screen,Players,Cards,cur_player,Cards_Rects,Option_Rects,Info_Cards_Rects,Mark)
            


