from enum import Enum, auto

import pyxel

from cavio.collisions import (
    is_colliding_below,
    resolve_horizontal_collision,
    resolve_vertical_collision,
)
from cavio.constants import (
    GRAVITY,
    PLAYER_IDLE,
    PLAYER_WALK1,
    PLAYER_WALK2,
    TERMINAL_VELOCITY,
    TILE_SIZE,
    TRANSPARENCY_COLOR,
)
from cavio.entities.entity import DamagableEntity
from cavio.states import State, StateMachine
from cavio.tilemap import tile_coords_to_world_coords


class PlayerMovementState(Enum):
    GROUND = auto()
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


class PlayerGroundState(PlayerState):
    key = PlayerMovementState.GROUND

    def __init__(self, player: "Player"):
        super().__init__(player)

    def update(self):
        self.player.dx = self.player.dx * (1 - self.player.default_friction)
        if abs(self.player.dx) < 0.01:
            self.player.dx = 0
        if pyxel.btn(pyxel.KEY_RIGHT) or pyxel.btn(pyxel.GAMEPAD1_BUTTON_DPAD_RIGHT):
            self.player.is_facing_right = True
            self.player.dx = self.player.speed
        elif pyxel.btn(pyxel.KEY_LEFT) or pyxel.btn(pyxel.GAMEPAD1_BUTTON_DPAD_LEFT):
            self.player.is_facing_right = False
            self.player.dx = -self.player.speed
        if self.player.is_grounded and (
            pyxel.btn(pyxel.KEY_UP)
            or pyxel.btn(pyxel.KEY_SPACE)
            or pyxel.btn(pyxel.GAMEPAD1_BUTTON_A)
        ):
            self.player.dy = -self.player.jump
            self.player.is_grounded = False

        # Horizontal movement
        self.player.dx = resolve_horizontal_collision(self.player, self.player.dx, 0)

        # Vertical movement
        ## Apply gravity
        self.player.dy = min(self.player.dy + GRAVITY, TERMINAL_VELOCITY)

        ## Resolve vertical collision
        prev_dy = self.player.dy
        self.player.dy = resolve_vertical_collision(self.player, self.player.dy, 0)

        self.player.x += self.player.dx
        self.player.y += self.player.dy

        # If player was pushed back from collision, zero out velocity
        # to avoid bounce. Note this can be disabled to enable bounce.
        if prev_dy > 0 and self.player.dy < 0:
            self.player.dy = 0
            self.player.is_grounded = True

    def draw(self):
        u, v, w, h = tile_coords_to_world_coords(*PLAYER_IDLE)
        u1, v1, _, _ = tile_coords_to_world_coords(*PLAYER_WALK1)
        u2, v2, _, _ = tile_coords_to_world_coords(*PLAYER_WALK2)
        if self.player.is_grounded:
            if abs(self.player.dx) > 0.01:
                u, v = (
                    (u2, v2)
                    if (abs(self.player.dx) > 0 and (pyxel.frame_count >> 2) & 1)
                    else (u, v)
                )
        else:
            u, v, _, _ = tile_coords_to_world_coords(
                *PLAYER_WALK1
            )  # TODO: Add air animation
        w = w if self.player.is_facing_right else -w
        pyxel.blt(self.player.sx, self.player.sy, 0, u, v, w, h, TRANSPARENCY_COLOR)


class Player(DamagableEntity):
    jump = 4.0
    speed = 4.0
    default_friction = 0.5

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
                PlayerMovementState.GROUND: PlayerGroundState(self),
            }
        )
        self.movement_state = PlayerMovementState.GROUND

    def update(self):
        self._movement_state.update()

    def draw(self):
        self._movement_state.draw()
