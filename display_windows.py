
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
                                start = True



        clock.tick(60)

        pygame.display.update()


    
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
        screen.blit(font.render(' pass Go, collect $200',True,WHITE),(ACTION_SCREEN_LEFT + 20,280))
    elif card == 5:
        screen.blit(font.render('Bank pays you dividend of $50',True,WHITE),(ACTION_SCREEN_LEFT + 20,ACTION_SCREEN_TOP + 30))
    elif card == 6:
        screen.blit(font.render('Get out of Jail free – this card may be ',True,WHITE),(ACTION_SCREEN_LEFT + 20,ACTION_SCREEN_TOP + 30))
        screen.blit(font.render(' kept until needed, or traded/sold',True,WHITE),(ACTION_SCREEN_LEFT + 20,280))
    elif card == 7:
        screen.blit(font.render('Go back 3 spaces ',True,WHITE),(ACTION_SCREEN_LEFT + 20,ACTION_SCREEN_TOP + 30))
    elif card == 8:
        screen.blit(font.render('Go directly to Jail – do not pass Go, ',True,WHITE),(ACTION_SCREEN_LEFT + 20,ACTION_SCREEN_TOP + 30))
        screen.blit(font.render(' do not collect $200',True,WHITE),(ACTION_SCREEN_LEFT + 20,280))
    elif card == 9:
        screen.blit(font.render('Make general repairs on all your property – ',True,WHITE),(ACTION_SCREEN_LEFT + 20,ACTION_SCREEN_TOP + 30))
        screen.blit(font.render('for each house pay $25 – for each hotel $100 ',True,WHITE),(ACTION_SCREEN_LEFT + 20,280))
    elif card == 10:
        screen.blit(font.render('Pay poor tax of $15',True,WHITE),(ACTION_SCREEN_LEFT + 20,ACTION_SCREEN_TOP + 30))
    elif card == 11:
        screen.blit(font.render('Take a trip to Reading Railroad – if',True,WHITE),(ACTION_SCREEN_LEFT + 20,ACTION_SCREEN_TOP + 30))
        screen.blit(font.render('you pass Go collect $200 ',True,WHITE),(ACTION_SCREEN_LEFT + 20,ACTION_SCREEN_TOP + 30))
    elif card == 12:
        screen.blit(font.render('Take a walk on the Boardwalk – ',True,WHITE),(ACTION_SCREEN_LEFT + 20,ACTION_SCREEN_TOP + 30))
        screen.blit(font.render('advance token to Boardwalk',True,WHITE),(ACTION_SCREEN_LEFT + 20,280))
    elif card == 13:
        screen.blit(font.render('You have been elected chairman ',True,WHITE),(ACTION_SCREEN_LEFT + 20,ACTION_SCREEN_TOP + 30))
        screen.blit(font.render('of the board – pay each player $50',True,WHITE),(ACTION_SCREEN_LEFT + 20,280))
    elif card == 14:
        screen.blit(font.render('Your building loan matures – collect $150',True,WHITE),(ACTION_SCREEN_LEFT + 20,ACTION_SCREEN_TOP + 30))
    elif card == 15:
        screen.blit(font.render('You have won a crossword competition',True,WHITE),(ACTION_SCREEN_LEFT + 20,ACTION_SCREEN_TOP + 30))
        screen.blit(font.render(' - collect $100',True,WHITE),(ACTION_SCREEN_LEFT + 20,ACTION_SCREEN_TOP + 30))


    pygame.display.update()
    pygame.time.delay(ACTION_SCREEN_DELAY)



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
        screen.blit(font.render(' collect $75',True,WHITE),(ACTION_SCREEN_LEFT + 20,280))
    elif card == 3:
        screen.blit(font.render('Doctor\'s fee - Pay $50',True,WHITE),(ACTION_SCREEN_LEFT + 20,ACTION_SCREEN_TOP + 30))
    elif card == 4:
        screen.blit(font.render('Get out of Jail free – this card may be ',True,WHITE),(ACTION_SCREEN_LEFT + 20,ACTION_SCREEN_TOP + 30))
        screen.blit(font.render(' kept until needed, or traded/sold',True,WHITE),(ACTION_SCREEN_LEFT + 20,280))
    elif card == 5:
        screen.blit(font.render('Go directly to Jail – do not pass Go, ',True,WHITE),(ACTION_SCREEN_LEFT + 20,ACTION_SCREEN_TOP + 30))
        screen.blit(font.render(' do not collect $200',True,WHITE),(ACTION_SCREEN_LEFT + 20,280))
    elif card == 6:
        screen.blit(font.render('It is your birthday Collect ',True,WHITE),(ACTION_SCREEN_LEFT + 20,ACTION_SCREEN_TOP + 30))
        screen.blit(font.render(' $10 from each player',True,WHITE),(ACTION_SCREEN_LEFT + 20,280))
    elif card == 7:
        screen.blit(font.render('Grand Opera Night - collect $50 ',True,WHITE),(ACTION_SCREEN_LEFT + 20,ACTION_SCREEN_TOP + 30))
        screen.blit(font.render(' for opening night seats',True,WHITE),(ACTION_SCREEN_LEFT + 20,280))
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
        screen.blit(font.render('$40 per house, $115 per hotel',True,WHITE),(ACTION_SCREEN_LEFT + 20,280))
    elif card == 14:
        screen.blit(font.render('Your have won second prize in a beauty ',True,WHITE),(ACTION_SCREEN_LEFT + 20,ACTION_SCREEN_TOP + 30))
        screen.blit(font.render(' contest – collect $10',True,WHITE),(ACTION_SCREEN_LEFT + 20,280))
    elif card == 15:
        screen.blit(font.render('You inherit $100',True,WHITE),(ACTION_SCREEN_LEFT + 20,ACTION_SCREEN_TOP + 30))
    elif card == 16:
        screen.blit(font.render('From sale of stock you get $50',True,WHITE),(ACTION_SCREEN_LEFT + 20,ACTION_SCREEN_TOP + 30))
    elif card == 17:
        screen.blit(font.render('Holiday Fund matures - Receive $100',True,WHITE),(ACTION_SCREEN_LEFT + 20,ACTION_SCREEN_TOP + 30))
                    


    pygame.display.update()
    pygame.time.delay(ACTION_SCREEN_DELAY)



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


# display window to inform passing go

def display_pass_go_window(screen):
                    
    pygame.gfxdraw.box(screen,
                       ((ACTION_SCREEN_LEFT,ACTION_SCREEN_TOP),
                        (ACTION_SCREEN_WIDTH,ACTION_SCREEN_HEIGHT)),TRANSPARENT)

    font = pygame.font.SysFont(CARD_TEXT_STYLE, 25)
    screen.blit(font.render('PASSED GO COLLECT $200',True,WHITE),(ACTION_SCREEN_LEFT + 20,ACTION_SCREEN_TOP + 60))

    pygame.display.update()
    pygame.time.delay(ACTION_SCREEN_DELAY)




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


