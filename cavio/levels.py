from cavio.player import Player
from cavio.camera import Camera
from cavio.background import Background
from cavio.constants import PLAYER_MARKER
from cavio.interfaces import Drawable, Updatable

class Level(Drawable, Updatable):
    def __init__(self) -> None:

        self.player = Player()
        self.camera = Camera()
        self.background = Background()
        self.entities = []
    
    def on_start() -> None:
        pass

    def on_end() -> None:
        pass

    def draw(self):
        pass

    def update(self):
        pass



level_1 = Level()
level_2 = Level()
