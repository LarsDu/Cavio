SCREEN_WIDTH = 256
SCREEN_HEIGHT = 256
TILE_SIZE = 8


# EDITOR MARKERS (x,y)
PLAYER_MARKER = (16, 16)
TURTLE_MARKER = (32, 16)

## Tilemap indices
SOLID_GRASS = (0, 0)
SOLID_BRICK = (1, 0)

## Special tiles
BASIC_LADDER = (2, 0)


# Sprites (x, y, w, h)

## Player
PLAYER_SPRITE = (0, 0, 16, 16)

## Enemy
TURTLE_SPRITE = (0, 16, 16, 16)

## Projectiles
FIREBALL_SPRITE = (0, 32, 16, 16)




# TILE sets with special properties

solid_tiles = {
    SOLID_GRASS,
    SOLID_BRICK,
}

ladder_tiles = {
    BASIC_LADDER,
}






