from abc import ABC
from typing import Protocol


class Drawable(Protocol):
    def draw(self) -> None: ...


class Updatable(Protocol):
    def update(self) -> None: ...


class Movable(Protocol):
    x: float
    y: float
    dx: float
    dy: float


class Collidable(Protocol):
    def on_collision_enter(self, other: "Collidable") -> None: ...

    def on_collision_exit(self, other: "Collidable") -> None: ...


class Damagable(Protocol):
    hp: int
    damage: int
