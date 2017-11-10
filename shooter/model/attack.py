
from shooter.model.ship import Ship


class Attack(Ship):
    def __init__(self, location=(200, 200)):
        Ship.__init__(self,
                      ship_type="Attack",
                      image_file_name="Attack1.png",
                      size=70,
                      health=1000,
                      location=location)


