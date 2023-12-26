import pygame.image
import pygame
from pygame.locals import *

herbi= pygame.image.load('herbi.png')

def char (screen,x,y):

    screen.blit(herbi, (x,y))

def movex (event, x_change):

        if event.type == KEYDOWN:
            if event.key == K_LEFT:
                x_change = -5
                return x_change
            if event.key == K_RIGHT:
                x_change = 5
                return x_change
        return x_change


def movey (event, y_change):
        if event.type == KEYDOWN:
            if event.key == K_UP:
                y_change = -5
                return y_change
            if event.key == K_DOWN:
                y_change = 5
                return y_change
        return y_change


def upx (event, x_change):
    if event.type == KEYUP:
        if event.key == K_LEFT or event.key == K_RIGHT:
            x_change = 0
            return x_change
    return x_change

def upy (event, y_change):
    if event.type == KEYUP:
        if event.key == K_UP or event.key == K_DOWN:
            y_change = 0
            return y_change
    return y_change