from cavio.entities.entity import DamagableEntity


class ZombieTurtle(DamagableEntity):
    def __init__(
        self,
        x: float = 0.0,
        y: float = 0.0,
        w: int = 16,
        h: int = 16,
        hp: int = 1,
        damage: int = 1,
    ):
        super().__init__(x, y, w, h, hp, damage)

    def update(self):
        pass

    def draw(self):
        pass


class Robot(DamagableEntity):
    def __init__(
        self,
        x: float = 0.0,
        y: float = 0.0,
        w: int = 16,
        h: int = 16,
        hp: int = 1,
        damage: int = 1,
    ):
        super().__init__(x, y, w, h, hp, damage)
