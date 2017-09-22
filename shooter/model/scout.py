
from shooter.model.ship import Ship
from shooter.config.colors import WHITE


class Scout(Ship):
    def __init__(self):
        Ship.__init__(self, type="Scout", size=20, location=(100, 100), health=500, color=WHITE)


