
import pygame
import sys
from random import *
from pygame.locals import *

from variables import *
from Player import *
from Card import *
from ask_for_game_details import *
from create_board import *
from create_game_options import *
from create_player_info import *
from handle_mouse_event import *


#   --------------  START GAME  -----------------

# display window to ask user to start the game

def display_start_game_window(screen,Players,Cards,cur_player):
    

    pygame.gfxdraw.box(screen,
                       ((ACTION_SCREEN_LEFT,ACTION_SCREEN_TOP),
                        (ACTION_SCREEN_WIDTH,ACTION_SCREEN_HEIGHT)),TRANSPARENT)

    font = pygame.font.SysFont(CARD_TEXT_STYLE, 25)
    screen.blit(font.render('START GAME',True,WHITE),(ACTION_SCREEN_LEFT + 150,ACTION_SCREEN_TOP + 60))

    pygame.draw.rect(screen,
                     BLUE,
                     ((ACTION_SCREEN_LEFT + OPTION_MARGIN,ACTION_SCREEN_TOP + ACTION_SCREEN_HEIGHT - OPTION_HEIGHT - OPTION_MARGIN),
                      (OPTION_WIDTH,OPTION_HEIGHT)))

    font = pygame.font.SysFont(CARD_TEXT_STYLE, 25)
    screen.blit(font.render('START',True,WHITE),(ACTION_SCREEN_LEFT + OPTION_MARGIN + 10,ACTION_SCREEN_TOP + ACTION_SCREEN_HEIGHT - OPTION_HEIGHT - OPTION_MARGIN + 5))


    pygame.draw.rect(screen,
                     RED,
                     ((ACTION_SCREEN_LEFT + ACTION_SCREEN_WIDTH - OPTION_WIDTH - OPTION_MARGIN,ACTION_SCREEN_TOP + ACTION_SCREEN_HEIGHT - OPTION_HEIGHT - OPTION_MARGIN),
                      (OPTION_WIDTH,OPTION_HEIGHT)))

    font = pygame.font.SysFont(CARD_TEXT_STYLE, 25)
    screen.blit(font.render('QUIT',True,WHITE),(ACTION_SCREEN_LEFT + ACTION_SCREEN_WIDTH - OPTION_MARGIN - OPTION_WIDTH + 10,ACTION_SCREEN_TOP + ACTION_SCREEN_HEIGHT - OPTION_HEIGHT - OPTION_MARGIN + 5))


    clock = pygame.time.Clock()

    done = False
    start = False


    while not start:
        
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                done = True
                start = True
            elif event.type == pygame.MOUSEBUTTONDOWN:
                
                mouse_pos = pygame.mouse.get_pos()

                x = mouse_pos[0]
                y = mouse_pos[1]

                # start clicked

                if x >= ACTION_SCREEN_LEFT + OPTION_MARGIN and x <= ACTION_SCREEN_LEFT + OPTION_MARGIN + OPTION_WIDTH  and y >= ACTION_SCREEN_TOP + ACTION_SCREEN_HEIGHT - OPTION_HEIGHT - OPTION_MARGIN and y <= ACTION_SCREEN_TOP + ACTION_SCREEN_HEIGHT - OPTION_MARGIN:
                    done = False
                    start = True
    
                    # adding all the static items
                    
                    screen.fill(BACKGROUND_COLOR)
    
                    create_board(screen)
        
                    create_game_options(screen)

                    create_player_info(screen,Players,Cards,cur_player)

                    roll_dice(screen,4,2)

                    for player in Players:
                        player.move_player(screen,player.cur_position)
    
                # quit clicked

                if x >= ACTION_SCREEN_LEFT + ACTION_SCREEN_WIDTH - OPTION_WIDTH - OPTION_MARGIN and x <= ACTION_SCREEN_LEFT + ACTION_SCREEN_WIDTH - OPTION_MARGIN and y >= ACTION_SCREEN_TOP + ACTION_SCREEN_HEIGHT - OPTION_HEIGHT - OPTION_MARGIN  and y <= ACTION_SCREEN_TOP + ACTION_SCREEN_HEIGHT - OPTION_MARGIN:
                    done = True
                    start = True

        

        clock.tick(60)

        pygame.display.update()


    return done




#   ----------------    RENT PAYMENT    ----------------

#display window to inform payment of rent

def display_rent_payment_window(screen,rent,prop_holder):
    

    pygame.gfxdraw.box(screen,
                       ((ACTION_SCREEN_LEFT,ACTION_SCREEN_TOP),
                        (ACTION_SCREEN_WIDTH,ACTION_SCREEN_HEIGHT)),TRANSPARENT)

    font = pygame.font.SysFont(CARD_TEXT_STYLE, 25)
    screen.blit(font.render('Pay M ' + str(rent) + ' to ' + str(prop_holder.name),True,WHITE),(ACTION_SCREEN_LEFT + 150,ACTION_SCREEN_TOP + 60))


    pygame.display.update()
    pygame.time.delay(ACTION_SCREEN_DELAY)

    """

    clock = pygame.time.Clock()

    start = False


    while not start:

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                start = True
            elif event.type == pygame.MOUSEBUTTONDOWN:
    
                mouse_pos = pygame.mouse.get_pos()

                x = mouse_pos[0]
                y = mouse_pos[1]

                # agree clicked

                if x >= ACTION_SCREEN_LEFT + OPTION_MARGIN + 10 and x <= ACTION_SCREEN_LEFT + OPTION_MARGIN + OPTION_WIDTH + 10 and y >= 480 and y <= 520:
                    start = True



        clock.tick(60)

        pygame.display.update()

    """



#   -----------------   JAIL CARD   ---------------

# display window to prompt player for use of jail card

def display_jail_card_window(screen):

    pygame.gfxdraw.box(screen,
                       ((ACTION_SCREEN_LEFT,ACTION_SCREEN_TOP),
                        (ACTION_SCREEN_WIDTH,ACTION_SCREEN_HEIGHT)),TRANSPARENT)

    font = pygame.font.SysFont(CARD_TEXT_STYLE, 25)
    screen.blit(font.render('USE JAIL CARD',True,WHITE),(ACTION_SCREEN_LEFT + 20,ACTION_SCREEN_TOP + 60))

    pygame.draw.rect(screen,
                     BLUE,
                     ((ACTION_SCREEN_LEFT + OPTION_MARGIN,ACTION_SCREEN_TOP + ACTION_SCREEN_HEIGHT - OPTION_HEIGHT - OPTION_MARGIN),
                      (OPTION_WIDTH,OPTION_HEIGHT)))

    font = pygame.font.SysFont(CARD_TEXT_STYLE, 25)
    screen.blit(font.render('USE',True,WHITE),(ACTION_SCREEN_LEFT + OPTION_MARGIN + 10,ACTION_SCREEN_TOP + ACTION_SCREEN_HEIGHT - OPTION_HEIGHT - OPTION_MARGIN + 5))


    pygame.draw.rect(screen,
                     RED,
                     ((ACTION_SCREEN_LEFT + ACTION_SCREEN_WIDTH - OPTION_WIDTH - OPTION_MARGIN,ACTION_SCREEN_TOP + ACTION_SCREEN_HEIGHT - OPTION_HEIGHT - OPTION_MARGIN),
                      (OPTION_WIDTH,OPTION_HEIGHT)))

    font = pygame.font.SysFont(CARD_TEXT_STYLE, 25)
    screen.blit(font.render('PAY $50',True,WHITE),(ACTION_SCREEN_LEFT + ACTION_SCREEN_WIDTH - OPTION_WIDTH - OPTION_MARGIN + 10,ACTION_SCREEN_TOP + ACTION_SCREEN_HEIGHT - OPTION_HEIGHT - OPTION_MARGIN + 5))


    clock = pygame.time.Clock()

    start = False
    use_card = False


    while not start:
        
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                start = True
            elif event.type == pygame.MOUSEBUTTONDOWN:
                
                mouse_pos = pygame.mouse.get_pos()

                x = mouse_pos[0]
                y = mouse_pos[1]

                # use clicked

                if x >= ACTION_SCREEN_LEFT + OPTION_MARGIN and x <= ACTION_SCREEN_LEFT + OPTION_MARGIN + OPTION_WIDTH and y >= ACTION_SCREEN_TOP + ACTION_SCREEN_HEIGHT - OPTION_MARGIN - OPTION_HEIGHT and y <= ACTION_SCREEN_TOP + ACTION_SCREEN_HEIGHT - OPTION_MARGIN:
                    use_card = True
                    start = True
    
    
                # cancel clicked

                if x >= ACTION_SCREEN_LEFT + ACTION_SCREEN_WIDTH - OPTION_MARGIN - OPTION_WIDTH and x <= ACTION_SCREEN_LEFT + ACTION_SCREEN_WIDTH - OPTION_MARGIN and y >= ACTION_SCREEN_TOP + ACTION_SCREEN_HEIGHT - OPTION_HEIGHT - OPTION_MARGIN and y <= ACTION_SCREEN_TOP + ACTION_SCREEN_HEIGHT - OPTION_MARGIN:
                    use_card = False
                    start = True

        

        clock.tick(60)

        pygame.display.update()

    
    return use_card
                       


#   --------------------    BUY PROPERTY    -------------------

# display window to ask user if he wants to buy property or not

