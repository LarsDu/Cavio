from enum import Enum, auto

import pyxel

from cavio.constants import PLAYER_IDLE, PLAYER_WALK1, PLAYER_WALK2, TRANSPARENCY_COLOR
from cavio.entities.entity import DamagableEntity
from cavio.states import State, StateMachine
from cavio.tilemap import tile_coords_to_world_coords


class PlayerMovementState(Enum):
    WALKING = auto()
    AIR = auto()
    DYING = auto()


class PlayerState(State):
    key: PlayerMovementState

    def __init__(self, player: "Player"):
        super().__init__()
        self.player = player

    def update(self):
        pass

    def draw(self):
        pass


class PlayerWalkingState(PlayerState):
    key = PlayerMovementState.WALKING

    def __init__(self, player: "Player"):
        super().__init__(player)

    def update(self):
        self.player.dx = 0
        self.player.dy = 0
        if pyxel.btn(pyxel.KEY_RIGHT):
            self.player.is_facing_right = True
            self.player.dx = self.player.speed
        elif pyxel.btn(pyxel.KEY_LEFT):
            self.player.is_facing_right = False
            self.player.dx = -self.player.speed
        elif (
            pyxel.btn(pyxel.KEY_UP)
            or pyxel.btn(pyxel.KEY_SPACE)
            or pyxel.btn(pyxel.GAMEPAD1_BUTTON_A)
        ):
            self.player.dy = -self.player.jump
        elif pyxel.btn(pyxel.KEY_DOWN):
            self.player.dx = 0
            self.player.dy = 0
        self.player.x += self.player.dx
        self.player.y += self.player.dy

    def draw(self):
        u, v, w, h = tile_coords_to_world_coords(*PLAYER_WALK1)
        u2, v2, _, _ = tile_coords_to_world_coords(*PLAYER_WALK2)
        u, v = (
            (u2, v2)
            if (abs(self.player.dx) > 0 and pyxel.frame_count // 3 & 1)
            else (u, v)
        )
        w = w if self.player.is_facing_right else -w
        pyxel.blt(self.player.sx, self.player.sy, 0, u, v, w, h, TRANSPARENCY_COLOR)


class Player(DamagableEntity):
    jump = 2
    speed = 2.5

    @property
    def movement_state(self) -> PlayerMovementState:
        return self._movement_state.key

    @movement_state.setter
    def movement_state(self, state: PlayerMovementState):
        self._movement_state = self.state_machine[state]

    def __init__(self, x: float, y: float):
        super().__init__(x, y, 16, 16, 100, 10)

        self.state_machine = StateMachine(
            {
                PlayerMovementState.WALKING: PlayerWalkingState(self),
            }
        )
        self.movement_state = PlayerMovementState.WALKING

    def update(self):
        self._movement_state.update()

    def draw(self):
        self._movement_state.draw()
