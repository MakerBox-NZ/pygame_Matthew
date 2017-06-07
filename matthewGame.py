#C:/Python361/0myprogs/RATA/matthewGame.py
#!/usr/bin/
#By Matthew Q McDermott
#Thanks to Jess-

import pygame
import sys
import os
from pygame.locals import *

'''OBJECTS'''



'''SETUP COLOURS'''
BLACK = (0, 0, 0)

'''SETUP'''
screenX = 960 #width
screenY = 720 #height

fps = 40
afps = 4
clock = pygame.time.Clock()
pygame.init()
screen = pygame.display.set_mode([screenX, screenY])

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
