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
        img = pygame.image.load(os.path.join('images', 'hero.png')).convert()
        self.images.append(img)
        self.image = self.images[0]
        self.rect = self.image.get_rect()
        

'''SETUP COLOURS'''
BLACK = (0, 0, 0)

'''SETUP'''
screenX = 960 #width
screenY = 720 #height

alpha = (0, 0, 0)
black = (1, 1, 1)
white = (255, 255, 255)

fps = 40
afps = 4
clock = pygame.time.Clock()
pygame.init()

main = True

screen = pygame.display.set_mode([screenX, screenY])
backdrop = pygame.image.load(os.path.join('images', 'stage.png')).convert()
backdropRect = screen.get_rect()

player = Player() #Spawn player
player.rect.x = 0
player.rect.y = 0
movingsprites = pygame.sprite.Group()
movingsprites.add(player)
                                          
'''MAIN LOOP'''

while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYUP:
            if event.key == ord('q'):
                pygame.quit()
                sys.exit()
                main == False

            if event.key == pygame.K_LEFT:
                print('left stop')
            if event.key == pygamw.K_RIGHT:
                print('right stop')
            if event.key == pygame.K_UP:
                print('up stop')

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                print('left')
            if event.key == pygame.K_RIGHT:
                print('right')
            if event.key == pygame.K_UP:
                print('up')
            
    screen.blit(backdrop, backdropRect)
    movingsprites.draw(screen) #draw player
    pygame.display.flip()
    clock.ticks(fps)
