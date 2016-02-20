import pygame
import sys
from pygame.locals import *

from variables import *


# --------------CREATE GAME OPTIONS--------------
# creates the game play options(8) - roll dice, bulid, trade, sell, mortgage, unmortgage, rules, quit game
#GAME_OPTIONS_WIDTH = 1440 width = 130
#GAME_OPTIONS_HEIGHT = 120 y-coord = 810 height = 60

def create_game_options(screen):

    color = (255,69,0) #RED

    #   ROLL DICE
    pygame.draw.rect(screen,
                     color,
                     ((OPTION_MARGIN + OPTION_BOARD_SPACING,
                      BOARD_HEIGHT + OPTION_MARGIN - OPTION_BOARD_SPACING),
                      (OPTION_WIDTH,
                      OPTION_HEIGHT)))

    font = pygame.font.SysFont(CARD_TEXT_STYLE, 20)
    font.set_bold(True)
    screen.blit(font.render('ROLL DICE', True, WHITE), (50, 800))



    #   BUILD
    pygame.draw.rect(screen,
                     color,
                     (((OPTION_MARGIN + OPTION_WIDTH) * 1 + OPTION_MARGIN + OPTION_BOARD_SPACING,
                      BOARD_HEIGHT + OPTION_MARGIN - OPTION_BOARD_SPACING),
                      (OPTION_WIDTH,
                      OPTION_HEIGHT)))

    font = pygame.font.SysFont(CARD_TEXT_STYLE, 20)
    font.set_bold(True)
    screen.blit(font.render('BUILD', True, WHITE), (230, 800))



    #   TRADE
    pygame.draw.rect(screen,
                     color,
                     (((OPTION_MARGIN + OPTION_WIDTH) * 2 + OPTION_MARGIN + OPTION_BOARD_SPACING,
                      BOARD_HEIGHT + OPTION_MARGIN - OPTION_BOARD_SPACING),
                      (OPTION_WIDTH,
                      OPTION_HEIGHT)))

    font = pygame.font.SysFont(CARD_TEXT_STYLE, 20)
    font.set_bold(True)
    screen.blit(font.render('TRADE', True, WHITE), (390, 800))


    #   SELL
    pygame.draw.rect(screen,
                     color,
                     (((OPTION_MARGIN + OPTION_WIDTH) * 3 + OPTION_MARGIN + OPTION_BOARD_SPACING,
                      BOARD_HEIGHT + OPTION_MARGIN - OPTION_BOARD_SPACING),
                      (OPTION_WIDTH,
                      OPTION_HEIGHT)))

    font = pygame.font.SysFont(CARD_TEXT_STYLE, 20)
    font.set_bold(True)
    screen.blit(font.render('SELL', True, WHITE), (560, 800))



    #   MORTGAGE
    pygame.draw.rect(screen,
                     color,
                     (((OPTION_MARGIN + OPTION_WIDTH) * 4 + OPTION_MARGIN + OPTION_BOARD_SPACING,
                      BOARD_HEIGHT + OPTION_MARGIN - OPTION_BOARD_SPACING),
                      (OPTION_WIDTH,
                      OPTION_HEIGHT)))

    font = pygame.font.SysFont(CARD_TEXT_STYLE, 20)
    font.set_bold(True)
    screen.blit(font.render('MORTGAGE', True, WHITE), (685, 800))



    #   UNMORTGAGE
    pygame.draw.rect(screen,
                     color,
                     (((OPTION_MARGIN + OPTION_WIDTH) * 5 + OPTION_MARGIN + OPTION_BOARD_SPACING,
                      BOARD_HEIGHT + OPTION_MARGIN - OPTION_BOARD_SPACING),
                      (OPTION_WIDTH,
                      OPTION_HEIGHT)))

    font = pygame.font.SysFont(CARD_TEXT_STYLE, 15)
    font.set_bold(True)
    screen.blit(font.render('UNMORTGAGE', True, WHITE), (845, 800))



    #   RULES
    pygame.draw.rect(screen,
                     color,
                     (((OPTION_MARGIN + OPTION_WIDTH) * 6 + OPTION_MARGIN * 5 + OPTION_BOARD_SPACING,
                      BOARD_HEIGHT + OPTION_MARGIN - OPTION_BOARD_SPACING),
                      (OPTION_WIDTH,
                      OPTION_HEIGHT)))

    font = pygame.font.SysFont(CARD_TEXT_STYLE, 20)
    font.set_bold(True)
    screen.blit(font.render('RULES(?)', True, WHITE), (1140, 800))



    #   QUIT GAME
    pygame.draw.rect(screen,
                     color,
                     (((OPTION_MARGIN + OPTION_WIDTH) * 7 + OPTION_MARGIN * 5 + OPTION_BOARD_SPACING,
                      BOARD_HEIGHT + OPTION_MARGIN - OPTION_BOARD_SPACING),
                      (OPTION_WIDTH,
                      OPTION_HEIGHT)))

    font = pygame.font.SysFont(CARD_TEXT_STYLE, 18)
    font.set_bold(True)
    screen.blit(font.render('QUIT GAME', True, WHITE), (1290, 800))


