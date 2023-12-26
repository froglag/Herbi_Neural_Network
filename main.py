import pygame
from pygame.locals import *
from pygame.display import Info
import  numpy as np
import herbivores as herb
import food

pygame.init()
wid=pygame.display.Info().current_w
hid=pygame.display.Info().current_h
screen= pygame.display.set_mode((wid, hid), pygame.FULLSCREEN)
clock= pygame.time.Clock()
pygame.display.set_caption('BORD')

def game_loop():
# starting variables
    x_change= 0
    y_change= 0
    x= wid/2
    y= hid/2
    i=700
    lifetime=0
    time=0.0
    running = True
# running loop
    while running:
# movement of character
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
            x_change= herb.movex(event, x_change)
            y_change= herb.movey(event, y_change)
            x_change= herb.upx(event, x_change)
            y_change= herb.upy(event, y_change)
# scene color, position of character and drawing character by using function
        screen.fill((90, 90, 90))
        x += x_change
        y += y_change
        herb.char(screen,x,y)
# frame of scene
        if x < 0 or x > wid - 40:
            running = False
        if y < 0 or y > hid - 40:
            running = False
# food creating
        if i==700:
            i-=700
            ranx= food.ranx(wid)
            rany= food.rany(hid)
        for j in range(len(ranx)):
            food.fd(screen, ranx[j], rany[j])
        i += 1
# food eating
        for j in range(len(ranx)):
            if x <= ranx[j] + 25 and x >= ranx[j] - 25 and y <= rany[j] + 25 and y >= rany[j] - 25:
                del(ranx[j], rany[j])
                lifetime-=35
                ranx.extend([np.random.randint(0, wid - 30)])
                rany.extend([np.random.randint(0, hid - 30)])
# lifetime
        if lifetime >= 350:
            running=False
        lifetime+=1

        print(time)
        time+=0.1
        pygame.display.update()
        clock.tick(60)

game_loop()
pygame.quit()
