
import pygame
import objects
from objects import *
from Constants import *

class Game:
    def __init__(self):
        pygame.init()
        pygame.mixer.init()

        self.clock = pygame.time.set_timer
        self.screen = pygame.display.set_mode([WIN_WIDTH, WIN_HEIGHT])
        pygame.display.set_caption('Platformer Game')
        self.background_image = pygame.image.load("backgraund.jpg")
        self.all_sprite_list = pygame.sprite.Group()

        self.platform_list = pygame.sprite.Group()
        self.create_platforms()

        self.artifact_list = pygame.sprite.Group()
        self.create_artifacts()

        self.player = objects.Player (0, 0)
        self.player.platforms = self.platform_list
        self.player.artifact = self.artifact_list
        self.all_sprite_list.add(self.player)

    def new_method(self):
        self.clock = pygame.time.clock( )

    def create_platforms(self):
        platform_coords = [
                     [200, 450],
                     [200, 500],
                     [200, 550],
                     [300, 500],
                     [300, 550],
                     [400, 450],
                     [450, 450],
                     [550, 350],
                     [600, 350],
                     [700, 300],
                     [750, 300],
                     [850, 250],
                     [900, 250],
                     [850, 250],
                     [900, 250],
                     [850, 250],
                     [900, 550],
                     [950, 450],
                     [1100, 500],
                     [1100, 550],
                     [1150, 400],
                     [1150, 450],
                     [1150, 500],
                     [1150, 550],
                     [1300, 400],
                     [1400, 400],
                     [1500, 400],
                                   ]
        for coord in platform_coords:
            platform = object.platform(coord[0], coord[1])
            self.platform_list.add(platform)
            self.all_sprite_list.add(platform)

    def create_artifact(self):
        artifact_coords = [
                     [200, 250],
                     [200, 300],
                     [200, 350],
                     [200, 400],
                     [450, 400],
                     [600, 200],
                     [600, 300],
                     [600, 550],
                     [600, 350],
                     [750, 550],
                     [750, 250],
                     [750, 150],
                     [900, 50],
                     [900, 100],
                     [900, 150],
                     [900, 200],
                     [1150, 300],
                     [1300, 200],
                     [1300, 250],
                     [1400, 200],
                     [1400, 250],
                     [1500, 200],
                     [1500, 250],
                           ]
        for coord in artifact_coords:
                    platform = objects.artifact(coord[0], coord[1])
                    self.artifacts_list.add(objects.artifact)
                    self.all_sprite_list.add(objects.artifact)
        def run(self):
            done = False

            self.screen.blit(self.background_image, (0,0))
            self.all_sprite_list.draw(self.screen)


            while not done:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        done = True
                pygame.display.update()
                pygame.display.flip()
                self.clock.tick(FPS)

            pygame.quit()

game = Game()

game.run()

