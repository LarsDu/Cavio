from cavio.entities.entity import DamagableEntity

class Player(DamagableEntity):
    def __init__(self, x: float, y: float):
        super().__init__(x, y, 16, 16, 100, 10)

    def update(self):
        pass

    def draw(self):
        pass


