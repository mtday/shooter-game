
import math
import os
import pygame

from shooter.config.dirs import DIR_IMAGES_SHIPS
from shooter.config.settings import FONT_NAME_DEFAULT
from shooter.config.settings import FONT_SIZE_DEFAULT
from shooter.config.colors import GREEN


class Ship(pygame.sprite.Sprite):
    def __init__(self, ship_type, size, location, health, direction=0, max_speed=5, acceleration=0.05, turn_speed=0.5):
        self.ship_type = ship_type
        self.size = size
        self.location = location
        self.destination = None
        self.health = health
        self.direction = direction
        self.current_speed = 0
        self.max_speed = max_speed
        self.acceleration = acceleration
        self.turn_speed = turn_speed
        self.selected = False
        self.has_moved = False
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

    def move(self, position):
        self.destination = position
        self.has_moved = True

    def update_direction(self):
        (x1, y1) = self.location
        (x2, y2) = self.destination

        # desired_direction_radians = ((math.pi / 2) + math.atan2(y2 - y1, x2 - x1)) - (math.pi / 2)
        desired_direction_radians = math.atan2(y2 - y1, x2 - x1)
        desired_direction_degrees = desired_direction_radians * 180 / math.pi
        direction_delta = math.fabs(self.direction - desired_direction_degrees)

        if direction_delta < self.turn_speed:
            self.direction = desired_direction_degrees
        elif desired_direction_degrees > self.direction:
            self.direction += self.turn_speed
        else:
            self.direction -= self.turn_speed
        return direction_delta < 10

    def update_speed(self):
        if self.current_speed < self.max_speed:
            self.current_speed += self.acceleration
            if self.current_speed > self.max_speed:
                self.current_speed = self.max_speed

    def update_location(self):
        if self.destination is not None and self.update_direction():
            self.update_speed()

            (x1, y1) = self.location
            (x2, y2) = self.destination
            distance = math.sqrt(((x2 - x1) * (x2 - x1)) + ((y2 - y1) * (y2 - y1)))

            if distance < self.current_speed:
                self.location = self.destination
            else:
                direction_radians = (self.direction * math.pi / 180)
                x_delta = self.current_speed * math.cos(direction_radians)
                y_delta = self.current_speed * math.sin(direction_radians)
                self.location = (x1 + x_delta, y1 + y_delta)

            if self.location == self.destination:
                self.destination = None

    def update(self):
        self.update_location()

        current_image = self.get_current_image()
        scale = self.size / current_image.get_width()
        ship_image = pygame.transform.rotozoom(current_image, self.direction, scale)
        # print(ship_image.get_width(), ship_image.get_height())

        if self.image.get_width() != ship_image.get_width() or self.image.get_height() != ship_image.get_height():
            self.image = pygame.Surface((ship_image.get_width(), ship_image.get_height() + FONT_SIZE_DEFAULT))

        self.image.blit(ship_image, (0, FONT_SIZE_DEFAULT))
        self.image.blit(self.ship_label, ((self.size / 2) - (self.ship_label.get_width() / 2), 0))
        self.rect = self.image.get_rect()
        self.rect.center = self.location

