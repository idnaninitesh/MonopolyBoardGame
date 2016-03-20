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

1) Allow user to select one or more property for selling
2) Allow user to enter amount
3) Allow user to select one or more property for buying
4) Allow user to ask for money
5) Validate the property involved in trade
6) Update the status

"""


def update_game_trade(screen,Players,Cards,cur_player,other_player,Cards_Rects,Option_Rects,Info_Cards_Rects,Cur_Mark,Other_Mark,Cur_Other_Mark,Other_Other_Mark):


    send_amount = 0
    receive_amount = 0
    send_property = set()
    receive_property = set()


    offer,send_amount,send_property,receive_amount,receive_property = display_trade_window(screen,Players,Cards,cur_player,other_player,Cur_Mark,Other_Mark,Cur_Other_Mark,Other_Other_Mark,send_amount,receive_amount,send_property,receive_property)


    if offer == True:
        
        if (send_property != set() or receive_property != set()) and (send_property.issubset(set(Cur_Mark)) and receive_property.issubset(set(Other_Mark))):

            Send_Cards = []
            Receive_Cards = []
        
            for send_index in send_property:
                Send_Cards.append(Cards[send_index])

            for receive_index in receive_property:
                Receive_Cards.append(Cards[receive_index])

            
            screen.fill(BACKGROUND_COLOR)

            create_board(screen,Cards)

            create_game_options(screen)
            
            for player in Players:
                player.move_player(screen,player.cur_position)

            create_player_info(screen,Players,Cards,cur_player)

            # confirmation prompt
            # show trade infomation


            

            trade_prop = display_trade_confirm_window(screen,Send_Cards,send_amount,Receive_Cards,receive_amount)


            if trade_prop == True:

                player = Players[cur_player]
                other = Players[other_player]

                # trade property action

                if send_amount > 0:
                    other.cur_balance += send_amount
                    player.cur_balance -= send_amount


                if receive_amount > 0:
                    other.cur_balance -= receive_amount
                    player.cur_balance += receive_amount

                if send_property != set():
                    send_property = list(send_property)

                    for send_index in send_property:

                        if Cards[send_index].status == 1:
                            player.property_owned.remove(send_index)
                            other.property_owned.append(send_index)
                        elif Cards[send_index].status == 2:
                            player.property_mortgaged.remove(send_index)
                            other.property_mortgaged.append(send_index)

                        if send_index in RAILS_CARDS:
                            player.total_rails_owned -= 1
                            other.total_rails_owned += 1
                        elif send_index in UTILITY_CARDS:
                            player.total_utilities_owned -= 1
                            other.total_utilities_owned += 1
                        else:

                            del_color = []

                            for color_cards in player.color_cards_owned:
                                if send_index in color_cards:
                                    del_color = color_cards

                            if del_color != []:
                                player.color_cards_owned.remove(del_color)

                            property_owned = set(other.property_owned)

                            if set(BROWN_CARDS).issubset(property_owned) and BROWN_CARDS not in other.color_cards_owned:
                                other.color_cards_owned.append(BROWN_CARDS)
                            if set(LIGHT_BLUE_CARDS).issubset(property_owned) and LIGHT_BLUE_CARDS not in other.color_cards_owned:
                                other.color_cards_owned.append(LIGHT_BLUE_CARDS)
                            if set(PINK_CARDS).issubset(property_owned) and PINK_CARDS not in other.color_cards_owned:
                                other.color_cards_owned.append(PINK_CARDS)
                            if set(ORANGE_CARDS).issubset(property_owned) and ORANGE_CARDS not in other.color_cards_owned:
                                other.color_cards_owned.append(ORANGE_CARDS)
                            if set(RED_CARDS).issubset(property_owned) and RED_CARDS not in other.color_cards_owned:
                                other.color_cards_owned.append(RED_CARDS)
                            if set(YELLOW_CARDS).issubset(property_owned) and YELLOW_CARDS not in other.color_cards_owned:
                                other.color_cards_owned.append(YELLOW_CARDS)
                            if set(GREEN_CARDS).issubset(property_owned) and GREEN_CARDS not in other.color_cards_owned:
                                other.color_cards_owned.append(GREEN_CARDS)
                            if set(BLUE_CARDS).issubset(property_owned) and BLUE_CARDS not in other.color_cards_owned:
                                other.color_cards_owned.append(BLUE_CARDS)    




                if receive_property != set():
                    receive_property = list(receive_property)

                    for receive_index in receive_property:

                        if Cards[receive_index].status == 1:
                            other.property_owned.remove(receive_index)
                            player.property_owned.append(receive_index)
                        elif Cards[receive_index].status == 2:
                            other.property_mortgaged.remove(receive_index)
                            player.property_mortgaged.append(receive_index)

                        if receive_index in RAILS_CARDS:
                            other.total_rails_owned -= 1
                            player.total_rails_owned += 1
                        elif receive_index in UTILITY_CARDS:
                            other.total_utilities_owned -= 1
                            player.total_utilities_owned += 1
                        else:

                            del_color = []

                            for color_cards in other.color_cards_owned:
                                if receive_index in color_cards:
                                    del_color = color_cards

                            if del_color != []:
                                other.color_cards_owned.remove(del_color)

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
                    # adding static part
                    
                    screen.fill(BACKGROUND_COLOR)

                    create_board(screen,Cards)

                    create_game_options(screen)
                    
                    for player in Players:
                        player.move_player(screen,player.cur_position)

                    create_player_info(screen,Players,Cards,cur_player)
                                
                    update_game_trade(screen,Players,Cards,cur_player,other_player,Cards_Rects,Option_Rects,Info_Cards_Rects,Cur_Mark,Other_Mark)


                                                
                
        else:

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
                # adding static part
                
                screen.fill(BACKGROUND_COLOR)

                create_board(screen,Cards)

                create_game_options(screen)
                
                for player in Players:
                    player.move_player(screen,player.cur_position)

                create_player_info(screen,Players,Cards,cur_player)
                            
                update_game_trade(screen,Players,Cards,cur_player,other_player,Cards_Rects,Option_Rects,Info_Cards_Rects,Cur_Mark,Other_Mark)

            



        
            

            

            

