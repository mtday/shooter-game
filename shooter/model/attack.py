
from shooter.model.ship import Ship


class Attack(Ship):
    def __init__(self):
        Ship.__init__(self,
                      ship_type="Attack",
                      size=100,
                      location=(200, 200),
                      health=1000,
                      image_file_name="Attack1.png")


