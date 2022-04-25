from tkinter import Image
from numpy import imag
import pygame
from Constants import *

class Player(pygame.sprite.Sprite):


    def __init__(self, x, y, img = ' img.png '):
        super().__init__()

    pygame.display.set_mode((1,1), pygame.NOFRAME)
    image = pygame.image.load(image).convert_alpha()
    image = image.convert_alpha()
 
    self.rect = self.image.get_rect()
    self.rect.y = y
    self.rect.x = x

    self.change_x = 0
    self.change_y = 0
    self.score = 0
    self.lives = 9

    self.platforms = pygame.sprite.Group()
    self.artifacts = pygame.sprite.Group()

    def update(self):

        self.calc_grav()

        self.rect.x += self.change_x

        block_hit_list = pygame.sprite.spritecollide(self,self.platforms, False)

        for block in block_hit_list:

            if self.change_x > 0:
                self.rect.right = block.rect.left

            elif self.change_x < 0:
                self.rect.left = block.rect.right

     
            self.rect.y += self.change_y

            block_hit_list = pygame.sprite.spritecollide(self, self.platforms, False)

            for block in block_hit_list:
         
                if self.change_y > 0:
                    self.rect.right.bottom = block.rect.top
               
                elif self.change_y < 0:
                    self.rect.top = block.rect.bottom


                self.change_y = 0


            artifact_hit_list = pygame.sprite.spritecollide (self, self.artifacts, False )

            for artifact in artifact_hit_list:
                self.score += 1
                artifact.kill()


    def calc_grav(self):
        if self.change_y == 0:
            self.change_y = 1
        else:

            self.change_y += 0.3

        if self.rect.y >= WIN_HEIGHT - self.rect.height and self.change_y >= 0:
            self.change_y = 0

        if self.rect.x < 0:
            self.rect.x = 0
            self.change_x = 0


    def jamp(self):
  
        self.rect.y += 2
        platform_hit_list = pygame.sprite.spritecollide(self, self.platforms, False)
        self.rect.y -= 2


        if len(platform_hit_list) > 0 or self.rect.bottom >= WIN_HEIGHT:
            self.change_y = -11

    def go_left(self):

        self.change_x = -5

    def go_right(self):

        self.change_x = 5

    def stop(self):

        self.change_x = 0

class Platform(pygame.sprinte.Sprite):
    images = ['platform_1.png', 'platform_2.png', 'platform_3.png']

    def __init__(self, x, y, type):
        super().__init__()

        self.image = pygame.image.load(platform.images[1]).convert_alpha()

        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x

class Artifact(pygame.sprinte.Sprite):
    def __init__(self, x, y, img = 'dux.png'):
        super().__init__()

        self.image = pygame.image.load(img).convert_alpha()


        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x