def display_buy_property_window(screen,final_card,Players,Cards,cur_player):

    pygame.gfxdraw.box(screen,
                       ((ACTION_SCREEN_LEFT,ACTION_SCREEN_TOP),
                        (ACTION_SCREEN_WIDTH,ACTION_SCREEN_HEIGHT)),TRANSPARENT)

    font = pygame.font.SysFont(CARD_TEXT_STYLE, 25)
    screen.blit(font.render('BUY ' + str(Cards[final_card].name),True,WHITE),(ACTION_SCREEN_LEFT + 20,ACTION_SCREEN_TOP + 30))
    screen.blit(font.render('COST : M ' + str(Cards[final_card].cost),True,WHITE),(ACTION_SCREEN_LEFT + 90,ACTION_SCREEN_TOP + 70))


    pygame.draw.rect(screen,
                     BLUE,
                     ((ACTION_SCREEN_LEFT + OPTION_MARGIN,ACTION_SCREEN_TOP + ACTION_SCREEN_HEIGHT - OPTION_HEIGHT - OPTION_MARGIN),
                      (OPTION_WIDTH,OPTION_HEIGHT)))

    font = pygame.font.SysFont(CARD_TEXT_STYLE, 25)
    screen.blit(font.render('BUY',True,WHITE),(ACTION_SCREEN_LEFT + OPTION_MARGIN + 10,ACTION_SCREEN_TOP + ACTION_SCREEN_HEIGHT - OPTION_HEIGHT - OPTION_MARGIN + 5))


    pygame.draw.rect(screen,
                     RED,
                     ((760 - OPTION_WIDTH - OPTION_MARGIN,550 - OPTION_HEIGHT - OPTION_MARGIN),
                      (OPTION_WIDTH,OPTION_HEIGHT)))

    font = pygame.font.SysFont(CARD_TEXT_STYLE, 25)
    screen.blit(font.render('CANCEL',True,WHITE),(ACTION_SCREEN_LEFT + ACTION_SCREEN_WIDTH - OPTION_WIDTH - OPTION_MARGIN + 10,ACTION_SCREEN_TOP + ACTION_SCREEN_HEIGHT - OPTION_HEIGHT - OPTION_MARGIN + 5))


    clock = pygame.time.Clock()

    start = False
    buy_prop = False


    while not start:
        
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                start = True
            elif event.type == pygame.MOUSEBUTTONDOWN:
                
                mouse_pos = pygame.mouse.get_pos()

                x = mouse_pos[0]
                y = mouse_pos[1]

                # buy clicked

                if x >= ACTION_SCREEN_LEFT + OPTION_MARGIN and x <= ACTION_SCREEN_LEFT + OPTION_MARGIN + OPTION_WIDTH and y >= ACTION_SCREEN_TOP + ACTION_SCREEN_HEIGHT - OPTION_HEIGHT - OPTION_MARGIN and y <= ACTION_SCREEN_TOP + ACTION_SCREEN_HEIGHT - OPTION_MARGIN:
                    buy_prop = True
                    start = True
    
    
                # cancel clicked

                if x >= ACTION_SCREEN_LEFT + ACTION_SCREEN_WIDTH - OPTION_WIDTH - OPTION_MARGIN and x <= ACTION_SCREEN_LEFT + ACTION_SCREEN_WIDTH - OPTION_MARGIN  and y >= ACTION_SCREEN_TOP + ACTION_SCREEN_HEIGHT - OPTION_HEIGHT - OPTION_MARGIN and y <= ACTION_SCREEN_TOP + ACTION_SCREEN_HEIGHT - OPTION_MARGIN:
                    buy_prop = False
                    start = True

        

        clock.tick(60)

        pygame.display.update()

    
    return buy_prop
                       


#   ----------------    GO TO JAIL  -----------------

#display window to inform movemement to jail

def display_go_to_jail_window(screen):
    

    pygame.gfxdraw.box(screen,
                       ((ACTION_SCREEN_LEFT,ACTION_SCREEN_TOP),
                        (ACTION_SCREEN_WIDTH,ACTION_SCREEN_HEIGHT)),TRANSPARENT)

    font = pygame.font.SysFont(CARD_TEXT_STYLE, 25)
    screen.blit(font.render('GO TO JAIL',True,WHITE),(ACTION_SCREEN_LEFT + 150,ACTION_SCREEN_TOP + 60))

    pygame.display.update()
    pygame.time.delay(ACTION_SCREEN_DELAY)

    """

    clock = pygame.time.Clock()

    start = False


    while not start:

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                start = True
            elif event.type == pygame.MOUSEBUTTONDOWN:
    
                mouse_pos = pygame.mouse.get_pos()

                x = mouse_pos[0]
                y = mouse_pos[1]

                # go clicked

                if x >= ACTION_SCREEN_LEFT + OPTION_MARGIN + 10 and x <= ACTION_SCREEN_LEFT + OPTION_MARGIN + OPTION_WIDTH + 10 and y >= 480 and y <= 520:
                    start = True



        clock.tick(60)

        pygame.display.update()

    """


#   ----------------    END TURN    ------------------

# display window to allow user to end turn
# also allow game options click except roll dice

def display_end_turn_window(screen,Players,Cards,cur_player,Cards_Rects,Option_Rects,Info_Cards_Rects):

    pygame.gfxdraw.box(screen,
                       ((ACTION_SCREEN_LEFT,ACTION_SCREEN_TOP),
                        (ACTION_SCREEN_WIDTH,ACTION_SCREEN_HEIGHT)),TRANSPARENT)

    font = pygame.font.SysFont(CARD_TEXT_STYLE, 25)
    screen.blit(font.render('END TURN',True,WHITE),(ACTION_SCREEN_LEFT + 20,ACTION_SCREEN_TOP + 60))


    pygame.draw.rect(screen,
                     BLUE,
                     ((ACTION_SCREEN_LEFT + OPTION_MARGIN,ACTION_SCREEN_TOP + ACTION_SCREEN_HEIGHT - OPTION_HEIGHT - OPTION_MARGIN),
                      (OPTION_WIDTH,OPTION_HEIGHT)))

    font = pygame.font.SysFont(CARD_TEXT_STYLE,25)
    screen.blit(font.render('END',True,WHITE),(ACTION_SCREEN_LEFT + OPTION_MARGIN + 10,ACTION_SCREEN_TOP + ACTION_SCREEN_HEIGHT - OPTION_HEIGHT - OPTION_MARGIN + 5))


    clock = pygame.time.Clock()

    start = False

    isRunning = False

    while not start:

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                start = True
            elif event.type == pygame.MOUSEBUTTONDOWN:
    
                mouse_pos = pygame.mouse.get_pos()

                x = mouse_pos[0]
                y = mouse_pos[1]

                # end turn clicked

                if x >= ACTION_SCREEN_LEFT + OPTION_MARGIN and x <= ACTION_SCREEN_LEFT + OPTION_MARGIN + OPTION_WIDTH and y >= ACTION_SCREEN_TOP + ACTION_SCREEN_HEIGHT - OPTION_HEIGHT - OPTION_MARGIN and y <= ACTION_SCREEN_TOP + ACTION_SCREEN_HEIGHT - OPTION_MARGIN:
                    start = True

                else:
                    Rects = get_rect_pressed_type(mouse_pos,Cards_Rects,Option_Rects,Info_Cards_Rects)

                    if Rects != None:

                        # rects is option,info or board
                        
                        rect_index = get_rect_pressed_index(mouse_pos,Rects)

                        # take necessary action based on the event that occured in the game
                        # kind of semaphore I think ;)

                        if Rects == Option_Rects and rect_index > 0 and rect_index < len(Rects):
    
                            # rect is among the Rects
                            
                            if isRunning == False:
                                from handle_game import handle_game

                                isRunning = True
                                cur_player,isRunning = handle_game(screen,Rects,rect_index,Players,Cards,cur_player,Cards_Rects,Option_Rects,Info_Cards_Rects,isRunning)
                                display_end_turn_window(screen,Players,Cards,cur_player,Cards_Rects,Option_Rects,Info_Cards_Rects)
                                start = True



        clock.tick(60)

        pygame.display.update()



#   -----------------   CHANCE  ------------------
    
# display window to show the chance card drawn

