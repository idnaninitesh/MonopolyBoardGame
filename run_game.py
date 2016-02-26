import pygame
import pygame.gfxdraw
import sys
from pygame.locals import *

from variables import *
from ask_for_game_details import *
from create_board import *
from create_game_options import *
from create_player_info import *
from handle_mouse_event import *
from handle_game import *
from Player import *
from Card import *


# -------------------MAIN GAME FUNTION---------------
def run_game():

    pygame.init()

    WINDOW_SIZE = [SCREEN_WIDTH,SCREEN_HEIGHT]
    screen = pygame.display.set_mode(WINDOW_SIZE)

    screen.fill(BACKGROUND_COLOR)

    pygame.display.set_caption("MONOPOLY")


    # ask for game details

    no_of_players,player_names,player_colors = ask_for_game_details(screen)
    

   # handle game details


    # creating the players
    
    Players = []

    for i in range(0,no_of_players):
        Players.append(Player(player_names[i],player_colors[i],1000))


    # create initial board

    create_board(screen)

    # rolls dice and places them at random position with 4 and 2 number in 1st and 2nd die respectively
    roll_dice(screen,4,2)           # Since 42 is the answer to everything :)

    Cards,Cards_Rects = create_card_rects()

    # placing the game pieces at the start position for each player

    for player in Players:
        
        if player.color == "BLUE":
            next_position = (1020,720)
        elif player.color == "RED":
            next_position = (1060,720)
        elif player.color == "GREEN":
            next_position = (1020,750)
        elif player.color == "YELLOW":
            next_position = (1060,750)
        else:
            next_position = ()


        player.move_player(screen,next_position)

    # create game options

    create_game_options(screen)

    Option_Rects = create_option_rects()


    # create player info

    # stores the index of player whose turn it is now
    
    cur_player = 0;

   
    create_player_info(screen,Players,Cards,cur_player)

    Info_Cards_Rects = create_info_rects()

        

    pygame.event.clear()

    
    # START GAME PROMPT

    pygame.gfxdraw.box(screen,
                       ((320,210),
                        (440,340)),(202,202,225,127))

    font = pygame.font.SysFont(CARD_TEXT_STYLE, 30)
    screen.blit(font.render('START GAME',True,BLACK),(450,270))

    pygame.draw.rect(screen,
                     BLUE,
                     ((320 + OPTION_MARGIN,550 - OPTION_HEIGHT - OPTION_MARGIN),
                      (OPTION_WIDTH,OPTION_HEIGHT)))

    font = pygame.font.SysFont(CARD_TEXT_STYLE, 30)
    screen.blit(font.render('START',True,WHITE),(370,485))


    pygame.draw.rect(screen,
                     RED,
                     ((760 - OPTION_WIDTH - OPTION_MARGIN,550 - OPTION_HEIGHT - OPTION_MARGIN),
                      (OPTION_WIDTH,OPTION_HEIGHT)))

    font = pygame.font.SysFont(CARD_TEXT_STYLE, 30)
    screen.blit(font.render('QUIT',True,WHITE),(630,485))


    clock = pygame.time.Clock()

    done = False
    start = False

    # Start Prompt

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

                if x >= 360 and x <= 490 and y >= 480 and y <= 520:
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

                if x >= 600 and x <= 730 and y >= 480 and y <= 520:
                    done = True
                    start = True

        

        clock.tick(60)

        pygame.display.update()

    

    clock = pygame.time.Clock()

    isRunning = False


    #--------------MAIN GAME LOOP------------------
    while not done:
        
        for event in pygame.event.get():
            
            """
                check_inputs()    #get key/mouse input inputs for this frame
                handle_inputs()    #handle each input that has occurred during this frame
                update_gamestate()    #update the state on the game (who's turn, etc)
                update_display()    #update pygame window graphics (draw stuff, flip display)

            """                

            if event.type == pygame.QUIT:
                done = True
            elif event.type == pygame.MOUSEBUTTONDOWN:

                # check inputs
                
                mouse_pos = pygame.mouse.get_pos()

                # handle inputs

                Rects = get_rect_pressed_type(mouse_pos,Cards_Rects,Option_Rects,Info_Cards_Rects)
                rect_index = get_rect_pressed_index(mouse_pos,Rects)

                # take necessary action based on the event that occured in the game
                # kind of semaphore I think ;)
                
                if isRunning == False:
                    isRunning = True
                    cur_player,isRunning = handle_game(screen,Rects,rect_index,Players,Cards,cur_player,Cards_Rects,Option_Rects,Info_Cards_Rects,isRunning)

                # update the state of the game after every turn
                # 1. Current Player
                # 2. Property of each player
                # 3. Balance of each player
                # 4. Position
                # 5. Other Player Attributes
                # 6. Status of each card
                # 7. Houses and hotels details associated with each card
                

        ####

        

        clock.tick(60)

        pygame.display.update()


    pygame.quit()




"""
------------------MONOPOLY FLOW----------------


# This is intentionally simplified pseudocode, but at the bottom-most level most
#    simple games have a similar structure to this.

#Construct your game objects
players = [Player(args) for n in range(num_players)]
cards = loadCards()   #or however you load your cards (files,database,etc)
board = Board()

#initialize your display context
pygame_screen.init()  #or whatever is the correct syntax for Pygame

# Main game loop
while 1:
    check_inputs()    #get key/mouse input inputs for this frame
    handle_inputs()    #handle each input that has occurred during this frame
    update_gamestate()    #update the state on the game (who's turn, etc)
    update_display()    #update pygame window graphics (draw stuff, flip display)

cleanup()
"""

