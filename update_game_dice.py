# provide mortgage option if rent cannot be payed (will do this after mortgage)

import pygame
import sys
from random import *
from pygame.locals import *

from variables import *
from Card import *
from Player import *
from create_board import *
from create_game_options import *
from create_player_info import *
from handle_mouse_event import *
from handle_game import *
from handle_quit_player import *
from display_windows import *

"""
Rules :

1) if player crosses go add 200 in his balance
2) if a player arrives on a property
    - if some player owns it pay rent to that player
    - if no one owns it prompt him whether to buy or auction
    - on railroads collect amount based on no of railroads to the holder
    - on gov utilities if 1 utility is owned steps*4 if both 10*steps
3) if a player arrives on a chance or commuity card select a random card and implement its details
4) income tax or luxury tax deduct 200
5) jail collect 50
6) free parking do nothing


"""



def update_game_dice(screen,initial_card,final_card,no1,no2,Players,Cards,cur_player):

    player = Players[cur_player]
    steps = no1 + no2

    # passed go
    # show go window

    

    if final_card < initial_card:
        
        display_pass_go_window(screen)
        
        player.cur_balance += 200

        screen.fill(BACKGROUND_COLOR)

        create_board(screen)

        create_game_options(screen)

        create_player_info(screen,Players,Cards,cur_player)

        for temp in Players:
            temp.move_player(screen,temp.cur_position)


    # go card

    if final_card == 0:
        player.cur_balance += 200

    # chance cards
    # display card information
    # execute card detail

    elif final_card == 7 or final_card == 22 or final_card == 36:
        new_card = execute_chance(screen,final_card,Players,Cards,cur_player)
        if new_card != final_card:
            
            screen.fill(BACKGROUND_COLOR)

            create_board(screen)

            create_game_options(screen)

            create_player_info(screen,Players,Cards,cur_player)

            for player in Players:
                player.move_player(screen,player.cur_position)


            final_card = update_game_dice(screen,initial_card,new_card,no1,no2,Players,Cards,cur_player)
            

    # community chest cards
    # display card information
    # execute card detail
    
    elif final_card == 2 or final_card == 17 or final_card == 33:
        new_card = execute_community(screen,final_card,Players,Cards,cur_player)
        if new_card != final_card:
            
            screen.fill(BACKGROUND_COLOR)

            create_board(screen)

            create_game_options(screen)

            create_player_info(screen,Players,Cards,cur_player)

            for player in Players:
                player.move_player(screen,player.cur_position)


            final_card = update_game_dice(screen,initial_card,new_card,no1,no2,Players,Cards,cur_player)

    # jail or go to jail
    # go to jail - display go to jail window
    # allow player to use jail card if he has it
    # else pay $50 value
    
    elif final_card == 10 or final_card == 30:

        if final_card == 30:

            display_go_to_jail_window(screen)

            screen.fill(BACKGROUND_COLOR)

            create_board(screen)

            create_game_options(screen)

            create_player_info(screen,Players,Cards,cur_player)

            for player in Players:
                player.move_player(screen,player.cur_position)

            

        if player.jail_card == True:
            # if he wants to use jail card
            use_card = display_jail_card_window(screen)

            #does not uses the jail card hence pay fine pressed cancel

            if use_card == False:
                if player.cur_balance > 50:
                    player.cur_balance -= 50
                else:
                    player.cur_balance -= 50
                    player.isBankrupt = True
            else:
                player.jail_card = False
        else:
            display_jail_fine_window(screen)
            if player.cur_balance > 50:
                player.cur_balance -= 50
            else:
                player.cur_balance -= 50
                player.isBankrupt = True
        
        final_card = 10

        

    # income or luxury tax
    # display tax window
    # deduct $200 balance from his account

    elif final_card == 4 or final_card == 38:

        display_tax_pay_window(screen,final_card)
        
        if player.cur_balance > 200:
            player.cur_balance -= 200
        else:
            player.cur_balance -= 200
            player.isBankrupt = True


    # property cards

    elif final_card != 20 and final_card != 0:


        # check status
        # 0 - available 1 - bought 2 - mortgaged
            

        if Cards[final_card].status == 0:
            
            buy_prop = display_buy_property_window(screen,final_card,Players,Cards,cur_player)

            # buys property
            # pay cost
            # update card status
            # update player property
            # if utility or railroad update count
            
            if buy_prop == True:
                player.cur_balance -= Cards[final_card].cost
                Cards[final_card].status = 1
                
                player.property_owned.append(final_card)
                if final_card == 12 or final_card == 28:
                    player.total_utilities_owned += 1
                elif final_card == 5 or final_card == 15 or final_card == 25 or final_card == 35:
                    player.total_rails_owned += 1
                else:
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
                    

                        
                        
                    
                    
                
        elif Cards[final_card].status == 1:
            
            prop_holder = None

            player = Players[cur_player]

            for temp in Players:
                if player != temp and final_card in temp.property_owned:
                    prop_holder = temp
                    break

            # none implies property is mortgaged
            
            if prop_holder != None:

                # railroads

                if final_card == 5 or final_card == 15 or final_card == 25 or final_card == 35:
                    rent = 25 * 2**(prop_holder.total_rails_owned-1)

                # utilities

                elif final_card == 12 or final_card == 28:
                    rent = 4*steps
                    if prop_holder.total_utilities_owned == 2:
                        rent = 10*steps

                else:
                    rent = Cards[final_card].rent

                    if Cards[final_card].houses_built > 0:
                        rent = Cards[final_card].house_rent[Cards[final_card].houses_built-1]

                    if Cards[final_card].hotel_built > 0:
                        rent = Cards[final_card].hotel_rent
                    
                display_rent_payment_window(screen,rent,prop_holder)

                if player.cur_balance > rent:
                    player.cur_balance -= rent
                else:
                    player.cur_balance -= rent
                    player.isBankrupt = True
                    Players[holder].cur_balance += rent                    

                
                    


    
        
    return final_card



