from cavio.entities.entity import DamagableEntity
from cavio.interfaces import Collidable


class ZombieTurtle(DamagableEntity, Collidable):
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

    def collide(self, other: Collidable):
        pass

    def on_collision_enter(self, other: Collidable):
        pass


class Robot(DamagableEntity, Collidable):
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

    def on_collision_enter(self, other: Collidable):
        pass