def display_chance_window(screen,card):


    pygame.gfxdraw.box(screen,
                       ((ACTION_SCREEN_LEFT,ACTION_SCREEN_TOP),
                        (ACTION_SCREEN_WIDTH,ACTION_SCREEN_HEIGHT)),TRANSPARENT)

    font = pygame.font.SysFont(CARD_TEXT_STYLE, 25)

    if card == 1:
        screen.blit(font.render('Advance to Go (Collect $200)',True,WHITE),(ACTION_SCREEN_LEFT + 20,ACTION_SCREEN_TOP + 30))
    elif card == 2:
        screen.blit(font.render('Advance to Illinois Avenue',True,WHITE),(ACTION_SCREEN_LEFT + 20,ACTION_SCREEN_TOP + 30))
    elif card == 3:
        screen.blit(font.render('Advance token to the nearest Railroad',True,WHITE),(ACTION_SCREEN_LEFT + 20,ACTION_SCREEN_TOP + 30))
    elif card == 4:
        screen.blit(font.render('Advance to St. Charles Place – if you ',True,WHITE),(ACTION_SCREEN_LEFT + 20,ACTION_SCREEN_TOP + 30))
        screen.blit(font.render(' pass Go, collect $200',True,WHITE),(ACTION_SCREEN_LEFT + 20,ACTION_SCREEN_TOP + 70))
    elif card == 5:
        screen.blit(font.render('Bank pays you dividend of $50',True,WHITE),(ACTION_SCREEN_LEFT + 20,ACTION_SCREEN_TOP + 30))
    elif card == 6:
        screen.blit(font.render('Get out of Jail free – this card may be ',True,WHITE),(ACTION_SCREEN_LEFT + 20,ACTION_SCREEN_TOP + 30))
        screen.blit(font.render(' kept until needed, or traded/sold',True,WHITE),(ACTION_SCREEN_LEFT + 20,ACTION_SCREEN_TOP + 70))
    elif card == 7:
        screen.blit(font.render('Go back 3 spaces ',True,WHITE),(ACTION_SCREEN_LEFT + 20,ACTION_SCREEN_TOP + 30))
    elif card == 8:
        screen.blit(font.render('Go directly to Jail – do not pass Go, ',True,WHITE),(ACTION_SCREEN_LEFT + 20,ACTION_SCREEN_TOP + 30))
        screen.blit(font.render(' do not collect $200',True,WHITE),(ACTION_SCREEN_LEFT + 20,ACTION_SCREEN_TOP + 70))
    elif card == 9:
        screen.blit(font.render('Make general repairs on all your property – ',True,WHITE),(ACTION_SCREEN_LEFT + 20,ACTION_SCREEN_TOP + 30))
        screen.blit(font.render('for each house pay $25 – for each hotel $100 ',True,WHITE),(ACTION_SCREEN_LEFT + 20,ACTION_SCREEN_TOP + 70))
    elif card == 10:
        screen.blit(font.render('Pay poor tax of $15',True,WHITE),(ACTION_SCREEN_LEFT + 20,ACTION_SCREEN_TOP + 30))
    elif card == 11:
        screen.blit(font.render('Take a trip to Reading Railroad – if',True,WHITE),(ACTION_SCREEN_LEFT + 20,ACTION_SCREEN_TOP + 30))
        screen.blit(font.render('you pass Go collect $200 ',True,WHITE),(ACTION_SCREEN_LEFT + 20,ACTION_SCREEN_TOP + 70))
    elif card == 12:
        screen.blit(font.render('Take a walk on the Boardwalk – ',True,WHITE),(ACTION_SCREEN_LEFT + 20,ACTION_SCREEN_TOP + 30))
        screen.blit(font.render('advance token to Boardwalk',True,WHITE),(ACTION_SCREEN_LEFT + 20,ACTION_SCREEN_TOP + 70))
    elif card == 13:
        screen.blit(font.render('You have been elected chairman ',True,WHITE),(ACTION_SCREEN_LEFT + 20,ACTION_SCREEN_TOP + 30))
        screen.blit(font.render('of the board – pay each player $50',True,WHITE),(ACTION_SCREEN_LEFT + 20,ACTION_SCREEN_TOP + 70))
    elif card == 14:
        screen.blit(font.render('Your building loan matures – collect $150',True,WHITE),(ACTION_SCREEN_LEFT + 20,ACTION_SCREEN_TOP + 30))
    elif card == 15:
        screen.blit(font.render('You have won a crossword competition',True,WHITE),(ACTION_SCREEN_LEFT + 20,ACTION_SCREEN_TOP + 30))
        screen.blit(font.render(' - collect $100',True,WHITE),(ACTION_SCREEN_LEFT + 20,ACTION_SCREEN_TOP + 70))


    pygame.display.update()
    pygame.time.delay(ACTION_SCREEN_DELAY)



#   ----------------    COMMUNITY CHEST ----------------

# display window to show the community chance card drawn

def display_community_window(screen,card):

    pygame.gfxdraw.box(screen,
                       ((ACTION_SCREEN_LEFT,ACTION_SCREEN_TOP),
                        (ACTION_SCREEN_WIDTH,ACTION_SCREEN_HEIGHT)),TRANSPARENT)

    font = pygame.font.SysFont(CARD_TEXT_STYLE, 25)

    if card == 1:
        screen.blit(font.render('Advance to Go (Collect $200)',True,WHITE),(ACTION_SCREEN_LEFT + 20,ACTION_SCREEN_TOP + 30))
    elif card == 2:
        screen.blit(font.render('Bank error in your favor -',True,WHITE),(ACTION_SCREEN_LEFT + 20,ACTION_SCREEN_TOP + 30))
        screen.blit(font.render(' collect $75',True,WHITE),(ACTION_SCREEN_LEFT + 20,ACTION_SCREEN_TOP + 70))
    elif card == 3:
        screen.blit(font.render('Doctor\'s fee - Pay $50',True,WHITE),(ACTION_SCREEN_LEFT + 20,ACTION_SCREEN_TOP + 30))
    elif card == 4:
        screen.blit(font.render('Get out of Jail free – this card may be ',True,WHITE),(ACTION_SCREEN_LEFT + 20,ACTION_SCREEN_TOP + 30))
        screen.blit(font.render(' kept until needed, or traded/sold',True,WHITE),(ACTION_SCREEN_LEFT + 20,ACTION_SCREEN_TOP + 70))
    elif card == 5:
        screen.blit(font.render('Go directly to Jail – do not pass Go, ',True,WHITE),(ACTION_SCREEN_LEFT + 20,ACTION_SCREEN_TOP + 30))
        screen.blit(font.render(' do not collect $200',True,WHITE),(ACTION_SCREEN_LEFT + 20,ACTION_SCREEN_TOP + 70))
    elif card == 6:
        screen.blit(font.render('It is your birthday Collect ',True,WHITE),(ACTION_SCREEN_LEFT + 20,ACTION_SCREEN_TOP + 30))
        screen.blit(font.render(' $10 from each player',True,WHITE),(ACTION_SCREEN_LEFT + 20,ACTION_SCREEN_TOP + 70))
    elif card == 7:
        screen.blit(font.render('Grand Opera Night - collect $50 ',True,WHITE),(ACTION_SCREEN_LEFT + 20,ACTION_SCREEN_TOP + 30))
        screen.blit(font.render(' for opening night seats',True,WHITE),(ACTION_SCREEN_LEFT + 20,ACTION_SCREEN_TOP + 70))
    elif card == 8:
        screen.blit(font.render('Income Tax Refund - collect $20 ',True,WHITE),(ACTION_SCREEN_LEFT + 20,ACTION_SCREEN_TOP + 30))
    elif card == 9:
        screen.blit(font.render('Life Insurance Matures - collect $100',True,WHITE),(ACTION_SCREEN_LEFT + 20,ACTION_SCREEN_TOP + 30))
    elif card == 10:
        screen.blit(font.render('Pay Hospital Fees of $100',True,WHITE),(ACTION_SCREEN_LEFT + 20,ACTION_SCREEN_TOP + 30))
    elif card == 11:
        screen.blit(font.render('Pay School Fees of $50',True,WHITE),(ACTION_SCREEN_LEFT + 20,ACTION_SCREEN_TOP + 30))
    elif card == 12:
        screen.blit(font.render('Receive $25 Consultancy Fees',True,WHITE),(ACTION_SCREEN_LEFT + 20,ACTION_SCREEN_TOP + 30))
    elif card == 13:
        screen.blit(font.render('You are assessed for street repairs ',True,WHITE),(ACTION_SCREEN_LEFT + 20,ACTION_SCREEN_TOP + 30))
        screen.blit(font.render('$40 per house, $115 per hotel',True,WHITE),(ACTION_SCREEN_LEFT + 20,ACTION_SCREEN_TOP + 70))
    elif card == 14:
        screen.blit(font.render('Your have won second prize in a beauty ',True,WHITE),(ACTION_SCREEN_LEFT + 20,ACTION_SCREEN_TOP + 30))
        screen.blit(font.render(' contest – collect $10',True,WHITE),(ACTION_SCREEN_LEFT + 20,ACTION_SCREEN_TOP + 70))
    elif card == 15:
        screen.blit(font.render('You inherit $100',True,WHITE),(ACTION_SCREEN_LEFT + 20,ACTION_SCREEN_TOP + 30))
    elif card == 16:
        screen.blit(font.render('From sale of stock you get $50',True,WHITE),(ACTION_SCREEN_LEFT + 20,ACTION_SCREEN_TOP + 30))
    elif card == 17:
        screen.blit(font.render('Holiday Fund matures - Receive $100',True,WHITE),(ACTION_SCREEN_LEFT + 20,ACTION_SCREEN_TOP + 30))
                    


    pygame.display.update()
    pygame.time.delay(ACTION_SCREEN_DELAY)



#   --------------- JAIL FINE   -----------------

# display window to inform payment of jail fine

def display_jail_fine_window(screen):
                    
    pygame.gfxdraw.box(screen,
                       ((ACTION_SCREEN_LEFT,ACTION_SCREEN_TOP),
                        (ACTION_SCREEN_WIDTH,ACTION_SCREEN_HEIGHT)),TRANSPARENT)

    font = pygame.font.SysFont(CARD_TEXT_STYLE, 25)
    screen.blit(font.render('IN JAIL PAY $50',True,WHITE),(ACTION_SCREEN_LEFT + 20,ACTION_SCREEN_TOP + 60))

    pygame.display.update()
    pygame.time.delay(ACTION_SCREEN_DELAY)


# display window to inform payment of luxury or income tax

def display_tax_pay_window(screen,final_card):
    

    pygame.gfxdraw.box(screen,
                       ((ACTION_SCREEN_LEFT,ACTION_SCREEN_TOP),
                        (ACTION_SCREEN_WIDTH,ACTION_SCREEN_HEIGHT)),TRANSPARENT)

    font = pygame.font.SysFont(CARD_TEXT_STYLE, 25)

    if final_card == 4:
        screen.blit(font.render('INCOME TAX PAY $200',True,WHITE),(ACTION_SCREEN_LEFT + 20,ACTION_SCREEN_TOP + 60))
    else:
        screen.blit(font.render('LUXURY TAX PAY $200',True,WHITE),(ACTION_SCREEN_LEFT + 20,ACTION_SCREEN_TOP + 60))


    pygame.display.update()
    pygame.time.delay(ACTION_SCREEN_DELAY)



#   ----------------    PASS GO --------------

# display window to inform passing go

def display_pass_go_window(screen):
                    
    pygame.gfxdraw.box(screen,
                       ((ACTION_SCREEN_LEFT,ACTION_SCREEN_TOP),
                        (ACTION_SCREEN_WIDTH,ACTION_SCREEN_HEIGHT)),TRANSPARENT)

    font = pygame.font.SysFont(CARD_TEXT_STYLE, 25)
    screen.blit(font.render('PASSED GO COLLECT $200',True,WHITE),(ACTION_SCREEN_LEFT + 20,ACTION_SCREEN_TOP + 60))

    pygame.display.update()
    pygame.time.delay(ACTION_SCREEN_DELAY)



