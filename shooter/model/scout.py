
from shooter.model.ship import Ship


class Scout(Ship):
    def __init__(self):
        Ship.__init__(self,
                      ship_type="Scout",
                      size=20,
                      location=(100, 100),
                      health=500,
                      image_file_name="Scout1.png")


