from cavio.interfaces import Drawable, Updatable

class Entity(Drawable, Updatable):
    def __init__(self, x: float, y: float, w: float, h: float) -> None:
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.is_active: bool = False
        self.is_alive: bool = False
    
    def update(self):
        pass
    
    def draw(self):
        pass
    
    
    
    
    
