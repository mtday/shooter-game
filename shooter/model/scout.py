
from shooter.model.ship import Ship


class Scout(Ship):
    def __init__(self, location=(100, 100)):
        Ship.__init__(self,
                      ship_type="Scout",
                      size=40,
                      health=500,
                      location=location)


