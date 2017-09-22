
import pygame


class Ship(pygame.sprite.Sprite):
    def __init__(self, type, size, location, health, color):
        self.type = type
        self.size = size
        self.location = location
        self.health = health
        self.color = color
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.Surface((size, size))
        self.rect = self.image.get_rect()
        self.rect.center = location

    def update(self):
        self.image.fill(self.color)
