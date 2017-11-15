
import os
import pygame

from shooter.config.dirs import DIR_IMAGES_SHIPS
from shooter.config.settings import FONT_NAME_DEFAULT
from shooter.config.settings import FONT_SIZE_DEFAULT
from shooter.config.colors import GREEN


class Ship(pygame.sprite.Sprite):
    def __init__(self, ship_type, size, location, health, direction=0):
        self.ship_type = ship_type
        self.size = size
        self.location = location
        self.health = health
        self.direction = direction
        self.selected = False
        pygame.sprite.Sprite.__init__(self)

        self.images = self.get_images()
        self.image = pygame.Surface((self.size, self.size + FONT_SIZE_DEFAULT))
        self.rect = self.image.get_rect()
        font = pygame.font.SysFont(FONT_NAME_DEFAULT, FONT_SIZE_DEFAULT)
        self.ship_label = font.render(self.ship_type, True, GREEN)

    def get_current_image(self):
        if self.selected:
            return self.images['selected']
        return self.images['normal']

    @staticmethod
    def get_image(file_name):
        return pygame.image.load(os.path.join(DIR_IMAGES_SHIPS, file_name)).convert()

    def get_images(self):
        images = {
            'normal':   self.get_image(self.ship_type + '.png'),
            'selected': self.get_image(self.ship_type + '.selected.png')
        }
        return images

    def update(self):
        current_image = self.get_current_image()
        scale = self.size / current_image.get_width()
        ship_image = pygame.transform.rotozoom(current_image, self.direction, scale)

        self.image.blit(ship_image, (0, FONT_SIZE_DEFAULT))
        self.image.blit(self.ship_label, ((self.size / 2) - (self.ship_label.get_width() / 2), 0))
        self.rect = self.image.get_rect()
        self.rect.center = self.location

