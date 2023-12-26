import pygame
import pygame.image
import numpy

food = pygame.image.load('frot.png')
def fd (screen, wid, hid):
    x=[]
    y=[]
    x.extend([wid])
    y.extend([hid])

    for i in range(len(x)):

        screen.blit(food, (x[i], y[i]))



def ranx (wid):
    x= []
    for i in range(10):
        x.extend([numpy.random.randint(0, wid - 30)])
    return x

def rany (hid):
    y= []
    for i in range(10):
        y.extend([numpy.random.randint(0, hid - 30)])
    return y
