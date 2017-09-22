
from shooter.model.ship import Ship
from shooter.config.colors import CYAN


class Attack(Ship):
    def __init__(self):
        Ship.__init__(self, type="Attack", size=30, location=(200, 200), health=1000, color=CYAN)


