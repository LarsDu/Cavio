from cavio.interfaces import Singleton

class GameManager(metaclass=Singleton):
    def __init__(self) -> None:
        self.score: int = 0
