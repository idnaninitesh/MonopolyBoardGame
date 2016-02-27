import pygame
import sys
from pygame.locals import *


from variables import *


# get the section in which the mouse was pressed i.e board,game options or info cards

def get_rect_pressed_type(mouse_pos,Cards_Rects,Option_Rects,Info_Cards_Rects):

    x = mouse_pos[0]
    y = mouse_pos[1]

    Rects = None

    # match x and y against the boundaries of each card list
    
    if x >= Option_Rects[0].x and x <= (Option_Rects[-1].x + Option_Rects[-1].width):
        if y >= Option_Rects[0].y and y <= (Option_Rects[0].y + Option_Rects[0].height):
            Rects = Option_Rects

    if x >= Cards_Rects[20].x and x <= (Cards_Rects[30].x + Cards_Rects[30].width):
        if y >= Cards_Rects[20].y and y <= (Cards_Rects[10].y + Cards_Rects[10].height):
            Rects = Cards_Rects

    if x >= Info_Cards_Rects[19].x and x <= (Info_Cards_Rects[31].x + Info_Cards_Rects[31].width):
        if y >= Info_Cards_Rects[21].y and y <= (Info_Cards_Rects[9].y + Info_Cards_Rects[9].height):
            Rects = Info_Cards_Rects
    
    return Rects


# get the index of rect within the set of Rectangles in which the mouse was presssed

def get_rect_pressed_index(mouse_pos,Rects):

    index = 0

    x = mouse_pos[0]
    y = mouse_pos[1]
    
    for rect in Rects:
        if rect != None:
            if rect.collidepoint(x,y):
                break
        index = index + 1
        

    return index
    
