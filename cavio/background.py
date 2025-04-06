import pyxel

from cavio.camera import Camera
from cavio.constants import BACKGROUND_MINES, BACKGROUND_SKY, BACKGROUND_TILEMAP
from cavio.interfaces import Drawable, Updatable
from cavio.tilemap import tile_coords_to_world_coords


class Background(Drawable):
    u: float
    v: float
    w: float
    h: float

    def __init__(self) -> None:
        self.camera = Camera()

    def draw(self):
        pass


class BackgroundSky(Background):
    u, v, w, h = BACKGROUND_SKY

    def __init__(self) -> None:
        super().__init__()

    def draw(self):
        # Tile twice horizontally to create a seamless background filling the camera view horizontally
        for i in range(self.camera.w // self.w + 1):
            pyxel.bltm(
                self.x - self.camera.x + i * self.w,
                self.y - self.camera.y,
                BACKGROUND_TILEMAP,
                self.u,
                self.v,
                self.w,
                self.h,
            )


class BackgroundMine(Background):
    u, v, w, h = BACKGROUND_MINES

    def __init__(self) -> None:
        super().__init__()

    def draw(self):
        # Tile twice vertically to create a seamless background filling the camera view vertically
        for i in range(self.camera.h // self.h + 1):
            pyxel.bltm(
                self.x - self.camera.x,
                self.y - self.camera.y + i * self.h,
                BACKGROUND_TILEMAP,
                self.u,
                self.v,
                self.w,
                self.h,
            )
