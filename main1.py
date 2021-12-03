import pygame.base
from pygame.locals import *
import random

pygame.init()
colors = (0,0,0)

class snake(pygame.sprite.Sprite):
    def __init__(self):
        super(snake,self).__init__()
        self.surface = pygame.Surface((25, 25))
        #self.surface.fill(colors)
        #self.rec = self.surface.get_rect()
    
    """def update(self, pressedkeys):
        if pressedkeys[K_UP]:
            self.rec.move_ip(0,-1)
        if pressedkeys[K_DOWN]:
            self.rec.move_ip(0,1)
        if pressedkeys[K_LEFT]:
            self.rec.move_ip(-1,0)
        if pressedkeys[K_RIGHT]:
            self.rec.move_ip(1, 0)
        
        if self.rec.left <0:
            self.rec.left = 0
        if self.rec.right >screen_width:
            self.rec.right = screen_width
        if self.rec.top <0:
            self.rec.top = 0
        if self.rec.bottom > screen_height:
            self.rec.bottom = screen_height"""
                

player = snake()
playerX = 280
playerY = 380
speed = 0.0009
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width,screen_height))
screen.fill((170,170,170))

running = True
while running:
    
    
    # check if user asked to exit
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
                
                
    if playerX <0:
        playerX = 0
    if playerX >screen_width -25:
        playerX = screen_width -25
    if playerY <0:
        playerY = 0
    if playerY > screen_height -25:
        playerY = screen_height -25
        
    
    player.surface.fill(colors)
        
    pressedkeys = pygame.key.get_pressed()                
    
    for key in pressedkeys:
        if pressedkeys[K_UP]:
            playerY -= speed
        if pressedkeys[K_DOWN]:
            playerY+= speed
        
        if pressedkeys[K_LEFT]:
            playerX -= speed
        if pressedkeys[K_RIGHT]:
            playerX+= speed
            
        if pressedkeys[K_SPACE]:
            color1 = random.randint(0,255)
            color2 = random.randint(0,255)
            color3 = random.randint(0,255)
            colors = (color1,color2,color3)
            
            
            
            
    
        
    


    #player.update(pressedkeys)
    screen.blit(player.surface, (playerX,playerY))
    pygame.display.flip()

