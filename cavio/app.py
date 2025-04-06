import pyxel
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from levels import level_1, level_2

class App:
    def __init__(self) -> None:
        pyxel.init(SCREEN_WIDTH, SCREEN_HEIGHT)
        pyxel.load("assets/cavio.pyxres")
        self.level = level_1

    def draw(self):
        pyxel.cls(0)
        self.level.draw()

    def update(self):
        self.level.update()



