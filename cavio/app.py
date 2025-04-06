import pyxel

from cavio.constants import SCREEN_HEIGHT, SCREEN_WIDTH
from cavio.levels import level_factory


class App:

    @property
    def level_id(self) -> int:
        if self.level is None:
            return -1
        return self.level.id

    @level_id.setter
    def level_id(self, level_id: int) -> None:
        if level_id != self.level_id:
            if self.level is not None:
                self.level.on_end()
            self.level = level_factory(level_id)
            if self.level is not None:
                self.level.on_start()

    def __init__(self) -> None:
        pyxel.init(SCREEN_WIDTH, SCREEN_HEIGHT)
        pyxel.load("assets/cavio.pyxres")
        self.level = None
        self.level_id = 1  # TODO: Switch to 0 for main menu
        pyxel.run(self.update, self.draw)

    def draw(self):
        pyxel.cls(0)
        self.level.draw()

    def update(self):
        self.level.update()
