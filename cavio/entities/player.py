from enum import Enum

from cavio.entities.entity import DamagableEntity
from cavio.states import State


class PlayerState(Enum):
    IDLE = 0
    WALKING = 1
    JUMPING = 2
    FALLING = 3
    ATTACKING = 4
    DYING = 5


class Player(DamagableEntity):
    def __init__(self, x: float, y: float):
        super().__init__(x, y, 16, 16, 100, 10)
        self.state: State = PlayerState.IDLE

    def update(self):
        self.state.update()

    def draw(self):
        self.state.draw()
