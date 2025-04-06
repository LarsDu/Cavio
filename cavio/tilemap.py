from functools import cache

import pyxel

from cavio.constants import TILE_SIZE


@cache
def tile_coords_to_world_coords(*args: tuple[float | int]) -> tuple[int, int]:
    return tuple(int(arg * TILE_SIZE) for arg in args)
