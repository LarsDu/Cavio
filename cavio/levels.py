import pyxel

from cavio.background import Background
from cavio.camera import Camera
from cavio.constants import PLAYER_MARKER, ZOMBIE_MARKER, marker_tiles
from cavio.entities.enemies import ZombieTurtle
from cavio.entities.player import Player
from cavio.interfaces import Drawable, Updatable
from cavio.tilemap import tile_coords_to_world_coords


class Level(Drawable, Updatable):
    id: int

    def __init__(self, tx: int, ty: int, tw: int, th: int) -> None:
        self.tx = tx
        self.ty = ty
        self.tw = tw
        self.th = th

        # The following fields are typically overwritten in subclasses
        self.player = Player(PLAYER_MARKER[0], PLAYER_MARKER[1])  # Overwritten in
        self.camera = Camera()
        self.background = Background()
        self.entities = []
        self.init_level()

    def on_start(self) -> None:
        pass

    def on_end(self) -> None:
        pass

    def init_level(self) -> None:
        # Instantiate all entities in level bounds
        for ttx in range(self.tx, self.tx + self.tw):
            for tty in range(self.ty, self.ty + self.th):
                # Convert tile coordinates to image coordinates (which use tile indices)
                tile_value = pyxel.tilemaps[0].pget(ttx, tty)
                if tile_value == PLAYER_MARKER:
                    self.player = Player(**tile_coords_to_world_coords(ttx, tty))
                elif tile_value == ZOMBIE_MARKER:
                    self.entities.append(**tile_coords_to_world_coords(ttx, tty))

    def activate_entities_in_camera_view(self) -> None:
        # TODO: Activate entities in camera view and deactivate entities outside of camera view
        pass

    def deactivate_entities_outside_camera_view(self) -> None:
        # TODO: Deactivate entities outside of camera view
        pass

    def update(self):
        self.activate_entities_in_camera_view()
        self.deactivate_entities_outside_camera_view()
        self.background.update()
        self.player.update()
        self.camera.update()
        for entity in self.entities:
            if entity.is_active:
                entity.update()

        # Clean up dead entities
        self.entities = [entity for entity in self.entities if entity.is_alive]

    def draw(self):
        self.background.draw()
        self.player.draw()
        for entity in self.entities:
            if entity.is_active:
                entity.draw()


class MainMenuLevel(Level):
    id = 0

    def __init__(self) -> None:
        super().__init__()


class Level1(Level):
    id = 1

    def __init__(self) -> None:
        super().__init__()


class Level2(Level):
    id = 2

    def __init__(self) -> None:
        super().__init__()


class Level3(Level):
    id = 3

    def __init__(self) -> None:
        super().__init__()


def level_factory(level_id: int) -> Level:
    match level_id:
        case 0:
            return MainMenuLevel()
        case 1:
            return Level1()
        case 2:
            return Level2()
        case 3:
            return Level3()

        case _:
            raise ValueError(f"Invalid level id: {level_id}")
