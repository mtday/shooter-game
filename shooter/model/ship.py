
import os
import pygame

from shooter.config.dirs import DIR_IMAGES_SHIPS


class Ship(pygame.sprite.Sprite):
    def __init__(self, ship_type, size, location, health, image_file_name, direction=0):
        self.ship_type = ship_type
        self.size = size
        self.location = location
        self.health = health
        self.direction = direction
        pygame.sprite.Sprite.__init__(self)
        self.original_image = pygame.image.load(os.path.join(DIR_IMAGES_SHIPS, image_file_name)).convert()
        self.image = self.original_image
        self.rect = self.image.get_rect()

    def update(self):
        scale = self.size / self.original_image.get_width()
        self.image = pygame.transform.rotozoom(self.original_image, self.direction, scale)
        self.rect = self.image.get_rect()
        self.rect.center = self.location
