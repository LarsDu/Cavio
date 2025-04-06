import pyxel
from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from levels import Level, level_factory


class App:

    @property
    def level_id(self) -> int:
        if self._level is None:
            return -1
        return self._level.id

    @level_id.setter
    def level_id(self, level_id: int) -> None:
        if level_id != self.level_id:
            if self._level is not None:
                self._level.on_end()
            self._level = level_factory(level_id)
            if self._level is not None:
                self._level.on_start()

    def __init__(self) -> None:
        pyxel.init(SCREEN_WIDTH, SCREEN_HEIGHT)
        pyxel.load("assets/cavio.pyxres")
        self._level = None
        self.level_id = 1
        pyxel.run(self.update, self.draw)

    def draw(self):
        pyxel.cls(0)
        self.level.draw()

    def update(self):
        self.level.update()
