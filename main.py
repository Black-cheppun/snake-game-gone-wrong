import pygame.base
from pygame.locals import *

pygame.init()

class snake(pygame.sprite.Sprite):
    def __init__(self):
        super(snake,self).__init__()
        self.surface = pygame.Surface((25, 25))
        self.surface.fill((0,0,0))
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
            
            
    
        
    


    #player.update(pressedkeys)
    screen.blit(player.surface, (playerX,playerY))
    pygame.display.flip()

