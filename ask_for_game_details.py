import pygame
import sys
from pygame.locals import *

from variables import *

def get_player_name(screen,index,list_names):
    screen.fill(BLACK)

    name = ""
    
    name_done = False

    
    while not name_done:
        for evt in pygame.event.get():
            if evt.type == KEYDOWN:
                if evt.unicode.isalpha():
                    name += evt.unicode
                elif evt.key == K_BACKSPACE:
                    name = name[:-1]
                elif evt.key == K_RETURN:
                    print(name)
                    if name.isalpha() and len(name) <= 10 and not name in list_names:
                        name_done = True
            elif evt.type == QUIT:
                pygame.quit()


        screen.fill((0,0,0))
        font = pygame.font.SysFont(CARD_TEXT_STYLE, 30)
        screen.blit(font.render('Enter name of player {0}'.format(index+1), True, WHITE),(100,100))
        screen.blit(font.render(name, True, WHITE), (100,200))
        screen.blit(font.render('Press ENTER To Continue ', True, WHITE),(600,800))
        pygame.display.flip()

    return name

    


def get_player_color(screen,index,list_color,player_names):
    screen.fill(BLACK)

    color = ""
    
    color_done = False

    
    while not color_done:
        for evt in pygame.event.get():
            if evt.type == KEYDOWN:
                if evt.unicode.isalpha():
                    color += evt.unicode
                elif evt.key == K_BACKSPACE:
                    color = color[:-1]
                elif evt.key == K_RETURN:
                    print(color)
                    if color.isalpha() and color.upper() in list_color:
                        color_done = True
            elif evt.type == QUIT:
                pygame.quit()


        screen.fill((0,0,0))
        font = pygame.font.SysFont(CARD_TEXT_STYLE, 30)
        screen.blit(font.render('Select color for {0}'.format(player_names[index]), True, WHITE),(100,100))
        screen.blit(font.render('Colors Available : [%s]' % (','.join(list_color)), True, WHITE),(100,140))
        screen.blit(font.render(color, True, WHITE), (100,200))
        screen.blit(font.render('Press ENTER To Continue ', True, WHITE),(600,800))
        pygame.display.flip()

    return color
    


    

def ask_for_player_details(screen,no_of_players):
    screen.fill(BLACK)

    no_of_players = int(no_of_players)

    player_names = []
    player_colors = []
    list_color = ['RED','GREEN','BLUE','YELLOW']
    name = ""
    color = ""

    for i in range(0,no_of_players):
        name = get_player_name(screen,i,player_names)

        player_names.append(name)
        
        color = get_player_color(screen,i,list_color,player_names)

        color = color.upper()
        player_colors.append(color)
        
        list_color.remove(player_colors[i])
        
    return (no_of_players,player_names,player_colors)
    

def ask_for_game_details(screen):

    no_of_players = "0"

    no_done = False
    
    while not no_done:
        for evt in pygame.event.get():
            if evt.type == KEYDOWN:
                if evt.unicode.isdigit() and evt.unicode>="2" and evt.unicode<="4":
                    no_of_players = evt.unicode
                elif evt.key == K_BACKSPACE:
                    no_of_players = "0"
                elif evt.key == K_RETURN:
                    print(no_of_players)
                    if no_of_players >= "2" and no_of_players <= "4":
                        no_done = True
            elif evt.type == QUIT:
                pygame.quit()


        screen.fill((0,0,0))
        font = pygame.font.SysFont(CARD_TEXT_STYLE, 30)
        screen.blit(font.render('Enter no of players (2 - 4)', True, WHITE),(100,100))
        screen.blit(font.render(no_of_players, True, WHITE), (100,200))
        screen.blit(font.render('Press ENTER To Continue ', True, WHITE),(600,800))
        pygame.display.flip()

    no_of_players,player_names,player_colors = ask_for_player_details(screen,no_of_players)    
    return (no_of_players,player_names,player_colors)

