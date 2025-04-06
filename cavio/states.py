import pyxel

from cavio.interfaces import Updatable


class State(Updatable, Drawable):
    def __init__(self, name: str):
        self.name = name

    def update(self):
        pass
