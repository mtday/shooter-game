import pygame

from shooter.config.settings import FPS_TARGET
from shooter.model.scout import Scout
from shooter.model.attack import Attack
from shooter.ui.window import Window
from shooter.util.ship_mgr import ShipMgr


class Game:
    def __init__(self):
        pygame.init()
        pygame.mixer.init()
        self.window = Window(self)
        self.clock = pygame.time.Clock()
        self.running = False
        self.ship_mgr = ShipMgr()
        self.ship_mgr.add_ship(Scout(location=(100, 300)))
        self.ship_mgr.add_ship(Scout(location=(250, 150)))
        self.ship_mgr.add_ship(Attack(location=(500, 200)))
        self.ship_mgr.add_ship(Attack(location=(700, 500)))

        attack_ship = Attack(location=(200, 500))
        attack_ship.selected = True
        self.ship_mgr.add_ship(attack_ship)

    def handle_events(self):
        events = pygame.event.get()
        self.window.handle_events(events)
        self.ship_mgr.handle_events(events)

    def run(self):
        self.running = True
        while self.running:
            self.clock.tick(FPS_TARGET)
            self.handle_events()
            self.draw()
        pygame.quit()

    def stop(self):
        self.running = False

    def draw(self):
        self.window.draw(self.ship_mgr)


if __name__ == '__main__':
    Game().run()
