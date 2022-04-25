
import pygame
import objects
from objects import *
from Constants import *
pygame.init()

class Game:
    def __init__(Self):
        pygame.init()
        pygame.mixer.init()

        Self.clock = pygame.time.set_timer
        Self.screen = pygame.display.set_mode([WIN_WIDTH, WIN_HEIGHT])
        pygame.display.set_caption('Platformer Game')
        Self.background_image = pygame.image.load("backgraund.jpg")
        Self.all_sprite_list = pygame.sprite.Group()

        Self.platform_list = pygame.sprite.Group()
        Self.create_platforms()

        Self.artifact_list = pygame.sprite.Group()
        Self.create_artifacts()

        Self.player = objects.Player (0, 0)
        Self.player.platforms = Self.platform_list
        Self.player.artifact = Self.artifact_list
        Self.all_sprite_list.add(Self.player)

    def new_method(Self):
        Self.clock = pygame.time.clock( )


    def create_platforms(Self):
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
            Self.platform_list.add(platform)
            Self.all_sprite_list.add(platform)

    def create_artifact(Self):
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
                    Self.artifacts_list.add(objects.artifact)
                    Self.all_sprite_list.add(objects.artifact)
        def run(self):
            done = False

            Self.screen.blit(Self.background_image, (0,0))
            Self.all_sprite_list.draw(Self.screen)


            while not done:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        done = True
                pygame.display.update()
                pygame.display.flip()
                Self.clock.tick(FPS)

            pygame.quit()

game = Game()

game.run()

