from typing import TYPE_CHECKING

from cavio.constants import SCREEN_HEIGHT, SCREEN_WIDTH
from cavio.singleton import Singleton

if TYPE_CHECKING:
    from cavio.entities.entity import Entity


class Camera(metaclass=Singleton):
    def __init__(self) -> None:
        self.target: Entity | None = None
        self.x = 0
        self.y = 0
        self.w = SCREEN_WIDTH
        self.h = SCREEN_HEIGHT

    def update(self):
        if self.target is None:
            raise ValueError("No target set for camera")
        self.x = self.target.x - self.w / 2
        self.y = self.target.y - self.h / 2

    def draw(self):
        pass