"""

1) Advance to Go (Collect $200) 
2) Advance to Illinois Ave. 
3) Advance token to the nearest Railroad and pay owner twice the rental to which he/she is otherwise entitled. If Railroad is unowned, you may buy it from the Bank. (There are two of these.) 
4) Advance to St. Charles Place – if you pass Go, collect $200 
5) Bank pays you dividend of $50 
6) Get out of Jail free – this card may be kept until needed, or traded/sold 
7) Go back 3 spaces 
8) Go directly to Jail – do not pass Go, do not collect $200 
9) Make general repairs on all your property – for each house pay $25 – for each hotel $100 
10) Pay poor tax of $15 
11) Take a trip to Reading Railroad – if you pass Go collect $200 
12) Take a walk on the Boardwalk – advance token to Boardwalk 
13) You have been elected chairman of the board – pay each player $50 
14) Your building loan matures – collect $150 
15) You have won a crossword competition - collect $100


"""

def execute_chance(screen,final_card,Players,Cards,cur_player):

    player = Players[cur_player]
    card = randint(1,15)

    display_chance_window(screen,card)

    if card == 1:
        final_card = 0
    elif card == 2:
        final_card = 24
    elif card == 3:
        final_card = ((round(final_card/10))*10 + 5)%40
    elif card == 4:
        if final_card > 11:
            player.cur_balance += 200
        final_card = 11
    elif card == 5:
        player.cur_balance += 50
    elif card == 6:
        player.jail_card = True
    elif card == 7:
        final_card -= 3
    elif card == 8:
        final_card = 10
    elif card == 9:
        for prop in player.property_owned:
            if Cards[prop].hotel_built > 0:
                if player.cur_balance > 100:
                    player.cur_balance -= 100
                else:
                    player.cur_balance -= 100
                    player.isBankrupt = True
            elif Cards[prop].houses_built > 0:
                if player.cur_balance > 25 * Cards[prop].houses_built:
                    player.cur_balance -= 25 * Cards[prop].houses_built
                else:
                    player.cur_balance -= 25 * Cards[prop].houses_built
                    player.isBankrupt = True
    elif card == 10:
        if player.cur_balance > 15:
            player.cur_balance -= 15
        else:
            player.cur_balance -= 15
            player.isBankrupt = True
    elif card == 11:
        if final_card > 5:
            player.cur_balance += 200
        final_card = 5
    elif card == 12:
        final_card = 39
    elif card == 13:
        for temp in Players:
            if player != temp:
                if player.cur_balance > 50:
                    player.cur_balance -= 50
                else:
                    player.cur_balance -= 50
                    player.isBankrupt = True
                temp.cur_balance += 50
    elif card == 14:
        player.cur_balance += 150
    elif card == 15:
        player.cur_balance += 100


    return final_card
        
        
        
    
    


