import pyxel

from cavio.interfaces import Updatable


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
    def __init__(self):
        self.states = {}
        self.current_state = None

    def add_state(self, state: State):
        self.states[state.name] = state
