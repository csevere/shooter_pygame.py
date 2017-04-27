import pygame
import sys

#doesn't need to be a class
def check_events():
    #the excape hatch (from while)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            #the user clicked the red x, get ot of the loop
            sys.exit()
