import pyxel
from constants import (
    TILE_SIZE,
    damaging_tiles,
    ladder_tiles,
    one_way_platform_tiles,
    solid_tiles,
)

from cavio.entities.entity import Entity


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


def is_solid_coord(wx: float, wy: float, tilemap_idx: int = 0) -> bool:
    """Check if the current tile is solid"""
    return is_solid_tile(int(wx) // TILE_SIZE, int(wy) // TILE_SIZE, tilemap_idx)


def is_ladder_coord(wx: float, wy: float, tilemap_idx: int = 0) -> bool:
    """Check if the current tile is a ladder"""
    return is_ladder_tile(int(wx) // TILE_SIZE, int(wy) // TILE_SIZE, tilemap_idx)


def is_solid_tile(tx: float, ty: float, tilemap_idx: int = 0) -> bool:
    """Check if the current tile is solid"""
    return pyxel.tilemaps[tilemap_idx].pget(tx, ty) in solid_tiles


def is_ladder_tile(tx: float, ty: float, tilemap_idx: int = 0) -> bool:
    """Check if the current tile is a ladder"""
    return pyxel.tilemaps[tilemap_idx].pget(tx, ty) in ladder_tiles


def is_colliding_below(entity, tilemap_idx=0):
    """Check if the entity is colliding with a solid tile below it.

    Args:
        entity: The entity to check (must have x, y, width, height properties)
        tilemap_idx: The tilemap index to check against

    Returns:
        bool: True if the entity is colliding with a solid tile below
    """
    # Check the bottom edge of the entity, at 3 points (left, center, right)
    # This helps catch when the entity is partially on a platform
    left_x = entity.x + 2
    center_x = entity.x + entity.width // 2
    right_x = entity.x + entity.width - 2
    bottom_y = entity.y + entity.height

    # Check if any of the three points are on a solid tile
    return (
        is_solid_coord(left_x, bottom_y + 1, tilemap_idx)
        or is_solid_coord(center_x, bottom_y + 1, tilemap_idx)
        or is_solid_coord(right_x, bottom_y + 1, tilemap_idx)
        or is_on_one_way_platform(entity, tilemap_idx)
    )


def is_colliding_above(entity, tilemap_idx=0):
    """Check if the entity is colliding with a solid tile above it.

    Args:
        entity: The entity to check (must have x, y, width, height properties)
        tilemap_idx: The tilemap index to check against

    Returns:
        bool: True if the entity is colliding with a solid tile above
    """
    # Check the top edge of the entity
    left_x = entity.x + 2
    center_x = entity.x + entity.width // 2
    right_x = entity.x + entity.width - 2
    top_y = entity.y

    return (
        is_solid_coord(left_x, top_y - 1, tilemap_idx)
        or is_solid_coord(center_x, top_y - 1, tilemap_idx)
        or is_solid_coord(right_x, top_y - 1, tilemap_idx)
    )


def is_colliding_left(entity: Entity, tilemap_idx=0):
    """Check if the entity is colliding with a solid tile to its left.

    Args:
        entity: The entity to check (must have x, y, width, height properties)
        tilemap_idx: The tilemap index to check against

    Returns:
        bool: True if the entity is colliding with a solid tile to the left
    """
    # Check the left edge of the entity
    left_x = entity.x
    top_y = entity.y + 2
    middle_y = entity.y + entity.height // 2
    bottom_y = entity.y + entity.height - 2

    return (
        is_solid_coord(left_x - 1, top_y, tilemap_idx)
        or is_solid_coord(left_x - 1, middle_y, tilemap_idx)
        or is_solid_coord(left_x - 1, bottom_y, tilemap_idx)
    )


def is_colliding_right(entity, tilemap_idx=0):
    """Check if the entity is colliding with a solid tile to its right.

    Args:
        entity: The entity to check (must have x, y, width, height properties)
        tilemap_idx: The tilemap index to check against

    Returns:
        bool: True if the entity is colliding with a solid tile to the right
    """
    # Check the right edge of the entity
    right_x = entity.x + entity.width
    top_y = entity.y + 2
    middle_y = entity.y + entity.height // 2
    bottom_y = entity.y + entity.height - 2

    return (
        is_solid_coord(right_x + 1, top_y, tilemap_idx)
        or is_solid_coord(right_x + 1, middle_y, tilemap_idx)
        or is_solid_coord(right_x + 1, bottom_y, tilemap_idx)
    )


def is_on_one_way_platform(entity, tilemap_idx=0):
    """Check if the entity is on a one-way platform tile

    Args:
        entity: The entity to check (must have x, y, width, height properties)
        tilemap_idx: The tilemap index to check against

    Returns:
        bool: True if the entity is on a one-way platform
    """
    # Check the bottom edge of the entity
    left_x = entity.x + 2
    right_x = entity.x + entity.width - 2
    bottom_y = entity.y + entity.height
    center_x = entity.x + entity.width // 2
    # Check if any of the three points are on a one-way platform
    return (
        is_one_way_platform_tile(left_x, bottom_y, tilemap_idx)
        or is_one_way_platform_tile(center_x, bottom_y, tilemap_idx)
        or is_one_way_platform_tile(right_x, bottom_y, tilemap_idx)
    )


def is_one_way_platform_tile(tx, ty, tilemap_idx=0):
    """Check if the current tile is a one-way platform.

    Args:
        tx: Tile x coordinate
        ty: Tile y coordinate
        tilemap_idx: The tilemap index to check against

    Returns:
        bool: True if the tile is a one-way platform
    """
    return pyxel.tilemaps[tilemap_idx].pget(tx, ty) in one_way_platform_tiles


def resolve_collision(
    entity: Entity, dx: float, dy: float, tilemap_idx: int = 0
) -> tuple[float, float]:
    """Resolve collision by adjusting entity position.

    Args:
        entity: The entity to adjust
        dx: Movement in x direction
        dy: Movement in y direction
        tilemap_idx: The tilemap index to check against

    Returns:
        tuple: Adjusted (dx, dy) values
    """
    # First attempt to move horizontally
    test_x = entity.x + dx
    if dx > 0 and not any(
        is_solid_coord(test_x + entity.width, entity.y + y, tilemap_idx)
        for y in range(2, entity.height - 1, 4)
    ):
        new_dx = dx
    elif dx < 0 and not any(
        is_solid_coord(test_x, entity.y + y, tilemap_idx)
        for y in range(2, entity.height - 1, 4)
    ):
        new_dx = dx
    else:
        # Collision occurred, stop horizontal movement
        new_dx = 0

    # Then attempt to move vertically
    if dy > 0:
        # Moving down
        if not is_colliding_below(entity, tilemap_idx):
            new_dy = dy
        else:
            # Snap to the top of the platform
            tile_y = ((entity.y + entity.height + dy) // TILE_SIZE) * TILE_SIZE
            new_dy = tile_y - (entity.y + entity.height)
    elif dy < 0:
        # Moving up
        if not is_colliding_above(entity, tilemap_idx):
            new_dy = dy
        else:
            # Snap to the bottom of the blocking tile
            tile_y = ((entity.y + dy) // TILE_SIZE + 1) * TILE_SIZE
            new_dy = tile_y - entity.y
    else:
        new_dy = 0

    return new_dx, new_dy


'''
def calculate_bounce(entity, collision_normal, bounce_factor=0.5):
    """Calculate bounce direction and velocity after a collision.

    Args:
        entity: The entity to bounce
        collision_normal: A tuple (nx, ny) normal vector of the surface hit
        bounce_factor: How bouncy the surface is (0-1, higher = more bounce)

    Returns:
        tuple: New velocity (vx, vy)
    """
    nx, ny = collision_normal

    # Get dot product of velocity and normal
    dot = entity.velocity.x * nx + entity.velocity.y * ny

    # Calculate reflection
    new_vx = entity.velocity.x - 2 * dot * nx
    new_vy = entity.velocity.y - 2 * dot * ny

    # Apply bounce factor
    new_vx *= bounce_factor
    new_vy *= bounce_factor

    return new_vx, new_vy
'''


# ------ Special Surface Types ------
def is_on_special_surface(
    tx: int, ty: int, surface_set: set[tuple[int, int]], tilemap_idx: int = 0
) -> bool:
    """Check if the current tile is a special surface type.

    Args:
        tx: Tile x coordinate
        ty: Tile y coordinate
        surface_set: A set of tile coordinates that are considered special surfaces
        tilemap_idx: The tilemap index to check against

    Returns:
        bool: True if the tile is a special surface type
    """
    return pyxel.tilemaps[tilemap_idx].pget(tx, ty) in surface_set


def is_damaging_surface(tx, ty, tilemap_idx=0):
    """Check if the current tile is a damaging surface (spikes, lava, etc).

    Args:
        tx: Tile x coordinate
        ty: Tile y coordinate
        tilemap_idx: The tilemap index to check against

    Returns:
        bool: True if the tile is a damaging surface
    """
    return is_on_special_surface(tx, ty, damaging_tiles, tilemap_idx)


def is_entity_on_special_surface(
    entity: Entity, surface_set: set[tuple[int, int]], tilemap_idx: int = 0
) -> bool:
    """Check if an entity is touching a damaging surface.

    Args:
        entity: The entity to check
        tilemap_idx: The tilemap index to check against

    Returns:
        bool: True if the entity is on a damaging surface
    """
    # Check multiple points around the entity's bounding box
    for x in range(entity.x + 2, entity.x + entity.width - 1, 4):
        for y in range(entity.y + 2, entity.y + entity.height - 1, 4):
            tx = x // TILE_SIZE
            ty = y // TILE_SIZE
            if is_on_special_surface(tx, ty, surface_set, tilemap_idx):
                return True
    return False


def is_entity_on_damaging_surface(entity: Entity, tilemap_idx: int = 0) -> bool:
    """Check if an entity is on a damaging surface.

    Args:
        entity: The entity to check
        tilemap_idx: The tilemap index to check against

    Returns:
        bool: True if the entity is on a damaging surface
    """
    return is_entity_on_special_surface(entity, damaging_tiles, tilemap_idx)


def is_entity_on_ladder(entity: Entity, tilemap_idx: int = 0) -> bool:
    """Check if an entity is on a ladder.

    Args:
        entity: The entity to check
        tilemap_idx: The tilemap index to check against

    Returns:
        bool: True if the entity is on a ladder
    """
    return is_entity_on_special_surface(entity, ladder_tiles, tilemap_idx)
