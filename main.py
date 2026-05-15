import pygame
import sys
import random
import time
from pygame.locals import *

pygame.init()

FPS = pygame.time.Clock()
FPS.tick(60)

Red = (255, 0, 0)
Green = (0, 255, 0)
Blue = (0, 0, 255)
Black = (0, 0, 0)
White = (255, 255, 255)

Screen_Width = 400
Screen_Height = 600
SPEED = 2
SCORE = 0

font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, Black)
 
background = pygame.image.load("road.png")
background = pygame.transform.scale_by(background, .37)


DISPLAYSURF = pygame.display.set_mode((Screen_Width, Screen_Height))
DISPLAYSURF.fill(White)
pygame.display.set_caption("Game")

class Enemy(pygame.sprite.Sprite):
      def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("red_car.png")
        self.image = pygame.transform.scale_by(self.image, .4)
        self.rect = self.image.get_bounding_rect()
        self.rect.center=(random.randint(40,Screen_Width - 40),0) 
      def move(self):
        global SCORE
        self.rect.move_ip(0,SPEED)
        if (self.rect.top > 600):
            SCORE += 1
            self.rect.top = 0
            self.rect.center = (random.randint(30, 370), 0)
 
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("blue_car.png")
        self.image = pygame.transform.scale_by(self.image, .5)
        self.rect = self.image.get_bounding_rect()
        self.rect.center = (160, 520)
    def move(self):
        pressed_keys = pygame.key.get_pressed()
        if self.rect.left > 0:
              if pressed_keys[K_LEFT]:
                  self.rect.move_ip(-5, 0)
        if self.rect.right < Screen_Width:        
              if pressed_keys[K_RIGHT]:
                  self.rect.move_ip(5, 0)
       
P1 = Player()
E1 = Enemy()

enemies = pygame.sprite.Group()
enemies.add(E1)
all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)
 
## variable for time passed to make speed exponential
INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 2000)

while True:
    for event in pygame.event.get():
        if event.type == INC_SPEED:
              SPEED += 0.5
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    DISPLAYSURF.blit(background, (0,0))
    scores = font_small.render(str(SCORE), True, Black)
    DISPLAYSURF.blit(scores, (10,10))
     
    for entity in all_sprites:
        DISPLAYSURF.blit(entity.image, entity.rect)
        entity.move()
 
    if pygame.sprite.spritecollideany(P1, enemies):
        time.sleep(0.5)
        DISPLAYSURF.fill(Red)
        DISPLAYSURF.blit(game_over, (30,250))
        pygame.display.update()

        for entity in all_sprites:
            entity.kill() 
        time.sleep(2)
        pygame.quit()
        sys.exit()
         
    pygame.display.update()
    FPS.tick(60)