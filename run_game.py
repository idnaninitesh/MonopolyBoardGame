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

    # creating the cards

    Cards = []

    # id_no,name,color,cost,rent,mortgage_value,house_cost,hotel_cost,house_rent,hotel_rent,board_pos,info_pos

    card = Card(0,"GO","",0,0,0,0,0,[],0,(1001,701),())
    Cards.append(card)
    
    card = Card(1,"MEDITARREANEAN AVENUE","BROWN",60,2,30,50,50,[10,30,90,160],250,(901,701),(1380,350))
    Cards.append(card)
    
    card = Card(2,"COMMUNITY CHEST","",0,0,0,0,0,[],0,(801,701),())
    Cards.append(card)

    card = Card(3,"BALTIC AVENUE","BROWN",80,4,30,50,50,[20,60,80,320],450,(701,701),(1330,350))
    Cards.append(card)

    card = Card(4,"INCOME TAX","",0,0,0,0,0,[],0,(601,701),())
    Cards.append(card)

    card = Card(5,"READING RAILROAD","BLACK",200,25,100,0,0,[],0,(501,701),(1280,350))
    Cards.append(card)

    card = Card(6,"ORIENTAL AVENUE","LIGHT_BLUE",100,6,50,50,50,[30,90,270,400],450,(401,701),(1255,350))
    Cards.append(card)
   
    card = Card(7,"CHANCE","",0,0,0,0,0,[],0,(301,701),())
    Cards.append(card)
   
    card = Card(8,"VERMONT AVENUE","LIGHT_BLUE",100,6,50,50,50,[30,90,270,400],450,(201,701),(1205,350))
    Cards.append(card)

    card = Card(9,"CONNECTICUT AVENUE","LIGHT_BLUE",120,8,60,50,50,[40,100,300,450],600,(101,701),(1180,350))
    Cards.append(card)

    card = Card(10,"IN JAIL","",0,0,0,0,0,[],0,(1,701),())
    Cards.append(card)

    card = Card(11,"ST. CHARLES PLACE","PINK",140,10,70,100,100,[50,150,450,625],750,(1,631),(1155,325))
    Cards.append(card)

    card = Card(12,"ELECTIC COMPANY","WHITE",150,10,75,0,0,[],0,(1,561),(1155,300))
    Cards.append(card)

    card = Card(13,"STATES AVENUE","PINK",140,10,70,100,100,[50,150,450,625],750,(1,491),(1155,275))
    Cards.append(card)

    card = Card(14,"VIRGINIA AVENUE","PINK",160,12,80,100,100,[60,180,500,700],900,(1,421),(1155,250))
    Cards.append(card)

    card = Card(15,"PENNSYLVANIA RAILROAD","BLACK",200,25,100,0,0,[],0,(1,351),(1155,225))
    Cards.append(card)

    card = Card(16,"ST. JAMES PLACE","ORANGE",180,14,90,100,100,[70,200,550,750],950,(1,281),(1155,200))
    Cards.append(card)

    card = Card(17,"COMMUNITY CHEST","",0,0,0,0,0,[],0,(1,211),())
    Cards.append(card)

    card = Card(18,"TENNESSEE AVENUE","ORANGE",180,14,90,100,100,[70,200,550,750],950,(1,141),(1155,150))
    Cards.append(card)

    card = Card(19,"NEW YORK AVENUE","ORANGE",200,16,100,100,100,[80,220,600,800],1000,(1,71),(1155,125))
    Cards.append(card)

    card = Card(20,"FREE PARKING","",0,0,0,0,0,[],0,(1,1),())
    Cards.append(card)

    card = Card(21,"KENTUCKY AVENUE","RED",220,18,110,150,150,[90,250,700,875],1050,(101,1),(1180,100))
    Cards.append(card)

    card = Card(22,"CHANCE","",0,0,0,0,0,[],0,(201,1),())
    Cards.append(card)

    card = Card(23,"INDIANA AVENUE","RED",220,18,110,150,150,[90,250,700,875],1050,(301,1),(1230,100))
    Cards.append(card)

    card = Card(24,"ILLINOIS AVENUE","RED",240,20,120,150,150,[100,300,750,925],1100,(401,1),(1255,100))
    Cards.append(card)

    card = Card(25,"B. & O. RAILROAD","BLACK",200,25,100,0,0,[],0,(501,1),(1280,100))
    Cards.append(card)

    card = Card(26,"ATLANTIC AVENUE","YELLOW",260,22,130,150,150,[110,330,800,975],1150,(601,1),(1305,100))
    Cards.append(card)

    card = Card(27,"VENTORA AVENUE","YELLOW",260,22,130,150,150,[110,330,800,975],1150,(701,1),(1330,100))
    Cards.append(card)

    card = Card(28,"WATER WORKS","WHITE",150,10,75,0,0,[],0,(801,1),(1355,100))
    Cards.append(card)

    card = Card(29,"MARVIN GARDENS","YELLOW",280,24,140,150,150,[120,360,850,1025],1200,(901,1),(1380,100))
    Cards.append(card)

    card = Card(30,"GO TO JAIL","",0,0,0,0,0,[],0,(1001,1),())
    Cards.append(card)

    card = Card(31,"PACIFIC AVENUE","GREEN",300,26,150,200,200,[130,390,900,1100],1275,(1001,71),(1405,125))
    Cards.append(card)

    card = Card(32,"CAROLINA AVENUE","GREEN",300,26,150,200,200,[130,390,900,1100],1275,(1001,141),(1405,150))
    Cards.append(card)

    card = Card(33,"COMMUNITY CHEST","",0,0,0,0,0,[],0,(1001,211),())
    Cards.append(card)

    card = Card(34,"PENNSYLVANIA AVENUE","GREEN",320,28,160,200,200,[150,450,1000,1200],1400,(1001,281),(1405,200))
    Cards.append(card)

    card = Card(35,"SHORT LANE","BLACK",200,25,100,0,0,[],0,(1001,351),(1405,225))
    Cards.append(card)

    card = Card(36,"CHANCE","",0,0,0,0,0,[],0,(1001,421),())
    Cards.append(card)
 
    card = Card(37,"PARK PLACE","BLUE",350,35,175,200,200,[175,500,1100,1300],1500,(1001,491),(1405,275))
    Cards.append(card)

    card = Card(38,"LUXURY TAX","",0,0,0,0,0,[],0,(1001,561),())
    Cards.append(card)

    card = Card(39,"BROADWALK","BLUE",400,50,200,200,200,[200,600,1400,1700],2000,(1001,631),(1405,325))
    Cards.append(card)




    # create initial board

    create_board(screen,player_colors)

    pygame.draw.line(screen, WHITE, (0,BOARD_HEIGHT + OPTION_BOARD_SPACING/2), (SCREEN_WIDTH,BOARD_HEIGHT + OPTION_BOARD_SPACING/2))
        
    pygame.draw.line(screen, WHITE, (BOARD_WIDTH + INFO_BOARD_SPACING/2,0), (BOARD_WIDTH + INFO_BOARD_SPACING/2,BOARD_HEIGHT + OPTION_BOARD_SPACING/2))


    # create game options

    create_game_options(screen)
    

    # create player info

    create_player_info(screen,Players,Cards)
    

    
    done = False

    clock = pygame.time.Clock()


    #--------------MAIN GAME LOOP------------------
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            elif event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                print(pos)
                #col = pos[0] // (CARD_WIDTH + CARD_MARGIN)
                #row = pos[1] // (CARD_HEIGHT + CARD_MARGIN)
                

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

