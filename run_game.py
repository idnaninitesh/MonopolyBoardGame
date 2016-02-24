# Next task : create screen for various play options


import pygame
import sys
from pygame.locals import *

from variables import *
from ask_for_game_details import *
from create_board import *
from create_game_options import *
from create_player_info import *
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

    create_board(screen,player_colors)

    # rolls dice and places them at random position with 4 and 2 number in 1st and 2nd die respectively
    roll_dice(screen,4,2)           # Since 42 is the answer to everything :)

    Cards,Cards_Rects = create_card_rects()

    print(len(Cards_Rects))

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

    print(len(Option_Rects))

    # create player info

    # stores the index of player whose turn it is now
    
    cur_player = 1;

   
    create_player_info(screen,Players,Cards,cur_player)

    Info_Cards_Rects = create_info_rects()

    print(len(Info_Cards_Rects))
    
    

    done = False

    clock = pygame.time.Clock()


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
                print(mouse_pos)
                #col = pos[0] // (CARD_WIDTH + CARD_MARGIN)
                #row = pos[1] // (CARD_HEIGHT + CARD_MARGIN)

                # handle inputs

                #rect_index = get_rect_pressed(mouse_pos)

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


"""

----------------PYGAME FLOW-------------------

import pygame

def main():
    #Set up the game and run the main game loop
    pygame.init()      # Prepare the pygame module for use
    surface_sz = 480   # Desired physical surface size, in pixels.

    # Create surface of (width, height), and its window.
    main_surface = pygame.display.set_mode((surface_sz, surface_sz))

    # Set up some data to describe a small rectangle and its color
    small_rect = (300, 200, 150, 90)
    some_color = (255, 0, 0)        # A color is a mix of (Red, Green, Blue)

    while True:
        ev = pygame.event.poll()    # Look for any event
        if ev.type == pygame.QUIT:  # Window close button clicked?
            break                   #   ... leave game loop

        # Update your game objects and data structures here...

        # We draw everything from scratch on each frame.
        # So first fill everything with the background color
        main_surface.fill((0, 200, 255))

        # Overpaint a smaller rectangle on the main surface
        main_surface.fill(some_color, small_rect)

        # Now the surface is ready, tell pygame to display it!
        pygame.display.flip()

    pygame.quit()     # Once we leave the loop, close the window.

main()

"""
