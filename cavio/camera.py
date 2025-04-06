from cavio.interfaces import Drawable, Updatable
from cavio.singleton import Singleton
from cavio.constants import SCREEN_WIDTH, SCREEN_HEIGHT

class Camera(Drawable, Updatable, metaclass=Singleton):
    def __init__(self, w: float = SCREEN_WIDTH, h: float = SCREEN_HEIGHT) -> None:
        self.x = 0
        self.y = 0
        self.w = w
        self.h = h


    def update(self):
        pass

    def draw(self):
        pass
    
    