#   ---------------- BUILD  -----------------

# display window to allow user to build houses/hotel

def display_build_window(screen,Players,Cards,cur_player,Mark):


    pygame.gfxdraw.box(screen,
                       ((ACTION_SCREEN_LEFT,180),
                        (ACTION_SCREEN_WIDTH,420)),TRANSPARENT)


    font = pygame.font.SysFont(CARD_TEXT_STYLE, 25)
    screen.blit(font.render('SELECT HIGHLIGHTED CARD',True,WHITE),(ACTION_SCREEN_LEFT + 20,200))


    create_info_cards(screen,ACTION_SCREEN_LEFT + 90,250)
    Build_Cards_Rects = create_info_rects(ACTION_SCREEN_LEFT + 90,250)

   #   UPDATING PLAYER PROPERTY

    for player_property in Mark:
        if Cards[player_property].color == "RED":
            color = RED
        elif Cards[player_property].color == "GREEN":
            color = GREEN
        elif Cards[player_property].color == "BLUE":
            color = BLUE
        elif Cards[player_property].color == "YELLOW":
            color = YELLOW
        elif Cards[player_property].color == "BLACK":
            color = BLACK
        elif Cards[player_property].color == "BROWN":
            color = BROWN
        elif Cards[player_property].color == "LIGHT_BLUE":
            color = LIGHT_BLUE
        elif Cards[player_property].color == "PINK":
            color = PINK
        elif Cards[player_property].color == "ORANGE":
            color = ORANGE
        else:
            color = WHITE

        pygame.draw.rect(screen,
                         color,
                         ((Build_Cards_Rects[player_property].left,
                          Build_Cards_Rects[player_property].top),
                          (INFO_CARD_WIDTH,
                           INFO_CARD_HEIGHT)))

    


    pygame.draw.rect(screen,
                     RED,
                     ((760 - OPTION_WIDTH - OPTION_MARGIN,550),
                      (OPTION_WIDTH,OPTION_HEIGHT)))

    font = pygame.font.SysFont(CARD_TEXT_STYLE, 25)
    screen.blit(font.render('CANCEL',True,WHITE),(ACTION_SCREEN_LEFT + ACTION_SCREEN_WIDTH - OPTION_WIDTH - OPTION_MARGIN + 10,560))



    clock = pygame.time.Clock()

    start = False
    build_card = None

    while not start:
        
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                start = True
            elif event.type == pygame.MOUSEBUTTONDOWN:
                
                mouse_pos = pygame.mouse.get_pos()

                x = mouse_pos[0]
                y = mouse_pos[1]

                # cancel clicked

                if x >= ACTION_SCREEN_LEFT + ACTION_SCREEN_WIDTH - OPTION_WIDTH - OPTION_MARGIN and x <= ACTION_SCREEN_LEFT + ACTION_SCREEN_WIDTH - OPTION_MARGIN  and y >= 550 and y <= 550 + OPTION_HEIGHT:
                    start = True

                else:
                    build_card = get_rect_pressed_index(mouse_pos,Build_Cards_Rects)
                    if build_card < len(Build_Cards_Rects):
                        start = True
                    



        

        clock.tick(60)

        pygame.display.update()



    return build_card        

    
# display window to confirm building of houses or hotel
    
def display_build_confirm_window(screen,card):

    pygame.gfxdraw.box(screen,
                       ((ACTION_SCREEN_LEFT,ACTION_SCREEN_TOP),
                        (ACTION_SCREEN_WIDTH,ACTION_SCREEN_HEIGHT)),TRANSPARENT)


    font = pygame.font.SysFont(CARD_TEXT_STYLE, 20)

    if card.houses_built == 4:
        screen.blit(font.render('Build HOTEL on ' + str(card.name),True,WHITE),(ACTION_SCREEN_LEFT + 20,ACTION_SCREEN_TOP + 10))
    else:
        screen.blit(font.render('Build HOUSE on ' + str(card.name),True,WHITE),(ACTION_SCREEN_LEFT + 20,ACTION_SCREEN_TOP + 10))
    screen.blit(font.render('COST : M ' + str(card.house_cost),True,WHITE),(ACTION_SCREEN_LEFT + 90,ACTION_SCREEN_TOP + 70))



    pygame.draw.rect(screen,
                     BLUE,
                     ((ACTION_SCREEN_LEFT + OPTION_MARGIN,ACTION_SCREEN_TOP + ACTION_SCREEN_HEIGHT - OPTION_HEIGHT - OPTION_MARGIN),
                      (OPTION_WIDTH,OPTION_HEIGHT)))

    font = pygame.font.SysFont(CARD_TEXT_STYLE, 25)
    screen.blit(font.render('BUILD',True,WHITE),(ACTION_SCREEN_LEFT + OPTION_MARGIN + 10,ACTION_SCREEN_TOP + ACTION_SCREEN_HEIGHT - OPTION_HEIGHT - OPTION_MARGIN + 5))


    pygame.draw.rect(screen,
                     RED,
                     ((760 - OPTION_WIDTH - OPTION_MARGIN,550 - OPTION_HEIGHT - OPTION_MARGIN),
                      (OPTION_WIDTH,OPTION_HEIGHT)))

    font = pygame.font.SysFont(CARD_TEXT_STYLE, 25)
    screen.blit(font.render('CANCEL',True,WHITE),(ACTION_SCREEN_LEFT + ACTION_SCREEN_WIDTH - OPTION_WIDTH - OPTION_MARGIN + 10,ACTION_SCREEN_TOP + ACTION_SCREEN_HEIGHT - OPTION_HEIGHT - OPTION_MARGIN + 5))


    clock = pygame.time.Clock()

    start = False
    build_prop = False

    while not start:
        
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                start = True
            elif event.type == pygame.MOUSEBUTTONDOWN:
                
                mouse_pos = pygame.mouse.get_pos()

                x = mouse_pos[0]
                y = mouse_pos[1]

                # build clicked

                if x >= ACTION_SCREEN_LEFT + OPTION_MARGIN and x <= ACTION_SCREEN_LEFT + OPTION_MARGIN + OPTION_WIDTH and y >= ACTION_SCREEN_TOP + ACTION_SCREEN_HEIGHT - OPTION_HEIGHT - OPTION_MARGIN and y <= ACTION_SCREEN_TOP + ACTION_SCREEN_HEIGHT - OPTION_MARGIN:
                    build_prop = True
                    start = True
    
    
                # cancel clicked

                if x >= ACTION_SCREEN_LEFT + ACTION_SCREEN_WIDTH - OPTION_WIDTH - OPTION_MARGIN and x <= ACTION_SCREEN_LEFT + ACTION_SCREEN_WIDTH - OPTION_MARGIN  and y >= ACTION_SCREEN_TOP + ACTION_SCREEN_HEIGHT - OPTION_HEIGHT - OPTION_MARGIN and y <= ACTION_SCREEN_TOP + ACTION_SCREEN_HEIGHT - OPTION_MARGIN:
                    build_prop = False
                    start = True

        

        clock.tick(60)

        pygame.display.update()

    
    return build_prop


#   --------------------    SELL    -------------------

#display window to allow user to sell property,hotel and houses

def display_sell_window(screen,Players,Cards,cur_player,Mark):


    pygame.gfxdraw.box(screen,
                       ((ACTION_SCREEN_LEFT,180),
                        (ACTION_SCREEN_WIDTH,420)),TRANSPARENT)


    font = pygame.font.SysFont(CARD_TEXT_STYLE, 25)
    screen.blit(font.render('SELECT HIGHLIGHTED CARD',True,WHITE),(ACTION_SCREEN_LEFT + 20,200))


    create_info_cards(screen,ACTION_SCREEN_LEFT + 90,250)
    Sell_Cards_Rects = create_info_rects(ACTION_SCREEN_LEFT + 90,250)

   #   UPDATING PLAYER PROPERTY

    for player_property in Mark:
        if Cards[player_property].color == "RED":
            color = RED
        elif Cards[player_property].color == "GREEN":
            color = GREEN
        elif Cards[player_property].color == "BLUE":
            color = BLUE
        elif Cards[player_property].color == "YELLOW":
            color = YELLOW
        elif Cards[player_property].color == "BLACK":
            color = BLACK
        elif Cards[player_property].color == "BROWN":
            color = BROWN
        elif Cards[player_property].color == "LIGHT_BLUE":
            color = LIGHT_BLUE
        elif Cards[player_property].color == "PINK":
            color = PINK
        elif Cards[player_property].color == "ORANGE":
            color = ORANGE
        else:
            color = WHITE

        pygame.draw.rect(screen,
                         color,
                         ((Sell_Cards_Rects[player_property].left,
                          Sell_Cards_Rects[player_property].top),
                          (INFO_CARD_WIDTH,
                           INFO_CARD_HEIGHT)))

    


    pygame.draw.rect(screen,
                     RED,
                     ((760 - OPTION_WIDTH - OPTION_MARGIN,550),
                      (OPTION_WIDTH,OPTION_HEIGHT)))

    font = pygame.font.SysFont(CARD_TEXT_STYLE, 25)
    screen.blit(font.render('CANCEL',True,WHITE),(ACTION_SCREEN_LEFT + ACTION_SCREEN_WIDTH - OPTION_WIDTH - OPTION_MARGIN + 10,560))



    clock = pygame.time.Clock()

    start = False
    sell_card = None

    while not start:
        
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                start = True
            elif event.type == pygame.MOUSEBUTTONDOWN:
                
                mouse_pos = pygame.mouse.get_pos()

                x = mouse_pos[0]
                y = mouse_pos[1]

                # cancel clicked

                if x >= ACTION_SCREEN_LEFT + ACTION_SCREEN_WIDTH - OPTION_WIDTH - OPTION_MARGIN and x <= ACTION_SCREEN_LEFT + ACTION_SCREEN_WIDTH - OPTION_MARGIN  and y >= 550 and y <= 550 + OPTION_HEIGHT:
                    start = True

                else:
                    sell_card = get_rect_pressed_index(mouse_pos,Sell_Cards_Rects)
                    if sell_card < len(Sell_Cards_Rects):
                        start = True
                    



        

        clock.tick(60)

        pygame.display.update()



    return sell_card        



