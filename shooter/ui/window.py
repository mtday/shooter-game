
import pygame
import time

from shooter.config.colors import BLACK

from shooter.config.settings import PREFERRED_WINDOW_SIZES
from shooter.config.settings import WINDOW_TITLE


class Window:
    def __init__(self, client):
        self.client = client
        self.full_screen = False
        (self.screen, self.window_settings) = Window.create_screen(self.full_screen)
        pygame.display.set_caption(WINDOW_TITLE)

    @staticmethod
    def create_screen(full_screen):
        if full_screen:
            window_settings = pygame.HWSURFACE | pygame.DOUBLEBUF | pygame.FULLSCREEN
            screen = pygame.display.set_mode(Window.get_display_mode(), window_settings)
        else:
            window_settings = pygame.DOUBLEBUF
            screen = pygame.display.set_mode(PREFERRED_WINDOW_SIZES[-1], window_settings)
        return screen, window_settings

    @staticmethod
    def get_display_mode():
        available = pygame.display.list_modes()
        if len(available) > 0:
            for mode in available:
                for preferred in PREFERRED_WINDOW_SIZES:
                    if mode[0] == preferred[0] and mode[1] == preferred[1]:
                        return mode
            return available[int(len(available) / 2)]
        return PREFERRED_WINDOW_SIZES[-1]

    def handle_events(self, events):
        for event in events:
            if event.type == pygame.QUIT:
                self.client.stop()
            elif event.type == pygame.VIDEORESIZE:
                self.screen = pygame.display.set_mode(event.size, self.window_settings)
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                self.client.stop()

    def draw(self, ship_mgr):
        self.screen.fill(BLACK)
        ship_mgr.draw(self.screen)
        pygame.display.flip()

