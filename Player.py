#include pygame again, because this is a different file
import pygame
import sys



class Player(object):
    #Classes have 2 parts: attri and methods
    def __init__(self, screen):
        self.image = pygame.image.load('./images/Hero.png')
        #resize the image...
        self.image = pygame.transform.scale(self.image, (207,250))
        self.x = 100
        self.y = 100
        self.screen = screen

    #define some methods
    def draw_me(self):
        self.screen.blit(self.image, [self.x, self.y])
