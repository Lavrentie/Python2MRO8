import pygame
from Constants import *

pygame.init()

class Player(pygame.sprite):

    def __init__(Self, x, y, img = 'prhv32'):
        super().__init__()
    Self.image = pygame.image.load('img').convert_alpha()

    Self.rect = Self.image.get_rect()
    Self.rect.y = Y
    Self.rect.x = X

    Self.change_x = 0
    Self.change_y = 0
    Self.score = 0
    Self.lives = 9

    Self.platforms = pygame.sprite.Group()
    Self.artifacts = pygame.sprite.Group()

    def update(Self):

        Self.calc_grav()

        Self.rect.x += Self.change_x

        block_hit_list = pygame.sprite.spritecollide(Self,Self.platforms, False)

        for block in block_hit_list:

            if Self.change_x > 0:
                Self.rect.right = block.rect.left

            elif Self.change_x < 0:
                Self.rect.left = block.rect.right

        # Движение вверх - вниз
            Self.rect.y += Self.change_y

            block_hit_list = pygame.sprite.spritecollide(Self, Self.platforms, False)

            for block in block_hit_list:

                if Self.change_y > 0:
                    Self.rect.right.bottom = block.rect.top
 
                elif Self.change_y < 0:
                    Self.rect.top = block.rect.bottom

  
                Self.change_y = 0

            artifact_hit_list = pygame.sprite.spritecollide (Self, Self.artifacts, False )

            for artifact in artifact_hit_list:
                Self.score += 1
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

        self.image = pygame.image.load(platform.images[0]).convert_alpha()


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