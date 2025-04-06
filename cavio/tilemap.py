from functools import cache

import pyxel

from cavio.constants import TILE_SIZE


@cache
def tile_coords_to_world_coords(tx: int, ty: int) -> tuple[int, int]:
    return (tx * TILE_SIZE, ty * TILE_SIZE)
