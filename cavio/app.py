import pyxel
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from levels import level_factory, Level

class App:

    @property
    def level_id(self) -> Level:
        return self.level.id
    
    @level_id.setter
    def level_id(self, level_id: int) -> None:
        self._level = level_factory(level_id)

    def __init__(self) -> None:
        pyxel.init(SCREEN_WIDTH, SCREEN_HEIGHT)
        pyxel.load("assets/cavio.pyxres")
        self.level_id = 1
        pyxel.run(self.update, self.draw)

    def draw(self):
        pyxel.cls(0)
        self.level.draw()

    def update(self):
        self.level.update()



