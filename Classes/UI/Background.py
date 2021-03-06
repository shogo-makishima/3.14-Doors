import pygame
from Classes.Settings import *


class Background(pygame.sprite.Sprite):
    def __init__(self, typeWorld=None, image_file="BackgroundWinter", location=(0, 0)):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(UI_SPRITES[image_file])
        if (typeWorld): self.image = pygame.image.load(LEVEL_GENERATOR_SPRITES[typeWorld]["Background"])

        self.image = pygame.transform.scale(self.image, (WIN_WIDTH, WIN_HEIGHT))
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location
