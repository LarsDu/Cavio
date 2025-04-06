import pyxel

from constants import TILE_SIZE, solid_tiles, ladder_tiles

def is_solid_coord(wx: float, wy: float, tilemap_idx: int = 0) -> bool:
    """Check if the current tile is solid"""
    return is_solid_tile(
        int(wx) // TILE_SIZE, int(wy) // TILE_SIZE, tilemap_idx
    )

def is_ladder_coord(wx: float, wy: float, tilemap_idx: int = 0) -> bool:
    """Check if the current tile is a ladder"""
    return is_ladder_tile(
        int(wx) // TILE_SIZE, int(wy) // TILE_SIZE, tilemap_idx
    )

def is_solid_tile(tx: float, ty: float, tilemap_idx: int = 0) -> bool:
    """Check if the current tile is solid
    """
    return pyxel.tilemaps[tilemap_idx].pget(tx, ty) in solid_tiles


def is_ladder_tile(tx: float, ty: float, tilemap_idx: int = 0) -> bool:
    """Check if the current tile is a ladder"""
    return pyxel.tilemaps[tilemap_idx].pget(tx, ty) in ladder_tiles
 

def collide_aabb(
    x1: float,
    y1: float,
    w1: float,
    h1: float,
    x2: float,
    y2: float,
    w2: float,
    h2: float,
) -> bool:
    """Check if two axis-aligned bounding boxes collide

    Args:
        x1: First box x position
        y1: First box y position
        w1: First box width
        h1: First box height
        x2: Second box x position
        y2: Second box y position
        w2: Second box width
        h2: Second box height

    Returns:
        bool: True if the boxes collide
    """
    return x1 < x2 + w2 and x1 + w1 > x2 and y1 < y2 + h2 and y1 + h1 > y2


def pushback_horz(
        
)