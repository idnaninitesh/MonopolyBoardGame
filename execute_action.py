import pygame
import sys
from pygame.locals import *

from variables import *
from create_board import *
from create_game_options import *
from create_player_info import *
from handle_mouse_event import *
from Player import *


def execute_action(screen,Rects,rect_index,Players,Cards,cur_player,Cards_Rects,Option_Rects,Info_Cards_Rects,isRunning):
    
    
    # a board card was clicked

    if len(Rects) == 40:
        if rect_index != 40:
            if Rects[0] == None:
                print("Info card : " + str(rect_index))
            else:
                print("Board card : " + str(rect_index))

    # a game action was clicked

    if len(Rects) == 8 and rect_index != 8:
        
        # roll dice
        if rect_index == 0:
            

            # adding all the static items
            
            screen.fill(BACKGROUND_COLOR)

            create_board(screen)

            create_game_options(screen)

            create_player_info(screen,Players,Cards,cur_player)

            # rolling dice
            
            steps = roll_dice(screen)
 
            player = Players[cur_player]

            initial_card = get_rect_pressed_index(player.cur_position,Cards_Rects)
            final_card = (initial_card + steps)%40

            # moving the current players piece
            
            final_pos = Cards[final_card].board_pos
            next_position = ()

            if player.color == "BLUE":
                next_position = (final_pos[0] + 19,final_pos[1] + 19)
            elif player.color == "RED":
                next_position = (final_pos[0] + 59,final_pos[1] + 19)
            elif player.color == "GREEN":
                next_position = (final_pos[0] + 19,final_pos[1] + 49)
            elif player.color == "YELLOW":
                next_position = (final_pos[0] + 59,final_pos[1] + 49)
            else:
                next_position = ()


            player.move_player(screen,next_position)

            # updating the position of all players' piece on the board
            
            for player in Players:
                player.move_player(screen,player.cur_position)


            # add the necessary actions to be taken due to dice roll
            # update_game_dice()
                
            # unlocking the game loop and updating the player turn

            isRunning = False
            cur_player = (cur_player+1)%len(Players)

            return cur_player,isRunning

        elif rect_index == 1:
            print("1;)")
            # build house/hotel
        elif rect_index == 2:
            print("2;)")
            # trade
        elif rect_index == 3:
            print("3;)")
            # sell
        elif rect_index == 4:
            print("4;)")
            # mortgage
        elif rect_index == 5:
            print("5;)")
            # unmortgage
        elif rect_index == 6:
            print("6;)")
            # rules
        elif rect_index == 7:
            pygame.quit()
            #print("7;)")
            # quit game
            

        

        
        
