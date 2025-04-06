from enum import Enum

from cavio.entities.entity import DamagableEntity
from cavio.states import State


class PlayerMovementState(Enum):
    IDLE = 0
    GROUNDED = 1
    AIR = 2
    ATTACKING = 3
    DYING = 4


class PlayerIdleState(State):
    def __init__(self):
        super().__init__()

    def update(self):
        pass

    def draw(self):
        pass


class PlayerWalkingState(State):
    def __init__(self):
        super().__init__()

    def update(self):
        pass


class Player(DamagableEntity):
    def __init__(self, x: float, y: float):
        super().__init__(x, y, 16, 16, 100, 10)
        self.movement_state: PlayerMovementState = PlayerMovementState.IDLE

    def update(self):
        self.movement_state.update()

    def draw(self):
        self.movement_state.draw()
