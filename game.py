import pygame
from Player import Player
#get the sys module to exit the program
import sys
from Game_functions import check_events

#The core game funcitonality/loop

def run_game():
    #Init all the pygame stuff
    pygame.init()
    #set up a tuple for the screen size, (horiz, vert)
    screen_size = (1000, 800)
    #Set up a tuple for the bg color
    background_color = (82, 111, 53)

    #Create a pygame screen to use
    screen = pygame.display.set_mode(screen_size) #object.object.method()
    #Set a caption on the terminal window
    pygame.display.set_caption("A heroic 3rd person shooter")

    #Main game loop. Run forever...(or until break)

    the_player = Player(screen)
    #creat object class object, pass screen

    while 1:

        screen.fill(background_color)
        check_events()

        #draw the player
        the_player.draw_me()
        
        #clear the screen for the next itme through the loop
        pygame.display.flip()

#Start the game
run_game()
