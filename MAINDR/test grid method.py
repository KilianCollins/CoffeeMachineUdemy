import sys

import pygame
from pygame.locals import *
import numpy



pygame.init()

SW = 1000
SH = 500
screen = pygame.display.set_mode((SW, SH))
clock = pygame.time.Clock()
running = True
background_color = "black"

# grid

def drawGrid(w, rows, surface):
    sizeBtwn = w // rows  # Gives us the distance between the lines

    x = 0  # Keeps track of the current x
    y = 0  # Keeps track of the current y
    for l in range(rows):  # We will draw one vertical and one horizontal line each loop
        x = x + sizeBtwn
        y = y + sizeBtwn

        pygame.draw.line(surface, (255,255,255), (x,0),(x,w))
        pygame.draw.line(surface, (255,255,255), (0,y),(w,y))



while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if keys[pygame.K_ESCAPE]:
            running = False


        #
        # if keys[pygame.K_w]:
        #
        # if keys[pygame.K_s]:
        #







    # fill the screen with a color to wipe away anything from last frame
    screen.fill(background_color)



    # RENDER YOUR GAME HERE

    drawGrid(SW,20, screen)

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()



# make window