# display window to confirm selling of houses or hotel or property

def display_sell_confirm_window(screen,card):

    pygame.gfxdraw.box(screen,
                       ((ACTION_SCREEN_LEFT,ACTION_SCREEN_TOP),
                        (ACTION_SCREEN_WIDTH,ACTION_SCREEN_HEIGHT)),TRANSPARENT)


    font = pygame.font.SysFont(CARD_TEXT_STYLE, 20)

    if card.hotel_built == 1:
        screen.blit(font.render('Sell HOTEL on ' + str(card.name),True,WHITE),(ACTION_SCREEN_LEFT + 20,ACTION_SCREEN_TOP + 10))
        screen.blit(font.render('RETURN VALUE : M ' + str(card.house_cost//2),True,WHITE),(ACTION_SCREEN_LEFT + 90,ACTION_SCREEN_TOP + 70))

    elif card.houses_built > 0:
        screen.blit(font.render('Sell HOUSE on ' + str(card.name),True,WHITE),(ACTION_SCREEN_LEFT + 20,ACTION_SCREEN_TOP + 10))
        screen.blit(font.render('RETURN VALUE : M ' + str(card.house_cost//2),True,WHITE),(ACTION_SCREEN_LEFT + 90,ACTION_SCREEN_TOP + 70))
    else:
        screen.blit(font.render('Sell Card ' + str(card.name),True,WHITE),(ACTION_SCREEN_LEFT + 20,ACTION_SCREEN_TOP + 10))
        screen.blit(font.render('RETURN VALUE : M ' + str(int(card.cost*0.9)),True,WHITE),(ACTION_SCREEN_LEFT + 90,ACTION_SCREEN_TOP + 70))





    pygame.draw.rect(screen,
                     BLUE,
                     ((ACTION_SCREEN_LEFT + OPTION_MARGIN,ACTION_SCREEN_TOP + ACTION_SCREEN_HEIGHT - OPTION_HEIGHT - OPTION_MARGIN),
                      (OPTION_WIDTH,OPTION_HEIGHT)))

    font = pygame.font.SysFont(CARD_TEXT_STYLE, 25)
    screen.blit(font.render('SELL',True,WHITE),(ACTION_SCREEN_LEFT + OPTION_MARGIN + 10,ACTION_SCREEN_TOP + ACTION_SCREEN_HEIGHT - OPTION_HEIGHT - OPTION_MARGIN + 5))


    pygame.draw.rect(screen,
                     RED,
                     ((760 - OPTION_WIDTH - OPTION_MARGIN,550 - OPTION_HEIGHT - OPTION_MARGIN),
                      (OPTION_WIDTH,OPTION_HEIGHT)))

    font = pygame.font.SysFont(CARD_TEXT_STYLE, 25)
    screen.blit(font.render('CANCEL',True,WHITE),(ACTION_SCREEN_LEFT + ACTION_SCREEN_WIDTH - OPTION_WIDTH - OPTION_MARGIN + 10,ACTION_SCREEN_TOP + ACTION_SCREEN_HEIGHT - OPTION_HEIGHT - OPTION_MARGIN + 5))


    clock = pygame.time.Clock()

    start = False
    sell_prop = False

    while not start:
        
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                start = True
            elif event.type == pygame.MOUSEBUTTONDOWN:
                
                mouse_pos = pygame.mouse.get_pos()

                x = mouse_pos[0]
                y = mouse_pos[1]

                # sell clicked

                if x >= ACTION_SCREEN_LEFT + OPTION_MARGIN and x <= ACTION_SCREEN_LEFT + OPTION_MARGIN + OPTION_WIDTH and y >= ACTION_SCREEN_TOP + ACTION_SCREEN_HEIGHT - OPTION_HEIGHT - OPTION_MARGIN and y <= ACTION_SCREEN_TOP + ACTION_SCREEN_HEIGHT - OPTION_MARGIN:
                    sell_prop = True
                    start = True
    
    
                # cancel clicked

                if x >= ACTION_SCREEN_LEFT + ACTION_SCREEN_WIDTH - OPTION_WIDTH - OPTION_MARGIN and x <= ACTION_SCREEN_LEFT + ACTION_SCREEN_WIDTH - OPTION_MARGIN  and y >= ACTION_SCREEN_TOP + ACTION_SCREEN_HEIGHT - OPTION_HEIGHT - OPTION_MARGIN and y <= ACTION_SCREEN_TOP + ACTION_SCREEN_HEIGHT - OPTION_MARGIN:
                    sell_prop = False
                    start = True

        

        clock.tick(60)

        pygame.display.update()

    
    return sell_prop


#   --------------------    MORTGAGE    ------------------

#display window to allow user to mortgage property

def display_mortgage_window(screen,Players,Cards,cur_player,Mark):


    pygame.gfxdraw.box(screen,
                       ((ACTION_SCREEN_LEFT,180),
                        (ACTION_SCREEN_WIDTH,420)),TRANSPARENT)


    font = pygame.font.SysFont(CARD_TEXT_STYLE, 25)
    screen.blit(font.render('SELECT HIGHLIGHTED CARD',True,WHITE),(ACTION_SCREEN_LEFT + 20,200))


    create_info_cards(screen,ACTION_SCREEN_LEFT + 90,250)
    Mortgage_Cards_Rects = create_info_rects(ACTION_SCREEN_LEFT + 90,250)

   #   UPDATING PLAYER PROPERTY

    for player_property in Mark:
        if Cards[player_property].color == "RED":
            color = RED
        elif Cards[player_property].color == "GREEN":
            color = GREEN
        elif Cards[player_property].color == "BLUE":
            color = BLUE
        elif Cards[player_property].color == "YELLOW":
            color = YELLOW
        elif Cards[player_property].color == "BLACK":
            color = BLACK
        elif Cards[player_property].color == "BROWN":
            color = BROWN
        elif Cards[player_property].color == "LIGHT_BLUE":
            color = LIGHT_BLUE
        elif Cards[player_property].color == "PINK":
            color = PINK
        elif Cards[player_property].color == "ORANGE":
            color = ORANGE
        else:
            color = WHITE

        pygame.draw.rect(screen,
                         color,
                         ((Mortgage_Cards_Rects[player_property].left,
                          Mortgage_Cards_Rects[player_property].top),
                          (INFO_CARD_WIDTH,
                           INFO_CARD_HEIGHT)))

    


    pygame.draw.rect(screen,
                     RED,
                     ((760 - OPTION_WIDTH - OPTION_MARGIN,550),
                      (OPTION_WIDTH,OPTION_HEIGHT)))

    font = pygame.font.SysFont(CARD_TEXT_STYLE, 25)
    screen.blit(font.render('CANCEL',True,WHITE),(ACTION_SCREEN_LEFT + ACTION_SCREEN_WIDTH - OPTION_WIDTH - OPTION_MARGIN + 10,560))



    clock = pygame.time.Clock()

    start = False
    mortgage_card = None

    while not start:
        
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                start = True
            elif event.type == pygame.MOUSEBUTTONDOWN:
                
                mouse_pos = pygame.mouse.get_pos()

                x = mouse_pos[0]
                y = mouse_pos[1]

                # cancel clicked

                if x >= ACTION_SCREEN_LEFT + ACTION_SCREEN_WIDTH - OPTION_WIDTH - OPTION_MARGIN and x <= ACTION_SCREEN_LEFT + ACTION_SCREEN_WIDTH - OPTION_MARGIN  and y >= 550 and y <= 550 + OPTION_HEIGHT:
                    start = True

                else:
                    mortgage_card = get_rect_pressed_index(mouse_pos,Mortgage_Cards_Rects)
                    if mortgage_card < len(Mortgage_Cards_Rects):
                        start = True
                    



        

        clock.tick(60)

        pygame.display.update()



    return mortgage_card        


# display window to confirm mortgage of property

def display_mortgage_confirm_window(screen,card):

    pygame.gfxdraw.box(screen,
                       ((ACTION_SCREEN_LEFT,ACTION_SCREEN_TOP),
                        (ACTION_SCREEN_WIDTH,ACTION_SCREEN_HEIGHT)),TRANSPARENT)


    font = pygame.font.SysFont(CARD_TEXT_STYLE, 20)

    screen.blit(font.render('Mortgage Card ' + str(card.name),True,WHITE),(ACTION_SCREEN_LEFT + 20,ACTION_SCREEN_TOP + 10))
    screen.blit(font.render('RETURN VALUE : M ' + str(card.mortgage_value),True,WHITE),(ACTION_SCREEN_LEFT + 90,ACTION_SCREEN_TOP + 70))





    pygame.draw.rect(screen,
                     BLUE,
                     ((ACTION_SCREEN_LEFT + OPTION_MARGIN,ACTION_SCREEN_TOP + ACTION_SCREEN_HEIGHT - OPTION_HEIGHT - OPTION_MARGIN),
                      (OPTION_WIDTH,OPTION_HEIGHT)))



    font = pygame.font.SysFont(CARD_TEXT_STYLE, 20)
    screen.blit(font.render('MORTGAGE',True,WHITE),(ACTION_SCREEN_LEFT + OPTION_MARGIN + 10,ACTION_SCREEN_TOP + ACTION_SCREEN_HEIGHT - OPTION_HEIGHT - OPTION_MARGIN + 5))


    pygame.draw.rect(screen,
                     RED,
                     ((760 - OPTION_WIDTH - OPTION_MARGIN,550 - OPTION_HEIGHT - OPTION_MARGIN),
                      (OPTION_WIDTH,OPTION_HEIGHT)))

    font = pygame.font.SysFont(CARD_TEXT_STYLE, 25)
    screen.blit(font.render('CANCEL',True,WHITE),(ACTION_SCREEN_LEFT + ACTION_SCREEN_WIDTH - OPTION_WIDTH - OPTION_MARGIN + 10,ACTION_SCREEN_TOP + ACTION_SCREEN_HEIGHT - OPTION_HEIGHT - OPTION_MARGIN + 5))


    clock = pygame.time.Clock()

    start = False
    mortgage_prop = False

    while not start:
        
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                start = True
            elif event.type == pygame.MOUSEBUTTONDOWN:
                
                mouse_pos = pygame.mouse.get_pos()

                x = mouse_pos[0]
                y = mouse_pos[1]

                # mortgage clicked

                if x >= ACTION_SCREEN_LEFT + OPTION_MARGIN and x <= ACTION_SCREEN_LEFT + OPTION_MARGIN + OPTION_WIDTH and y >= ACTION_SCREEN_TOP + ACTION_SCREEN_HEIGHT - OPTION_HEIGHT - OPTION_MARGIN and y <= ACTION_SCREEN_TOP + ACTION_SCREEN_HEIGHT - OPTION_MARGIN:
                    mortgage_prop = True
                    start = True
    
    
                # cancel clicked

                if x >= ACTION_SCREEN_LEFT + ACTION_SCREEN_WIDTH - OPTION_WIDTH - OPTION_MARGIN and x <= ACTION_SCREEN_LEFT + ACTION_SCREEN_WIDTH - OPTION_MARGIN  and y >= ACTION_SCREEN_TOP + ACTION_SCREEN_HEIGHT - OPTION_HEIGHT - OPTION_MARGIN and y <= ACTION_SCREEN_TOP + ACTION_SCREEN_HEIGHT - OPTION_MARGIN:
                    mortgage_prop = False
                    start = True

        

        clock.tick(60)

        pygame.display.update()

    
    return mortgage_prop


#   --------------------    UNMORTGAGE  ------------------

#display window to allow user to unmortgage property

def display_unmortgage_window(screen,Players,Cards,cur_player,Mark):


    pygame.gfxdraw.box(screen,
                       ((ACTION_SCREEN_LEFT,180),
                        (ACTION_SCREEN_WIDTH,420)),TRANSPARENT)


    font = pygame.font.SysFont(CARD_TEXT_STYLE, 25)
    screen.blit(font.render('SELECT HIGHLIGHTED CARD',True,WHITE),(ACTION_SCREEN_LEFT + 20,200))


    create_info_cards(screen,ACTION_SCREEN_LEFT + 90,250)
    Unmortgage_Cards_Rects = create_info_rects(ACTION_SCREEN_LEFT + 90,250)

   #   UPDATING PLAYER PROPERTY

    for player_property in Mark:
        if Cards[player_property].color == "RED":
            color = RED
        elif Cards[player_property].color == "GREEN":
            color = GREEN
        elif Cards[player_property].color == "BLUE":
            color = BLUE
        elif Cards[player_property].color == "YELLOW":
            color = YELLOW
        elif Cards[player_property].color == "BLACK":
            color = BLACK
        elif Cards[player_property].color == "BROWN":
            color = BROWN
        elif Cards[player_property].color == "LIGHT_BLUE":
            color = LIGHT_BLUE
        elif Cards[player_property].color == "PINK":
            color = PINK
        elif Cards[player_property].color == "ORANGE":
            color = ORANGE
        else:
            color = WHITE

        pygame.draw.rect(screen,
                         color,
                         ((Unmortgage_Cards_Rects[player_property].left,
                          Unmortgage_Cards_Rects[player_property].top),
                          (INFO_CARD_WIDTH,
                           INFO_CARD_HEIGHT)))

    


    pygame.draw.rect(screen,
                     RED,
                     ((760 - OPTION_WIDTH - OPTION_MARGIN,550),
                      (OPTION_WIDTH,OPTION_HEIGHT)))

    font = pygame.font.SysFont(CARD_TEXT_STYLE, 25)
    screen.blit(font.render('CANCEL',True,WHITE),(ACTION_SCREEN_LEFT + ACTION_SCREEN_WIDTH - OPTION_WIDTH - OPTION_MARGIN + 10,560))



    clock = pygame.time.Clock()

    start = False
    unmortgage_card = None

    while not start:
        
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                start = True
            elif event.type == pygame.MOUSEBUTTONDOWN:
                
                mouse_pos = pygame.mouse.get_pos()

                x = mouse_pos[0]
                y = mouse_pos[1]

                # cancel clicked

                if x >= ACTION_SCREEN_LEFT + ACTION_SCREEN_WIDTH - OPTION_WIDTH - OPTION_MARGIN and x <= ACTION_SCREEN_LEFT + ACTION_SCREEN_WIDTH - OPTION_MARGIN  and y >= 550 and y <= 550 + OPTION_HEIGHT:
                    start = True

                else:
                    unmortgage_card = get_rect_pressed_index(mouse_pos,Unmortgage_Cards_Rects)
                    if unmortgage_card < len(Unmortgage_Cards_Rects):
                        start = True
                    



        

        clock.tick(60)

        pygame.display.update()



    return unmortgage_card        


# display window to confirm remove mortgage of property

def display_unmortgage_confirm_window(screen,card):

    pygame.gfxdraw.box(screen,
                       ((ACTION_SCREEN_LEFT,ACTION_SCREEN_TOP),
                        (ACTION_SCREEN_WIDTH,ACTION_SCREEN_HEIGHT)),TRANSPARENT)


    font = pygame.font.SysFont(CARD_TEXT_STYLE, 20)

    screen.blit(font.render('Unmortgage Card ' + str(card.name),True,WHITE),(ACTION_SCREEN_LEFT + 20,ACTION_SCREEN_TOP + 10))
    screen.blit(font.render('COST : M ' + str(int(card.mortgage_value*1.1)),True,WHITE),(ACTION_SCREEN_LEFT + 90,ACTION_SCREEN_TOP + 70))





    pygame.draw.rect(screen,
                     BLUE,
                     ((ACTION_SCREEN_LEFT + OPTION_MARGIN,ACTION_SCREEN_TOP + ACTION_SCREEN_HEIGHT - OPTION_HEIGHT - OPTION_MARGIN),
                      (OPTION_WIDTH,OPTION_HEIGHT)))



    font = pygame.font.SysFont(CARD_TEXT_STYLE, 16)
    screen.blit(font.render('UNMORTGAGE',True,WHITE),(ACTION_SCREEN_LEFT + OPTION_MARGIN + 10,ACTION_SCREEN_TOP + ACTION_SCREEN_HEIGHT - OPTION_HEIGHT - OPTION_MARGIN + 5))


    pygame.draw.rect(screen,
                     RED,
                     ((760 - OPTION_WIDTH - OPTION_MARGIN,550 - OPTION_HEIGHT - OPTION_MARGIN),
                      (OPTION_WIDTH,OPTION_HEIGHT)))

    font = pygame.font.SysFont(CARD_TEXT_STYLE, 25)
    screen.blit(font.render('CANCEL',True,WHITE),(ACTION_SCREEN_LEFT + ACTION_SCREEN_WIDTH - OPTION_WIDTH - OPTION_MARGIN + 10,ACTION_SCREEN_TOP + ACTION_SCREEN_HEIGHT - OPTION_HEIGHT - OPTION_MARGIN + 5))


    clock = pygame.time.Clock()

    start = False
    unmortgage_prop = False

    while not start:
        
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                start = True
            elif event.type == pygame.MOUSEBUTTONDOWN:
                
                mouse_pos = pygame.mouse.get_pos()

                x = mouse_pos[0]
                y = mouse_pos[1]

                # unmortgage clicked

                if x >= ACTION_SCREEN_LEFT + OPTION_MARGIN and x <= ACTION_SCREEN_LEFT + OPTION_MARGIN + OPTION_WIDTH and y >= ACTION_SCREEN_TOP + ACTION_SCREEN_HEIGHT - OPTION_HEIGHT - OPTION_MARGIN and y <= ACTION_SCREEN_TOP + ACTION_SCREEN_HEIGHT - OPTION_MARGIN:
                    unmortgage_prop = True
                    start = True
    
    
                # cancel clicked

                if x >= ACTION_SCREEN_LEFT + ACTION_SCREEN_WIDTH - OPTION_WIDTH - OPTION_MARGIN and x <= ACTION_SCREEN_LEFT + ACTION_SCREEN_WIDTH - OPTION_MARGIN  and y >= ACTION_SCREEN_TOP + ACTION_SCREEN_HEIGHT - OPTION_HEIGHT - OPTION_MARGIN and y <= ACTION_SCREEN_TOP + ACTION_SCREEN_HEIGHT - OPTION_MARGIN:
                    unmortgage_prop = False
                    start = True

        

        clock.tick(60)

        pygame.display.update()

    
    return unmortgage_prop


#   --------------------    QUIT GAME   -----------------

# display window to ask user to quit the game

def display_quit_window(screen):
    

    pygame.gfxdraw.box(screen,
                       ((ACTION_SCREEN_LEFT,ACTION_SCREEN_TOP),
                        (ACTION_SCREEN_WIDTH,ACTION_SCREEN_HEIGHT)),TRANSPARENT)

    font = pygame.font.SysFont(CARD_TEXT_STYLE, 25)
    screen.blit(font.render('QUIT GAME',True,WHITE),(ACTION_SCREEN_LEFT + 150,ACTION_SCREEN_TOP + 60))

    pygame.draw.rect(screen,
                     BLUE,
                     ((ACTION_SCREEN_LEFT + OPTION_MARGIN,ACTION_SCREEN_TOP + ACTION_SCREEN_HEIGHT - OPTION_HEIGHT - OPTION_MARGIN),
                      (OPTION_WIDTH,OPTION_HEIGHT)))

    font = pygame.font.SysFont(CARD_TEXT_STYLE, 25)
    screen.blit(font.render('QUIT',True,WHITE),(ACTION_SCREEN_LEFT + OPTION_MARGIN + 10,ACTION_SCREEN_TOP + ACTION_SCREEN_HEIGHT - OPTION_HEIGHT - OPTION_MARGIN + 5))


    pygame.draw.rect(screen,
                     RED,
                     ((ACTION_SCREEN_LEFT + ACTION_SCREEN_WIDTH - OPTION_WIDTH - OPTION_MARGIN,ACTION_SCREEN_TOP + ACTION_SCREEN_HEIGHT - OPTION_HEIGHT - OPTION_MARGIN),
                      (OPTION_WIDTH,OPTION_HEIGHT)))

    font = pygame.font.SysFont(CARD_TEXT_STYLE, 25)
    screen.blit(font.render('CANCEL',True,WHITE),(ACTION_SCREEN_LEFT + ACTION_SCREEN_WIDTH - OPTION_MARGIN - OPTION_WIDTH + 10,ACTION_SCREEN_TOP + ACTION_SCREEN_HEIGHT - OPTION_HEIGHT - OPTION_MARGIN + 5))


    clock = pygame.time.Clock()

    done = False
    start = False


    while not start:
        
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                done = True
                start = True
            elif event.type == pygame.MOUSEBUTTONDOWN:
                
                mouse_pos = pygame.mouse.get_pos()

                x = mouse_pos[0]
                y = mouse_pos[1]

                # quit clicked

                if x >= ACTION_SCREEN_LEFT + OPTION_MARGIN and x <= ACTION_SCREEN_LEFT + OPTION_MARGIN + OPTION_WIDTH  and y >= ACTION_SCREEN_TOP + ACTION_SCREEN_HEIGHT - OPTION_HEIGHT - OPTION_MARGIN and y <= ACTION_SCREEN_TOP + ACTION_SCREEN_HEIGHT - OPTION_MARGIN:
                    done = True
                    start = True
    
                # cancel clicked

                if x >= ACTION_SCREEN_LEFT + ACTION_SCREEN_WIDTH - OPTION_WIDTH - OPTION_MARGIN and x <= ACTION_SCREEN_LEFT + ACTION_SCREEN_WIDTH - OPTION_MARGIN and y >= ACTION_SCREEN_TOP + ACTION_SCREEN_HEIGHT - OPTION_HEIGHT - OPTION_MARGIN  and y <= ACTION_SCREEN_TOP + ACTION_SCREEN_HEIGHT - OPTION_MARGIN:
                    done = False
                    start = True

        

        clock.tick(60)

        pygame.display.update()


    return done


#   ----------------    RULES   ------------------

def display_rules_window(screen):


    pygame.gfxdraw.box(screen,
                       ((0,0),
                        (1100,770)),TRANSPARENT)


    rulesImg = pygame.image.load('rules.png')
    rulesImg = pygame.transform.scale(rulesImg,(900,630))
    screen.blit(rulesImg,(100,70))
    

    pygame.draw.rect(screen,
                     BLUE,
                     ((500, 720),
                      (100,OPTION_HEIGHT)))

    font = pygame.font.SysFont(CARD_TEXT_STYLE, 25)
    screen.blit(font.render('DONE',True,WHITE),(510,725))


    clock = pygame.time.Clock()

    start = False


    while not start:
        
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                start = True
            elif event.type == pygame.MOUSEBUTTONDOWN:
                
                mouse_pos = pygame.mouse.get_pos()

                x = mouse_pos[0]
                y = mouse_pos[1]

                # quit clicked

                if x >= 500 and x <= 600  and y >= 720 and y <= 720 + OPTION_HEIGHT:
                    start = True
    
        

        clock.tick(60)

        pygame.display.update()



#   ----------------    TRADE   -----------------

# display window to select player to trade with

def display_select_trade_player_window(screen,Players,Cards,cur_player):

    pygame.gfxdraw.box(screen,
                       ((ACTION_SCREEN_LEFT,ACTION_SCREEN_TOP),
                        (ACTION_SCREEN_WIDTH,ACTION_SCREEN_HEIGHT)),TRANSPARENT)


    font = pygame.font.SysFont(CARD_TEXT_STYLE, 20)

    screen.blit(font.render('Select the player you want to trade with :',True,WHITE),(ACTION_SCREEN_LEFT + 20,ACTION_SCREEN_TOP + 10))

    current = Players[cur_player]

    rect_x = 320
    rect_y = 250
    rect_width = 420
    rect_height = 50
    rect_margin = 25
    
    Player_Boundary = []
            
    for player in Players:

        if player != current:
        
            if player.color == "RED":
                color = RED
            elif player.color == "GREEN":
                color = GREEN
            elif player.color == "BLUE":
                color = BLUE
            elif player.color == "YELLOW":
                color = YELLOW
            else:
                color = WHITE
    
            pygame.draw.rect(screen,
                             color,
                             ((rect_x,rect_y),
                             (rect_width,rect_height)),2)
            
    
            font = pygame.font.SysFont(CARD_TEXT_STYLE, 20)
            screen.blit(font.render('' + player.name, True, color), (rect_x + 20,rect_y + 10))
            screen.blit(font.render('M ' + str(player.cur_balance), True, color), (rect_x + 280,rect_y + 10))

            Player_Boundary.append((rect_x,rect_y))

            rect_y = rect_y + rect_height + rect_margin
            

        else:
            Player_Boundary.append((-1,-1))


    pygame.draw.rect(screen,
                     RED,
                     ((760 - OPTION_WIDTH - OPTION_MARGIN,550 - OPTION_HEIGHT - OPTION_MARGIN),
                      (OPTION_WIDTH,OPTION_HEIGHT)))

    font = pygame.font.SysFont(CARD_TEXT_STYLE, 25)
    screen.blit(font.render('CANCEL',True,WHITE),(ACTION_SCREEN_LEFT + ACTION_SCREEN_WIDTH - OPTION_WIDTH - OPTION_MARGIN + 10,ACTION_SCREEN_TOP + ACTION_SCREEN_HEIGHT - OPTION_HEIGHT - OPTION_MARGIN + 5))


    clock = pygame.time.Clock()

    start = False
    other_player = -1

    while not start:
        
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                start = True
            elif event.type == pygame.MOUSEBUTTONDOWN:
                
                mouse_pos = pygame.mouse.get_pos()


                x = mouse_pos[0]
                y = mouse_pos[1]

                for bound in Player_Boundary:
                    if x != -1 and y != -1 and x >= bound[0] and x <= bound[0] + rect_width and y >= bound[1] and y <= bound[1] + rect_height:
                        other_player = Player_Boundary.index(bound)
                        return other_player
    
                # cancel clicked

                if x >= ACTION_SCREEN_LEFT + ACTION_SCREEN_WIDTH - OPTION_WIDTH - OPTION_MARGIN and x <= ACTION_SCREEN_LEFT + ACTION_SCREEN_WIDTH - OPTION_MARGIN  and y >= ACTION_SCREEN_TOP + ACTION_SCREEN_HEIGHT - OPTION_HEIGHT - OPTION_MARGIN and y <= ACTION_SCREEN_TOP + ACTION_SCREEN_HEIGHT - OPTION_MARGIN:
                    other_player = -1
                    start = True

        

        clock.tick(60)

        pygame.display.update()

    return other_player


# display window to allow user to enter trade infomation

def display_trade_window(screen,Players,Cards,cur_player,other_player,Cur_Mark,Other_Mark,int_send,int_receive,int_send_prop,int_receive_prop):


    send_amount = int_send
    receive_amount = int_receive
    send_prop = int_send_prop
    receive_prop = int_receive_prop


    pygame.gfxdraw.box(screen,
                       ((175,150),
                        (650,450)),TRANSPARENT)


    font = pygame.font.SysFont(CARD_TEXT_STYLE, 25)
    screen.blit(font.render('TRADE WINDOW',True,WHITE),(450,170))


    # left cards
    
    create_info_cards(screen,200,200)
    Send_Cards_Rects = create_info_rects(200,200)

    # seperator
    pygame.draw.line(screen, WHITE, (500,200), (500,525))

    # right seperator
    create_info_cards(screen,525,200)
    Receive_Cards_Rects = create_info_rects(525,200)


   #   UPDATING CURRENT AND OTHER PLAYER PROPERTY

    for player_property in Cur_Mark:
        if Cards[player_property].color == "RED":
            color = RED
        elif Cards[player_property].color == "GREEN":
            color = GREEN
        elif Cards[player_property].color == "BLUE":
            color = BLUE
        elif Cards[player_property].color == "YELLOW":
            color = YELLOW
        elif Cards[player_property].color == "BLACK":
            color = BLACK
        elif Cards[player_property].color == "BROWN":
            color = BROWN
        elif Cards[player_property].color == "LIGHT_BLUE":
            color = LIGHT_BLUE
        elif Cards[player_property].color == "PINK":
            color = PINK
        elif Cards[player_property].color == "ORANGE":
            color = ORANGE
        else:
            color = WHITE

        pygame.draw.rect(screen,
                         color,
                         ((Send_Cards_Rects[player_property].left,
                          Send_Cards_Rects[player_property].top),
                          (INFO_CARD_WIDTH,
                           INFO_CARD_HEIGHT)))
        

    
    for player_property in Other_Mark:
        if Cards[player_property].color == "RED":
            color = RED
        elif Cards[player_property].color == "GREEN":
            color = GREEN
        elif Cards[player_property].color == "BLUE":
            color = BLUE
        elif Cards[player_property].color == "YELLOW":
            color = YELLOW
        elif Cards[player_property].color == "BLACK":
            color = BLACK
        elif Cards[player_property].color == "BROWN":
            color = BROWN
        elif Cards[player_property].color == "LIGHT_BLUE":
            color = LIGHT_BLUE
        elif Cards[player_property].color == "PINK":
            color = PINK
        elif Cards[player_property].color == "ORANGE":
            color = ORANGE
        else:
            color = WHITE

        pygame.draw.rect(screen,
                         color,
                         ((Receive_Cards_Rects[player_property].left,
                          Receive_Cards_Rects[player_property].top),
                          (INFO_CARD_WIDTH,
                           INFO_CARD_HEIGHT)))
        


    # send amount box

    pygame.draw.rect(screen,
                     BLACK,
                     ((405,500),
                     (70,25)))

    font = pygame.font.SysFont(CARD_TEXT_STYLE, 18)
    screen.blit(font.render('M ' + str(send_amount),True,WHITE),(410,505))


    # receive amount box

    pygame.draw.rect(screen,
                     BLACK,
                     ((525,500),
                     (70,25)))

    font = pygame.font.SysFont(CARD_TEXT_STYLE, 18)
    screen.blit(font.render('M ' + str(receive_amount),True,WHITE),(530,505))    
    
    

    # buttons
    
    pygame.draw.rect(screen,
                     BLUE,
                     ((300,545),
                      (100,OPTION_HEIGHT)))

    font = pygame.font.SysFont(CARD_TEXT_STYLE, 25)
    screen.blit(font.render('OFFER',True,WHITE),(310,550))


    pygame.draw.rect(screen,
                     RED,
                     ((650,545),
                      (100,OPTION_HEIGHT)))

    font = pygame.font.SysFont(CARD_TEXT_STYLE, 22)
    screen.blit(font.render('CANCEL',True,WHITE),(660,550))



    clock = pygame.time.Clock()

    start = False
    offer = False

    
    while not start:

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                start = True
            elif event.type == pygame.MOUSEBUTTONDOWN:
                
                mouse_pos = pygame.mouse.get_pos()

                x = mouse_pos[0]
                y = mouse_pos[1]

                # offer clicked
                
                if x >= 300 and x <= 400 and y >= 545 and y <= 545 + OPTION_HEIGHT:
                    offer = True
                    start = True

                # cancel clicked

                if x >= 650 and x <= 750 and y >= 545 and y <= 545 + OPTION_HEIGHT:
                    offer = False
                    start = True

                # property selected

                # send property

                if x >= 200 and x <= 475 and y >= 200 and y <= 475:
                    send_card = get_rect_pressed_index(mouse_pos,Send_Cards_Rects)

                    if send_card < len(Send_Cards_Rects):
                        send_prop.update([send_card])

                # receive property
                
                if x >= 525 and x <= 800 and y >= 200 and y <= 475:
                    receive_card = get_rect_pressed_index(mouse_pos,Receive_Cards_Rects)

                    if receive_card < len(Receive_Cards_Rects):
                        receive_prop.update([receive_card])



                # amount entered

                # send amount

                if x >= 405 and x <= 475 and y >= 500 and y <= 525:
                    amt_done = False
                    while not amt_done:
                        for evnt in pygame.event.get():
                            if evnt.type == KEYDOWN:
                                if evnt.unicode.isdigit and send_amount*10 + int(evnt.unicode) < Players[cur_player].cur_balance:
                                    send_amount = send_amount*10 + int(evnt.unicode)
                                elif evnt.key == K_BACKSPACE:
                                    if send_amount != 0:
                                        send_amount = (send_amount - (send_amount%10))//10
                                elif evnt.key == K_RETURN:
                                    if send_amount < Players[cur_player].cur_balance:
                                        amt_done = True


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

                            create_board(screen)

                            create_game_options(screen)
                            
                            for player in Players:
                                player.move_player(screen,player.cur_position)

                            create_player_info(screen,Players,Cards,cur_player)
                            
                        display_trade_window(screen,Players,Cards,cur_player,other_player,Cur_Mark,Other_Mark,send_amount,receive_amount,send_prop,receive_prop)

                        
                            
                # receive amount

                if x >= 525 and x <= 595 and y >= 500 and y <= 525:

                    amt_done = False

                    while not amt_done:
                        for evtn in pygame.event.get():
                            if evtn.type == KEYDOWN:
                                if evtn.unicode.isdigit and receive_amount*10 + int(evtn.unicode) < Players[other_player].cur_balance:
                                    receive_amount = receive_amount*10 + int(evtn.unicode)
                                elif evtn.key == K_BACKSPACE:
                                    if receive_amount != 0:
                                        receive_amount = (receive_amount - (receive_amount%10))//10
                                elif evtn.key == K_RETURN:
                                    if receive_amount < Players[other_player].cur_balance:
                                        amt_done = True

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

                            create_board(screen)

                            create_game_options(screen)
                            
                            for player in Players:
                                player.move_player(screen,player.cur_position)

                            create_player_info(screen,Players,Cards,cur_player)

                            
                        display_trade_window(screen,Players,Cards,cur_player,other_player,Cur_Mark,Other_Mark,send_amount,receive_amount,send_prop,receive_prop)
                
                    
        

        clock.tick(60)

        pygame.display.update()

    
    return offer,send_amount,send_prop,receive_amount,receive_prop





# display window to allow other player to confirm trade infomation

def display_trade_confirm_window(screen,Send_Cards,send_amount,Receive_Cards,receive_amount):


    pygame.gfxdraw.box(screen,
                       ((ACTION_SCREEN_LEFT,ACTION_SCREEN_TOP),
                        (ACTION_SCREEN_WIDTH,ACTION_SCREEN_HEIGHT)),TRANSPARENT)


    font = pygame.font.SysFont(CARD_TEXT_STYLE, 20)

    screen.blit(font.render('Trade',True,WHITE),(ACTION_SCREEN_LEFT + 20,ACTION_SCREEN_TOP + 10))
    y_start = ACTION_SCREEN_TOP + 30
    receive_worth = receive_amount
    
    for receive_card in Receive_Cards:
        screen.blit(font.render('' + str(receive_card.name),True,WHITE),(ACTION_SCREEN_LEFT + 20,y_start))
        if receive_card.status == 1:
            receive_worth += receive_card.cost
        elif receive_card.status == 2:
            receive_worth += receive_card.mortgage_value
        y_start += 20


    screen.blit(font.render('(Worth : ' + str(receive_worth) + ')',True,WHITE),(ACTION_SCREEN_LEFT + 20,y_start))
    y_start += 20


    screen.blit(font.render('For',True,WHITE),(ACTION_SCREEN_LEFT + 20,y_start))
    y_start += 20

    
    send_worth = send_amount
    
    for send_card in Send_Cards:
        screen.blit(font.render('' + str(send_card.name),True,WHITE),(ACTION_SCREEN_LEFT + 20,y_start))
        if send_card.status == 1:
            send_worth += send_card.cost
        elif send_card.status == 2:
            send_worth += send_card.mortgage_value
        y_start += 20

    screen.blit(font.render('(Worth : ' + str(send_worth) + ')',True,WHITE),(ACTION_SCREEN_LEFT + 20,y_start))


    pygame.draw.rect(screen,
                     BLUE,
                     ((ACTION_SCREEN_LEFT + OPTION_MARGIN,ACTION_SCREEN_TOP + ACTION_SCREEN_HEIGHT - OPTION_HEIGHT - OPTION_MARGIN),
                      (OPTION_WIDTH,OPTION_HEIGHT)))



    font = pygame.font.SysFont(CARD_TEXT_STYLE, 25)
    screen.blit(font.render('TRADE',True,WHITE),(ACTION_SCREEN_LEFT + OPTION_MARGIN + 10,ACTION_SCREEN_TOP + ACTION_SCREEN_HEIGHT - OPTION_HEIGHT - OPTION_MARGIN + 5))


    pygame.draw.rect(screen,
                     RED,
                     ((760 - OPTION_WIDTH - OPTION_MARGIN,550 - OPTION_HEIGHT - OPTION_MARGIN),
                      (OPTION_WIDTH,OPTION_HEIGHT)))

    font = pygame.font.SysFont(CARD_TEXT_STYLE, 25)
    screen.blit(font.render('CANCEL',True,WHITE),(ACTION_SCREEN_LEFT + ACTION_SCREEN_WIDTH - OPTION_WIDTH - OPTION_MARGIN + 10,ACTION_SCREEN_TOP + ACTION_SCREEN_HEIGHT - OPTION_HEIGHT - OPTION_MARGIN + 5))


    clock = pygame.time.Clock()

    start = False
    trade_prop = False

    while not start:
        
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                start = True
            elif event.type == pygame.MOUSEBUTTONDOWN:
                
                mouse_pos = pygame.mouse.get_pos()

                x = mouse_pos[0]
                y = mouse_pos[1]

                # unmortgage clicked

                if x >= ACTION_SCREEN_LEFT + OPTION_MARGIN and x <= ACTION_SCREEN_LEFT + OPTION_MARGIN + OPTION_WIDTH and y >= ACTION_SCREEN_TOP + ACTION_SCREEN_HEIGHT - OPTION_HEIGHT - OPTION_MARGIN and y <= ACTION_SCREEN_TOP + ACTION_SCREEN_HEIGHT - OPTION_MARGIN:
                    trade_prop = True
                    start = True
    
    
                # cancel clicked

                if x >= ACTION_SCREEN_LEFT + ACTION_SCREEN_WIDTH - OPTION_WIDTH - OPTION_MARGIN and x <= ACTION_SCREEN_LEFT + ACTION_SCREEN_WIDTH - OPTION_MARGIN  and y >= ACTION_SCREEN_TOP + ACTION_SCREEN_HEIGHT - OPTION_HEIGHT - OPTION_MARGIN and y <= ACTION_SCREEN_TOP + ACTION_SCREEN_HEIGHT - OPTION_MARGIN:
                    trade_prop = False
                    start = True

        

        clock.tick(60)

        pygame.display.update()

    
    return trade_prop

   

