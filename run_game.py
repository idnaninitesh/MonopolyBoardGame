import pygame
import sys
from pygame.locals import *

from variables import *
from ask_for_game_details import *
from create_board import *
from create_game_options import *
from create_player_info import *


# -------------------MAIN GAME FUNTION---------------
def run_game():

    pygame.init()

    WINDOW_SIZE = [SCREEN_WIDTH,SCREEN_HEIGHT]
    screen = pygame.display.set_mode(WINDOW_SIZE)

    screen.fill(BACKGROUND_COLOR)

    pygame.display.set_caption("MONOPOLY")


    # ask for game details

    ask_for_game_details(screen)
    

    # handle game details

    # store no of players, their color and name


    # create initial board

    create_board(screen)

    pygame.draw.line(screen, WHITE, (0,BOARD_HEIGHT + OPTION_BOARD_SPACING/2), (SCREEN_WIDTH,BOARD_HEIGHT + OPTION_BOARD_SPACING/2))
        
    pygame.draw.line(screen, WHITE, (BOARD_WIDTH + INFO_BOARD_SPACING/2,0), (BOARD_WIDTH + INFO_BOARD_SPACING/2,BOARD_HEIGHT + OPTION_BOARD_SPACING/2))


    # create game options

    create_game_options(screen)
    

    # create player info

    create_player_info(screen)
    

    
    done = False

    clock = pygame.time.Clock()


    #--------------MAIN GAME LOOP------------------
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            elif event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                #col = pos[0] // (CARD_WIDTH + CARD_MARGIN)
                #row = pos[1] // (CARD_HEIGHT + CARD_MARGIN)
                


        # check for any play option clicked

        #check_play_option(pos)

        
        # execute logic based on the button selected
        # change the state and display after the code is executed

        

        clock.tick(60)

        pygame.display.update()


    pygame.quit()

 
