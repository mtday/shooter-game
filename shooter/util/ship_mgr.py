
import pygame


class ShipMgr:
    def __init__(self):
        self.ships = pygame.sprite.Group()

    def draw(self, surface):
        self.ships.update()
        self.ships.draw(surface)

    def add_ship(self, ship):
        self.ships.add(ship)
