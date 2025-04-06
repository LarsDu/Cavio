SCREEN_WIDTH = 256
SCREEN_HEIGHT = 256
TILE_SIZE = 8


# EDITOR MARKERS (x,y)
PLAYER_MARKER = (8, 5)
ZOMBIE_MARKER = (0, 11)
BAT_MARKER = (0,9)
GEM_MARKER = (0,15)

## Tilemap indices
SOLID_BRICK_LIGHT = (2,0)
SOLID_BRICK_LIGHT_TOP = (2,1)
SOLID_BRICK_DARK = (3,0)
SOLID_BRICK_DARK_TOP = (3,1)

## Special tiles
BASIC_LADDER = (0, 13)


# Sprites (tx, ty, tw, th)

## Player
PLAYER_IDLE = (0, 3, 2, 2)
PLAYER_WALK1 = (0, 5, 2, 2)
PLAYER_WALK2 = (2, 5, 2, 2)
PLAYER_JUMP = (0, 5, 2, 2) # TODO
PLAYER_FALL = (0, 5, 2, 2) # TODO
PLAYER_CLIMB1 = (4 ,5, 2, 2)
PLAYER_CLIMB2 = (6 ,5, 2, 2)
PLAYER_SHOOT_RIGHT = (2, 3, 2, 2)
PLAYER_SHOOT_UP_RIGHT = (4,3, 2, 2)
PLAYER_SHOOT_DOWN_RIGHT = (8,3, 2, 2)

## Enemy
ZOMBIE_WALK1 = (2,11,2,2)
ZOMBIE_WALK2 = (4, 11, 2, 2)

ROBOT_WALK1 = (2,7,2,2)
ROBOT_WALK2 =  (4,7,2,2)


## Projectiles
FIREBALL1 = (0, 32, 16, 16)
FALLING_ROCK = (4,13,1,1)
FALLING_SHARD = (5,13,1,2)

# Explosions 
EXPLOSION1 = (6,9,2,2)

# Powerups
DROPLET = (6,13,1,1)
GEM = (2,15,2,2)

# Environment
LADDER = (0,13,2,2)

# TILE sets with special properties

solid_tiles = {
   SOLID_BRICK_LIGHT,
   SOLID_BRICK_LIGHT_TOP,
   SOLID_BRICK_DARK,
   SOLID_BRICK_DARK_TOP,
}

ladder_tiles = {
    BASIC_LADDER,
}






