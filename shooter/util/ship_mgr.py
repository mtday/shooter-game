
import pygame


class ShipMgr:
    def __init__(self):
        self.ships = pygame.sprite.Group()

    def draw(self, surface):
        self.ships.update()
        self.ships.draw(surface)

    def add_ship(self, ship):
        self.ships.add(ship)

    def handle_events(self, events):
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                ship_selection_changed = False
                for ship in self.ships.sprites():
                    if ship.rect.collidepoint(event.pos):
                        ship.selected = not ship.selected
                        ship_selection_changed = True
                if not ship_selection_changed:
                    for ship in self.ships.sprites():
                        if ship.selected:
                            ship.selected = False
                            if not ship.has_moved:
                                ship.move(event.pos)
