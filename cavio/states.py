from enum import Enum

import pyxel

from cavio.interfaces import Drawable, Updatable


class State(Updatable, Drawable):
    def __init__(self):
        pass

    def on_enter(self):
        pass

    def on_exit(self):
        pass

    def update(self):
        pass

    def draw(self):
        pass


class StateMachine:
    def __init__(self, states: dict[Enum, State]):
        self.states = states
        self.current_state = None

    def __getitem__(self, key: str) -> State:
        return self.states[key]

    def __setitem__(self, key: str, value: State):
        self.states[key] = value
