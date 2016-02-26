# implement chance and community chest cards
# implement buy and auction property
# provide mortgage option if rent cannot be payed

import pygame
import sys
from pygame.locals import *

from variables import *
from create_board import *
from create_game_options import *
from create_player_info import *
from handle_mouse_event import *
from Card import *
from Player import *

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



def update_game_dice(initial_card,final_card,no1,no2,Players,Cards,cur_player):

    player = Players[cur_player]
    flag = 1
    steps = no1 + no2

    # chance cards

    if final_card == 7 or final_card == 22 or final_card == 36:
        print("Chance")

    # community chest cards
    
    elif final_card == 2 or final_card == 17 or final_card == 33:
        print("Community Chest")

    # jail or go to jail

    elif final_card == 10 or final_card == 30:
        if player.cur_balance > 50:
            player.cur_balance -= 50
        else:
            player.isBankrupt = True
        final_card = 10

    # income or luxury tax

    elif final_card == 4 or final_card == 38:
        if player.cur_balance > 200:
            player.cur_balance -= 200
        else:
            player.isBankrupt = True

    # property cards 

    elif final_card != 20:


        # check status
        # 0 - available 1 - bought 2 - mortgaged

        if Cards[final_card].status == 0:
            print("Hello")

            
        elif Cards[final_card].status == 1:
            
            prop_holder = None

            for temp in Players:
                if final_card in temp.property_owned:
                    prop_holder = temp
                    break

            # none implies property is mortgaged
            
            if holder != None:

                # railroads

                if final_card == 5 or final_card == 15 or final_card == 25 or final_card == 35:
                    rent = 25 * 2**prop_holder.total_rails_owned

                # utilities

                elif final_card == 12 or final_card == 28:
                    rent = 4*steps
                    if prop_holder.total_utilities_owned == 2:
                        rent = 10*steps

                else:
                    rent = Cards[final_card].rent

                    if houses_built > 0:
                        rent = Cards[final_card].house_rent[houses_built-1]

                    if hotel_built > 0:
                        rent = Cards[final_card].hotel_rent
                    
                pygame.draw.rect(screen,
                                 LIGHT_BLUE,
                                 ((320,210),
                                 (440,340)),5)

                font = pygame.font.SysFont(CARD_TEXT_STYLE, 15)
                screen.blit(font.render('Pay M ' + str(rent) + ' to ' + str(prop_holder.name),True,BLACK),(450,270))

                pygame.draw.rect(screen,
                                 BLUE,
                                 ((320 + OPTION_MARGIN,550 - OPTION_HEIGHT - OPTION_MARGIN),
                                  (OPTION_WIDTH,OPTION_HEIGHT)))

                font = pygame.font.SysFont(CARD_TEXT_STYLE, 30)
                screen.blit(font.render('AGREE',True,WHITE),(370,485))


 

                clock = pygame.time.Clock()

                start = False

                # Rent Payment Display

                while not start:
        
                    for event in pygame.event.get():

                        if event.type == pygame.QUIT:
                            start = True
                        elif event.type == pygame.MOUSEBUTTONDOWN:
                
                            mouse_pos = pygame.mouse.get_pos()

                            x = mouse_pos[0]
                            y = mouse_pos[1]
            
                            # start clicked
        
                            if x >= 360 and x <= 490 and y >= 480 and y <= 520:
                                start = True
    
                                # adding all the static items
                    
                                screen.fill(BACKGROUND_COLOR)
    
                                create_board(screen)
        
                                create_game_options(screen)

                                roll_dice(screen,no1,no2)


                    clock.tick(60)

                    pygame.display.update()



                if player.cur_balance > rent:
                    player.cur_balance -= rent
                else:
                    player.isBankrupt = True
                    Players[holder].cur_balance += rent                    

                
                    


    
    # passed go

    if flag and final_card < initial_card:
        player.cur_balance += 200
        
    return final_card
    
    

    
