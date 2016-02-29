
import pygame
import pygame.gfxdraw
import sys
from pygame.locals import *

from Player import *
from Card import *
from ask_for_game_details import *
from create_board import *
from create_game_options import *
from create_player_info import *
from handle_mouse_event import *
from handle_game import *


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


    """
        Test Build Feature
    """

    Players[cur_player].property_owned.append(1)
    Players[cur_player].property_owned.append(3)
    Cards[1].status = 1
    Cards[3].status = 1
    Players[cur_player].color_cards_owned.append(BROWN_CARDS)

    """
    """

    create_player_info(screen,Players,Cards,cur_player)

    Info_Cards_Rects = create_info_rects()

        
    # START GAME PROMPT

    done = display_start_game_window(screen,Players,Cards,cur_player)

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
                if Rects != None:

                    # rects is option,info or board
                    
                    rect_index = get_rect_pressed_index(mouse_pos,Rects)

                    # take necessary action based on the event that occured in the game
                    # kind of semaphore I think ;)

                    if Rects == Option_Rects and rect_index < len(Rects):

                        # rect is among the Rects
                        
                        if isRunning == False:
                            isRunning = True
                            cur_player,isRunning = handle_game(screen,Rects,rect_index,Players,Cards,cur_player,Cards_Rects,Option_Rects,Info_Cards_Rects,isRunning)
                


        

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

