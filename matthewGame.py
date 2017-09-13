#!/usr/bin/
#By Matthew Q McDermott
#Thanks to Jess-

import pygame
import sys
import os
import pygame.freetype #load fonts
from pygame.locals import *

'''OBJECTS'''

def stats(score):
    #display text, 1, colour (rgb)
    text_score = myfont.render("Score: "+str(score), 1, (250,147,248))
    screen.blit(text_score, (4, 4))
    
class Platform(pygame.sprite.Sprite):
    #x location, y location, img width, img height, img file)
    def __init__(self, xloc, yloc, imgw, imgh, img):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([imgw, imgh])
        self.image.convert_alpha()
        self.image.set_colorkey(alpha)

        self.rect = self.image.get_rect()
        self.blockpic = pygame.image.load(img).convert()
        self.rect.y = yloc
        self.rect.x = xloc

        #paint image into blocks
        self.image.blit(self.blockpic, (0,0), (0,0,imgw,imgh))


    def level1():
        #create level 1
        platform_list = pygame.sprite.Group()
        block = Platform(0, 591, 768, 118,os.path.join('images','block0.png'))
        platform_list.add(block) #after each block

        return platform_list # at end of function level1

    def loot1():
        #create loot
        platform_list = pygame.sprite.Group()
        block = Platform(0, 591, 768, 118,os.path.join('images','Rainbow-300px.png'))
        platform_list.add(block) #after each block

        return platform_list # at end of function level1

    
    
class Player(pygame.sprite.Sprite):
    #spawn a player
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.momentumX = 0
        self.momentumY = 0

        #gravity varibles
        self.collide_delta = 0
        self.jump_delta = 6

        self.score = 0 #set score
        self.damage = 0 #player is hit
        self.images = [ ]
        img = pygame.image.load(os.path.join('images', 'hero.png')).convert()
        self.images.append(img)
        self.image = self.images[0]
        self.rect = self.image.get_rect()
        self.image.convert_alpha()
        self.image.set_colorkey(alpha)

    def control(self, x, y):
        #control player movement
        self.momentumX += x
        self.momentumY += y

    def update(self, enemy_list):
        #update sprite position
        currentX = self.rect.x
        nextX = currentX + self.momentumX
        self.rect.x = nextX

        currentY = self.rect.y
        nextY = currentY + self.momentumY
        self.rect.y = nextY

        #gravity
        if self.collide_delta < 6 and self.jump_delta < 6:
            self.jump_delta = 6*2
            self.momentumY -= 33 #how can you jump

            self.collide_delta +=6
            self.jump_delta += 6
        
        #collisions
        block_hit_list = pygame.sprite.spritecollide(self, platform_list, False)
        if self.momentumX > 0:
            for block in block_hit_list:
                self.rect.y = currentY
                self.rect.x = currentX+9
                self.collide_delta = 0 #stop jumping

        if self.momentumY > 0:
            for block in block_hit_list:
                self.rect.y = currentY
                self.momentumY = 0
                self.collide_delta = 0 #stop jumping
                
        enemy_hit_list = pygame.sprite.spritecollide(self, enemy_list, False)
        '''for enemy in enemy_hit_list:
            self.score -= 1
            print(self.score)'''
        if self.damage == 0:
            for enemy in enemy.hit_list:
                if not self.rect.contains(enemy):
                    self.damage = self.rect.colliderect(enemy)
                    print(self.score)

        if self.damage == 1:
            idx = self.rect.collidelist(enemy_hit_list)
            if idx == -1:
                self.damage - 0
                self.score -= 1

    def jump (self, platform_list):
        self.jump_delta = 0


    def gravity(self):
        self.momentumY += 3.2 #how fast player falls

        if self.rect.y > 960 and self.momentumY >= 0:
            self.momentumY = 0
            self.rect.y = screenY-20

class Enemy(pygame.sprite.Sprite):
    #spawn an enemy
    def __init__(self,x,y,img):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join('images', 'enemy.png'))
        self.image.convert_alpha()
        self.image.set_colorkey(alpha)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.counter = 0 #counter variable
        
    def move(self):
        #enemy movement
        if self.counter >= 0 and self.counter <= 30:
            self.rect.x += 2
        elif self.counter >= 30 and self.counter <= 60:
            self.rect.x -= 2
        else:
            self.counter = 0
            print('reset')

        self.counter += 1
    

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
pygame.font.init() #start free type

font_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "fonts", "amazdoom.tff")
font_size = 64
myfont = pygame.font.Font(font_path, font_size)

main = True
     
screen = pygame.display.set_mode([screenX, screenY])
backdrop = pygame.image.load(os.path.join('images', 'stage.png')).convert()
backdropRect = screen.get_rect()
platform_list = Platform.level1() #set stage for Level 1

player = Player() #Spawn player
player.rect.x = 0
player.rect.y = 0
movingsprites = pygame.sprite.Group()
movingsprites.add(player)
movesteps = 10 #how fast to move

forwardX = 600 #when to scroll
backwardX = 150 #when to scroll

#enemy code
enemy = Enemy(100,50, 'enemy.png')  #spawn an enemy
enemy_list = pygame.sprite.Group()  #create enemy group
enemy_list.add(enemy) #add enemy to group
                                          
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
                player.control(movesteps, 0)
            if event.key == pygame.K_RIGHT:
                print('right stop')
                player.control(-movesteps, 0)
            if event.key == pygame.K_UP:
                print('up stop')

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                print('left')
                player.control(-movesteps, 0)
            if event.key == pygame.K_RIGHT:
                print('right')
                player.control(movesteps, 0)
            if event.key == pygame.K_UP:
                print('jump')
                player.jump(platform_list)

    #scroll world forward
    if player.rect.x >= forwardX:
        scroll = min(1, (backwardX - player.rect.x))
        player.rect.x = backwardX
        for platform in platform_list:
            platform.rect.x += scroll
            
    #scroll world backword
    if player.rect.x <= forwardX:
        scroll = player.rect.x - forwardX
        player.rect.x = forwardX
        for platform in platform_list:
            platform.rect.x -= scroll
            
    screen.blit(backdrop, backdropRect)
    
    platform_list.draw(screen) #draw platforms on screen
    player.gravity()
    player.update(enemy_list) #update player position
    movingsprites.draw(screen) #draw player
    
    enemy_list.draw(screen) #refresh enemies
    enemy.move() #move enemy sprite

    stats(player.score)
    
    pygame.display.flip()
    clock.tick(fps)
