from typing import TYPE_CHECKING

from cavio.interfaces import Damagable, Drawable, Updatable

if TYPE_CHECKING:
    from cavio.camera import Camera


class Entity(Drawable, Updatable):
    @property
    def sx(self) -> int:
        return self.x - self.camera.x

    @property
    def sy(self) -> int:
        return self.y - self.camera.y

    def __init__(self, x: float, y: float, w: float, h: float) -> None:
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.is_facing_right: bool = True
        self.is_active: bool = False
        self.is_alive: bool = False
        self.is_grounded: bool = True
        self.dx: float = 0
        self.dy: float = 0

        from cavio.camera import Camera  # avoid circular import

        self.camera = Camera()

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
