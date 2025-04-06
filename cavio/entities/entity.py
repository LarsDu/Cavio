from cavio.interfaces import Drawable, Updatable, Damagable

class Entity(Drawable, Updatable):
    def __init__(self, x: float, y: float, w: float, h: float) -> None:
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.is_active: bool = False
        self.is_alive: bool = False
        self.dx: float = 0
        self.dy: float = 0

    def update(self):
        pass

    def draw(self):
        pass


class DamagableEntity(Entity, Damagable):
    def __init__(
        self,
        x: float = 0.0,
        y: float = 0.0,
        w: int = 16,
        h: int = 16,
        hp: int = 1,
        damage: int = 1,
    ):
        super().__init__(x, y, w, h)
        self.hp = hp
        self.damage = damage

