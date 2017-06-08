#!/usr/bin/
#By Matthew Q McDermott
#Thanks to Jess-

import pygame
import sys
import os
from pygame.locals import *

'''OBJECTS'''
class Player(pygame.sprite.Sprite):
    #spawn a player
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.images = [ ]
        images = pygame.image.load(os.path.join('images', 'hero.png')).convert()


'''SETUP COLOURS'''
BLACK = (0, 0, 0)

'''SETUP'''
screenX = 960 #width
screenY = 720 #height

fps = 40
afps = 4
clock = pygame.time.Clock()
pygame.init()

main = True

screen = pygame.display.set_mode([screenX, screenY])
backdrop = pygame.image.load(os.path.join('images', 'Backgrond#1.png')).convert()
backdropRect = screen.get_rect()

player = Player() #Spawn player
player.rect.x = 0
player.rect.y = 0
movingsprites = pygame.sprite.Group()
movingsprites.add(player)
                                          
'''MAIN LOOP'''
'''
while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYUP:
            if event.key == ord('q'):
                pygame.quit()
                sys.exit()
                main == False
'''
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    screen.fill(BLACK)
