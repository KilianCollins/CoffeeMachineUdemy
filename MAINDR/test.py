import sys

import pygame
from pygame.locals import *
import numpy



pygame.init()

SW = 1280
SH = 720
screen = pygame.display.set_mode((SW, SH))
clock = pygame.time.Clock()
running = True
background_color = "black"

#
#
# class Ball:
#     def __init__(self):
#         # should start in the center of the screen
#         self.x_pos = SW/2
#         self.y_pos = SH/2
#         #draw the ball
# #         move the ball
#
#
# class Paddle:
#     def __init__(self):
#         super()
#         self.x_pos = SW / 3
#         self.y_pos = SH / 2
#
#
#
#     def move(self,y:int=0) -> int:
#         if y <0:
#             self.y_pos =- 30
#             return (self.y_pos)
#         if y > 0:
#             self.y_pos += 30
#             return (self.y_pos)
#
#
# paddle_LEFT = Paddle()
left = 30
top = 30
width =30
height = 30
while running:
    keys = pygame.key.get_pressed()



    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if keys[pygame.K_ESCAPE]:
            running = False




        if keys[pygame.K_w]:
            if height >= 650:
                height = height
                top = top
            else:
                height += 30
                


        if keys[pygame.K_s]:
            if height < 0:
                height = height
                top = top

            else:
                height -= 30
                # top +=30









    # fill the screen with a color to wipe away anything from last frame
    screen.fill(background_color)
    pygame.draw.rect(screen, "white", pygame.Rect(left, top, width, height))


    # RENDER YOUR GAME HERE

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()



# make window