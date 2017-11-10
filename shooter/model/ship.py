
import os
import pygame

from shooter.config.dirs import DIR_IMAGES_SHIPS
from shooter.config.settings import FONT_NAME_DEFAULT
from shooter.config.settings import FONT_SIZE_DEFAULT
from shooter.config.colors import GREEN
from shooter.config.colors import BLUE


class Ship(pygame.sprite.Sprite):
    def __init__(self, ship_type, size, location, health, image_file_name, direction=0):
        self.ship_type = ship_type
        self.size = size
        self.location = location
        self.health = health
        self.direction = direction
        self.selected = False
        pygame.sprite.Sprite.__init__(self)

        self.original_image = pygame.image.load(os.path.join(DIR_IMAGES_SHIPS, image_file_name)).convert()
        self.image = pygame.Surface((self.size, self.size + FONT_SIZE_DEFAULT))
        self.rect = self.image.get_rect()
        font = pygame.font.SysFont(FONT_NAME_DEFAULT, FONT_SIZE_DEFAULT)
        self.ship_label = font.render(self.ship_type, True, GREEN)

    def update(self):
        scale = self.size / self.original_image.get_width()
        ship_image = pygame.transform.rotozoom(self.original_image, self.direction, scale)

        self.image.blit(ship_image, (0, FONT_SIZE_DEFAULT))
        self.image.blit(self.ship_label, ((self.size / 2) - (self.ship_label.get_width() / 2), 0))
        if self.selected:
            selected_circle_line_width = 1
            pygame.draw.circle(self.image, BLUE, (self.size // 2, (self.size + FONT_SIZE_DEFAULT) // 2),
                               self.size // 2 + 5, selected_circle_line_width)
        self.rect = self.image.get_rect()
        self.rect.center = self.location