"""

1) Advance to Go (Collect $200) 
2) Bank error in your favor – collect $75 
3) Doctor's fees – Pay $50 
4) Get out of jail free – this card may be kept until needed, or sold 
5) Go to jail – go directly to jail – Do not pass Go, do not collect $200 
6) It is your birthday Collect $10 from each player 
7) Grand Opera Night – collect $50 from every player for opening night seats 
8) Income Tax refund – collect $20 
9) Life Insurance Matures – collect $100 
10) Pay Hospital Fees of $100 
11) Pay School Fees of $50 
12) Receive $25 Consultancy Fee 
13) You are assessed for street repairs – $40 per house, $115 per hotel 
14) You have won second prize in a beauty contest– collect $10 
15) You inherit $100 
16) From sale of stock you get $50 
17) Holiday Fund matures - Receive $100

"""


def execute_community(screen,final_card,Players,Cards,cur_player):


    player = Players[cur_player]
    card = randint(1,17)

    display_community_window(screen,card)

    if card == 1:
        final_card = 0
    elif card == 2:
        player.cur_balance += 75
    elif card == 3:
        if player.cur_balance > 50:
            player.cur_balance -= 50
        else:
            player.isBankrupt = True
    elif card == 4:
        player.jail_card = True
    elif card == 5:
        final_card = 10
    elif card == 6:
        for temp in Players:
            if player != temp:
                if temp.cur_balance > 10:
                    temp.cur_balance -= 10
                else:
                    temp.cur_balance -= 10
                    temp.isBankrupt = True

                player.cur_balance += 10
    elif card == 7:
        for temp in Players:
            if player != temp:
                if temp.cur_balance > 50:
                    temp.cur_balance -= 50
                else:
                    temp.cur_balance -= 50
                    temp.isBankrupt = True

                player.cur_balance += 50
    elif card == 8:
        player.cur_balance += 20
    elif card == 9:
        player.cur_balance += 100
    elif card == 10:
        if player.cur_balance > 100:
            player.cur_balance -= 100
        else:
            player.cur_balance -= 100
            player.isBankrupt = True
    elif card == 11:
        if player.cur_balance > 50:
            player.cur_balance -= 50
        else:
            player.cur_balance -= 50
            player.isBankrupt = True
    elif card == 12:
        player.cur_balance += 125
    elif card == 13:
        for prop in player.property_owned:
            if Cards[prop].hotel_built > 0:
                if player.cur_balance > 115:
                    player.cur_balance -= 115
                else:
                    player.cur_balance -= 115
                    player.isBankrupt = True
            elif Cards[prop].houses_built > 0:
                if player.cur_balance > 40 * Cards[prop].houses_built:
                    player.cur_balance -= 40 * Cards[prop].houses_built
                else:
                    player.cur_balance -= 40 * Cards[prop].houses_built
                    player.isBankrupt = True
    elif card == 14:
        player.cur_balance += 10
    elif card == 15:
        player.cur_balance += 100
    elif card == 16:
        player.cur_balance += 50
    elif card == 17:
        player.cur_balance += 100


    return final_card
        



    

        
        
    
